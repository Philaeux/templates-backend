import strawberry

from template.graphql.types.generated import ApiError


@strawberry.type
class QueryA:

    @strawberry.mutation
    async def qa(self, info) -> ApiError:

        # Typical database access
        # with info.context['session_factory'](expire_on_commit=False) as session:
        # ...

        return ApiError(message="Not Implemented")
