import strawberry
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

# ORM MAPPING
strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


# How to add an orm mapping to strawberry type
#from obugs.database.entry import Entry as EntryEntity
#@strawberry_sqlalchemy_mapper.type(EntryEntity)
#class Entry:
#    pass


# OTHERS
@strawberry.type
class ApiError:
    message: str
