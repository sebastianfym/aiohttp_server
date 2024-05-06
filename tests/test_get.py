import aiohttp
import pytest


@pytest.mark.asyncio
async def test_get_request():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8000/healthcheck') as resp:
            assert await resp.json() == {}
            assert resp.status == 200
