import asyncio
import logging
from asyncio import ensure_future
from functools import wraps
from traceback import format_exception
from typing import Any, Callable, Coroutine, Union

from starlette.concurrency import run_in_threadpool

NoArgsNoReturnFuncT = Callable[[], None]
NoArgsNoReturnAsyncFuncT = Callable[[], Coroutine[Any, Any, None]]
NoArgsNoReturnDecorator = Callable[[Union[NoArgsNoReturnFuncT, NoArgsNoReturnAsyncFuncT]], NoArgsNoReturnAsyncFuncT]


def repeat_every(*,
                 seconds: float,
                 wait_first: bool = False,
                 logger: logging.Logger | None = None,
                 raise_exceptions: bool = False,
                 max_repetitions: int | None = None,
                 ) -> NoArgsNoReturnDecorator:
    """Function returning a decorator that modifies a function so it is periodically re-executed after its first call.

    The function it decorates should accept no arguments and return nothing. If necessary, this can be accomplished
    by using `functools.partial` or otherwise wrapping the target function prior to decoration.

    :param seconds: The number of seconds to wait between repeated calls
    :param wait_first: If True, the function will wait for a single period before the first call
    :param logger: The logger to use to log any exceptions raised by calls to the decorated function. If not provided,
    exceptions will not be logged by this function.
    :param raise_exceptions: If True, errors raised by the decorated function will be raised to the event loop's exception
    handler. Note that if an error is raised, the repeated execution will stop. Otherwise, exceptions are just logged
    and the execution continues to repeat.
    :param max_repetitions: The maximum number of times to call the repeated function. If `None`, the function is repeated
    forever.
    """

    def decorator(func: NoArgsNoReturnAsyncFuncT | NoArgsNoReturnFuncT) -> NoArgsNoReturnAsyncFuncT:
        """Converts the decorated function into a repeated, periodically-called version of itself"""
        is_coroutine = asyncio.iscoroutinefunction(func)

        @wraps(func)
        async def wrapped() -> None:
            repetitions = 0

            async def loop() -> None:
                nonlocal repetitions
                if wait_first:
                    await asyncio.sleep(seconds)
                while max_repetitions is None or repetitions < max_repetitions:
                    try:
                        if is_coroutine:
                            await func()  # type: ignore
                        else:
                            await run_in_threadpool(func)
                        repetitions += 1
                    except Exception as exc:
                        if logger is not None:
                            formatted_exception = "".join(format_exception(type(exc), exc, exc.__traceback__))
                            logger.error(formatted_exception)
                        if raise_exceptions:
                            raise exc
                    await asyncio.sleep(seconds)

            ensure_future(loop())

        return wrapped

    return decorator
    