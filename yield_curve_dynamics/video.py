import click
import numpy as np

from .data import load_csv
from .animate import create_animation


@click.command(name='video')
@click.option('-f', '--csv-file', type=click.File(mode='r'), default='-',
              help='CSV file containing parameters for ' +
                   'Nelson-Siegel-Svensson curves')
def cli_video(csv_file):
    '''Load CSV file and create a yield curve video.'''
    click.echo('Loading csv from {}'.format(csv_file.name))
    curves = list(load_csv(csv_file))
    click.echo('Successfully loaded {} curves'.format(len(curves)))
    t = np.linspace(0, 30, 200)
    anim = create_animation(curves, t)
    anim.save('yieldcurve.mp4')
    return 0
