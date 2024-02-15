from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from strawberry.fastapi import GraphQLRouter
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyLoader

from template.settings import Settings
from template.database.database import Database
from template.graphql.schema import schema

# App
settings = Settings()
app = FastAPI()

# Database
database = Database(uri=settings.database_uri, check_migrations=True)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# GraphQL
async def get_context():
    return {
        "settings": settings,
        "session_factory": database.session_factory,
        "sqlalchemy_loader": StrawberrySQLAlchemyLoader(bind=database.session_factory()),
    }


graphql_app = GraphQLRouter(
    schema,
    graphiql=settings.debug,
    context_getter=get_context,
)
app.include_router(graphql_app, prefix="/graphql")


@app.get('/hello')
async def hello(request: Request):
    return {"message": "Hello World"}
