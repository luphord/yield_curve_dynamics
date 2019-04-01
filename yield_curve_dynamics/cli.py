# -*- coding: utf-8 -*-

'''Main command line interface for Yield Curve Dynamics.'''
import click

from .download import cli_download
from .data import cli_load_csv, cli_transform
from .video import cli_video


@click.group(name='yield_curve_dynamics')
def main():
    '''A cursory look at the dynamics of zero coupon bond yield curves.'''
    pass


main.add_command(cli_download)
main.add_command(cli_load_csv)
main.add_command(cli_transform)
main.add_command(cli_video)
