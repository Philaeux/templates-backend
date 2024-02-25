import pytest

from template.graphql.schema import schema
from template.backend import get_context


@pytest.fixture()
async def context():
    """Define the context used by the graphql application"""
    context = await get_context()
    return context


@pytest.mark.asyncio
async def test_qa(context):
    """Test the execution of the querry qa"""
    
    query = """
        query TestQuery {
            qa {
                id
            }
        }
    """

    result = await schema.execute(
        query,
        context_value=context,
        variable_values={},
    )

    assert result.errors is None
    assert result.data["qa"] == {}
