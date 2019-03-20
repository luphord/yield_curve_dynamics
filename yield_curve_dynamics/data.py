import io
import csv
import zipfile
from collections import defaultdict

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


_relevant_params = ['BETA0', 'BETA1', 'BETA2', 'BETA3', 'TAU1', 'TAU2']


@click.command(name='transform')
@click.option('-i', '--ecb-input',
              type=click.Path(exists=True, file_okay=True, dir_okay=False,
                              resolve_path=True),
              required=True,
              help='ZIP file containing a CSV as provided ' +
                   'by European Central Bank')
@click.option('-o', '--csv-output',
              type=click.Path(exists=False, file_okay=True, dir_okay=False,
                              resolve_path=True),
              required=True,
              help='CSV output file with Nelson-Siegel-Svensson parameters')
def cli_transform(ecb_input, csv_output):
    '''Load data as provided by ECB and transform to parameters CSV.'''
    click.echo('Loading ECB data from {}'.format(ecb_input))
    with zipfile.ZipFile(ecb_input) as z:
        with io.TextIOWrapper(z.open('data.csv', 'r')) as f:
            reader = csv.DictReader(f)
            filtered = [dict(param=row['DATA_TYPE_FM'].lower(),
                             date=row['TIME_PERIOD'],
                             value=row['OBS_VALUE'])
                        for row in reader
                        if row['DATA_TYPE_FM'] in _relevant_params]

    pivot = defaultdict(dict)
    for row in filtered:
            d = pivot[row['date']]
            d['date'] = row['date']
            d[row['param']] = row['value']

    pivot = sorted(pivot.values(), key=lambda row: row['date'])
    headers = ['date'] + [p.lower() for p in _relevant_params]
    click.echo(f'Writing Nelson-Siegel-Svensson parameters to {csv_output}')
    with open(csv_output, 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(pivot)
