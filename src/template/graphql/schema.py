import strawberry

from template.graphql.mutations.a import ma
from template.graphql.queries.a import qa
from template.graphql.types import strawberry_sqlalchemy_mapper


@strawberry.type
class Mutation:
    ma = strawberry.mutation(resolver=ma)


@strawberry.type
class Query:
    qa = strawberry.field(resolver=qa)


strawberry_sqlalchemy_mapper.finalize()
additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())
schema = strawberry.Schema(query=Query, mutation=Mutation, types=additional_types)
