import pandas as pd
import pickle
import click
from glue import qglue

@click.command()
@click.argument('pklfile', type=str)
def main(**kwargs):
    with open(kwargs['pklfile'], 'rb') as f:
        pkl = pickle.load(f)

    if isinstance(pkl, dict):
        qglue(**pkl)
    else:
        qglue(df=pkl)


if __name__ == '__main__':
    main()
