# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '9/17/15'

import multiprocessing
import click
import gunicorn.app.base
import six

from ironsmith.app import Application
from ..main import cli


class Server(gunicorn.app.base.BaseApplication):
    """Integrated gunicorn application server"""

    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super(Server, self).__init__()

    def load_config(self):
        config = dict(
            [(key, value) for key, value in six.iteritems(self.options)
             if key in self.cfg.settings and value is not None])
        for key, value in six.iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


@cli.command('runserver', short_help='run server.')
@click.option('-b', '--bind', default='127.0.0.1:8000', type=str,
              help='address and port to bind to.')
@click.option('-w', '--workers', default=0, type=click.IntRange(0, None),
              envvar='IRONSMITH_WORKERS',
              help='''number of worker processes, default is cpu_num * 2.
              Read from envvar IRONWORKER_WORKERS.''')
@click.option('--threads', default=1, type=click.IntRange(1, None),
              envvar='STONEMASON_THREADS',
              help='''number of threads per process, default is 1.
              Read from envvar IRONWORKER_THREADS.  ''')
def run_server_command(bind, workers, threads):
    ctx = click.get_current_context().obj

    host, port = bind.split(':')
    port = int(port)

    app = Application()

    if ctx['verbose']:
        log_level = 'debug'
    else:
        log_level = 'info'

    if ctx['debug']:
        app.run(host=host, port=port, debug=ctx['debug'], )
    else:
        if workers == 0:
            # by default, use cpu num * 2
            workers = multiprocessing.cpu_count() * 2

        options = {
            'workers': workers,
            'threads': threads,
            'bind': bind,
            'loglevel': log_level,
            'errorlog': '-',  # log to stderr
            'preload_app': False
        }
        server = Server(app, options)
        server.run()
