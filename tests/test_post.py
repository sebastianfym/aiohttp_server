import aiohttp
import pytest


@pytest.mark.asyncio
async def test_post_request():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8000/hash', json={}) as resp:
            assert resp.status == 400
            assert await resp.json() == {"validation_errors": "Validation error"}

        async with session.post('http://localhost:8000/hash', json={"string": "string"}) as resp:
            assert resp.status == 200
            assert await resp.json() == {
                'hash_string': '473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8'}

        async with session.post('http://localhost:8000/hash', json={"string": 0}) as resp:
            assert resp.status == 200
            assert await resp.json() == {
                "hash_string": "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"}
