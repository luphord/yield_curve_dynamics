import zipfile

import click


def download(start_date, end_date, output_file, aaa_curves):
    pass


@click.command(name='download')
@click.option('-s', '--start-date', type=str, required=True,
              help='start date for curve download')
@click.option('-e', '--end-date', type=str, required=True,
              help='end date for curve download')
@click.option('-f', '--zip-file',
              type=click.Path(file_okay=True, dir_okay=False,
                              resolve_path=True),
              required=True,
              help='ZIP file for download output')
@click.option('--aaa-curves/--no-aaa-curves', default=True,
              help='Download curve data bootstrapped from AAA rated bonds')
def cli_download(start_date, end_date, zip_file, aaa_curves):
    '''Download raw yield curve data parameters from ECB.'''
    rated = 'AAA rated' if aaa_curves else 'all Euro area'
    click.echo(f'Downloading ECB yield curve data for {rated} bonds ' +
               f'from {start_date} until {end_date} and storing as {zip_file}')
    with zipfile.ZipFile(zip_file, 'w') as z:
        with z.open('data.csv', 'w') as csv_file:
            download(start_date, end_date, csv_file, aaa_curves)
    return 0
