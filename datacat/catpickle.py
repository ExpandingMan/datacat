import pickle
import click

# ========================================================================
#   catpickle.py:
#       This script will load up a pickle and launch directly into the 
#       debugger, giving access to the pickle as the object pkl.
# ========================================================================

@click.command()
@click.argument('pklfile', type=str)
def main(**kwargs):
    with open(kwargs['pklfile'], 'rb') as f:
        pkl = pickle.load(f)



    import ipdb; ipdb.set_trace()
    # pickle file loaded into object 'pkl'



if __name__ == '__main__':
    main()

