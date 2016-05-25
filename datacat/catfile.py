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
@click.argument('fname', type=str)
def main(**kwargs):
    if ('pkl' in kwargs['fname']) | ('pic' in kwargs['fname']):
        with open(kwargs['fname'], 'rb') as f:
            cat = pickle.load(f)
        print('Object of type:', type(cat))
    elif 'csv' in kwargs['fname']:
        cat = pd.DataFrame.from_csv(kwargs['fname'], index_col=None)




    import ipdb; ipdb.set_trace()
    # file loaded into object 'cat'




if __name__ == '__main__':
    main()

