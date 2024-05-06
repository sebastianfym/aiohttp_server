import click
from aiohttp import web

from config import app


@click.command()
@click.option('--host', default='0.0.0.0', help='Host IP address')
@click.option('--port', default=8000, help='Port number')
def run_server(host, port):
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    run_server()
