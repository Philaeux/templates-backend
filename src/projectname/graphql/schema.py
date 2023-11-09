import strawberry

from projectname.graphql.mutations.a import MutationA

from projectname.graphql.queries.a import QueryA

from projectname.graphql.types import strawberry_sqlalchemy_mapper


@strawberry.type
class Mutation(MutationA):
    pass


@strawberry.type
class Query(QueryA):
    pass


strawberry_sqlalchemy_mapper.finalize()
additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())
schema = strawberry.Schema(query=Query, mutation=Mutation, types=additional_types)
