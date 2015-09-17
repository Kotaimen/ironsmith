# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '9/17/15'

import os

import click

import ironsmith

CONTEXT_SETTINGS = dict(
    auto_envvar_prefix='IRONSMITH',
    help_option_names=['-h', '--help'],
)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug', default=False, count=True,
              help='''enable debug mode.''')
@click.option('-v', '--verbose', default=False, count=True,
              help='being verbose.')
@click.version_option(ironsmith.__version__, message='Ironsmith %(version)s')
def cli(debug, verbose):
    """Ironsmith

    """
    ctx = click.get_current_context()
    ctx.obj = dict(
        debug=debug,
        verbose=verbose,
    )
