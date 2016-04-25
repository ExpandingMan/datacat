import pickle
import click
import pandas as pd
import numpy as np

# ========================================================================
#   catpickle.py:
#       This script will load up a pickle and launch directly into the 
#       debugger, giving access to the pickle as the object pkl.
# ========================================================================

@click.command()
@click.argument('csvfile', type=str)
def main(**kwargs):
    df = pd.DataFrame.from_csv(kwargs['csvfile'], index_col=None)



    import ipdb; ipdb.set_trace()
    # csv loaded into dataframe 'df'



if __name__ == '__main__':
    main()

