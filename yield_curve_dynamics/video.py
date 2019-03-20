import click
import numpy as np

from .data import load_csv
from .animate import create_animation


@click.command(name='video')
@click.option('-f', '--csv-file', type=click.File(mode='r'), default='-',
              help='CSV file containing parameters for ' +
                   'Nelson-Siegel-Svensson curves')
@click.option('-o', '--mp4-output',
              type=click.Path(exists=False, file_okay=True, dir_okay=False,
                              resolve_path=True),
              required=True,
              help='MP4 video output file')
def cli_video(csv_file, mp4_output):
    '''Load CSV file and create a yield curve video.'''
    click.echo('Loading csv from {}'.format(csv_file.name))
    curves = list(load_csv(csv_file))
    click.echo('Successfully loaded {} curves'.format(len(curves)))
    t = np.linspace(0, 30, 200)
    anim = create_animation(curves, t)
    anim.save(mp4_output)
    return 0
