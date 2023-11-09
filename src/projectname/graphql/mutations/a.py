import strawberry

from projectname.graphql.types import ApiError


@strawberry.type
class MutationA:

    @strawberry.mutation
    async def ma(self, info) -> ApiError:
        # Typical user check
        # current_user = check_user(info.context["settings"].jwt_secret_key,
        #                           info.context["request"].headers.get("Authorization"))

        # Typical database access
        # with info.context['session_factory'](expire_on_commit=False) as session:
        # ...

        return ApiError(message="Not Implemented")
