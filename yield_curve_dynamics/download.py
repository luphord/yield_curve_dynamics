import zipfile
from urllib.request import urlopen

import click

_URL = (
    'https://sdw-wsrest.ecb.europa.eu/service/data/YC/'
    'B.U2.EUR.4F.G_N_{aaa}.SV_C_YM.?'
    'startPeriod={start_date}&endPeriod={end_date}&format=csvdata'
)


def download(start_date, end_date, aaa_curves, output_file):
    url = _URL.format(aaa=('A' if aaa_curves else 'C'),
                      start_date=start_date,
                      end_date=end_date)
    with urlopen(url) as response:
        for line in response:
            output_file.write(line)


@click.command(name='download')
@click.option('-s', '--start-date', type=str, required=True,
              help='start date for curve download')
@click.option('-e', '--end-date', type=str, required=True,
              help='end date for curve download')
@click.option('--aaa-curves/--no-aaa-curves', default=True,
              help='Download curve data bootstrapped from AAA rated bonds')
@click.option('-f', '--zip-file',
              type=click.Path(file_okay=True, dir_okay=False,
                              resolve_path=True),
              required=True,
              help='ZIP file for download output')
def cli_download(start_date, end_date, aaa_curves, zip_file):
    '''Download raw yield curve data parameters from ECB.'''
    rated = 'AAA rated' if aaa_curves else 'all Euro area'
    click.echo(f'Downloading ECB yield curve data for {rated} bonds ' +
               f'from {start_date} until {end_date} and storing as {zip_file}')
    with zipfile.ZipFile(zip_file, 'w') as z:
        with z.open('data.csv', 'w') as csv_file:
            download(start_date, end_date, aaa_curves, csv_file)
    return 0
