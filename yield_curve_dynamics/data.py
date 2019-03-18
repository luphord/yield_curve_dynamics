import sys
import click


@click.command(name='load_csv')
@click.option('-f', '--csv-file', type=click.File(mode='r'), default='-',
              help='CSV file containing parameters for ' +
                   'Nelson-Siegel-Svensson curves')
def load_csv(csv_file):
    '''Load a sequence of Nelson-Siegel-Svensson curves from a CSV file.'''
    click.echo('Loading csv from {}'.format(csv_file.name))
    return 0
