import pandas as pd
import pickle
import click
from glue import qglue

@click.command()
@click.argument('fname', type=str)
def main(**kwargs):
    if ('pkl' in kwargs['fname']) | ('pic' in kwargs['fname']):
        with open(kwargs['fname'], 'rb') as f:
            df = pickle.load(f)
        # if a dictionary, assume all members are dataframes
        if isinstance(df, dict):
            qglue(**df)
    elif 'csv' in kwargs['fname']:
        df = pd.DataFrame.from_csv(kwargs['fname'], index_col=None)

    qglue(df=df)


if __name__ == '__main__':
    main()
