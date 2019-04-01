import zipfile

import click


def download(start_date, end_date, output_file):
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
def cli_download(start_date, end_date, zip_file):
    '''Download raw yield curve data parameters from ECB.'''
    click.echo('Downloading ECB yield curve data ' +
               f'from {start_date} until {end_date} and storing as {zip_file}')
    with zipfile.ZipFile(zip_file, 'w') as z:
        with z.open('data.csv', 'w') as csv_file:
            download(start_date, end_date, csv_file)
    return 0
