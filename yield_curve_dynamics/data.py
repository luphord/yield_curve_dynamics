import click
import pandas as pd
from nelson_siegel_svensson import NelsonSiegelSvenssonCurve


def load_csv(csv_file):
    eur_hist = pd.read_csv(csv_file, parse_dates=['date'], index_col=0)
    for ts, param in eur_hist.iterrows():
        yield ts.date(), NelsonSiegelSvenssonCurve(*param)


@click.command(name='load_csv')
@click.option('-f', '--csv-file', type=click.File(mode='r'), default='-',
              help='CSV file containing parameters for ' +
                   'Nelson-Siegel-Svensson curves')
def cli_load_csv(csv_file):
    '''Load a sequence of Nelson-Siegel-Svensson curves from a CSV file.'''
    click.echo('Loading csv from {}'.format(csv_file.name))
    curves = list(load_csv(csv_file))
    click.echo('Successfully loaded {} curves'.format(len(curves)))
    return 0
