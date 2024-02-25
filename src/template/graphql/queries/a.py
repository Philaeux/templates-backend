import strawberry
from strawberry.types import Info

from template.graphql.types.generated import ApiError


@strawberry.type
class QueryA:

    @strawberry.mutation
    async def qa(self, info: Info) -> ApiError:

        # Typical database access
        # with info.context['session_factory'](expire_on_commit=False) as session:
        # ...

        return ApiError(message="Not Implemented")
