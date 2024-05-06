from aiohttp import web

from views import get_view, post_view

app = web.Application()
app.add_routes([web.get('/healthcheck', get_view),
                web.post('/hash', post_view)])