from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

# ORM MAPPING
strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


# How to add an orm mapping to strawberry type
from template.database.a import A as AEntity


@strawberry_sqlalchemy_mapper.type(AEntity)
class A:
    pass
