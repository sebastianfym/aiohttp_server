from aiohttp import web

from utillities import value_hash


async def get_view(request):
    return web.json_response({}, status=200)


async def post_view(request):
    body = await request.json()

    if "string" not in body.keys():
        data = {"validation_errors": "Validation error"}
        return web.json_response(data, status=400)

    return web.json_response({"hash_string": value_hash(str(body["string"]))}, status=200)