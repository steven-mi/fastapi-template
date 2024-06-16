import pytest


@pytest.mark.anyio
async def test_get_user_by_name_200(client):
    response = await client.get(
        "/users/test",
    )
    assert response.status_code == 200
    assert response.json()["user_name"] == "test"


@pytest.mark.anyio
async def test_get_all_users_200(client):
    response = await client.get(
        "/users",
    )
    assert response.status_code == 200
    assert len(response.json()) > 0
