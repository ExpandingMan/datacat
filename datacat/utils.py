import numpy as np
import pandas as pd
import pickle
import datetime


# ==========================================================================================
#   utils.py
#       some generally useful functions.  mostly dataframe manipulation
# ==========================================================================================


def disaggregate(df, col):
    """
    Disaggregates a dataframe, so that there are col[index] copies of each row.
    These rows will be differentiated with the new 'disagg_id' column.
    While this is a rather stupid operation because it creates a lot of degenerate data,
    it turns out to often make things much, much simpler and is often the quickest option.
    Should be about as efficient as this can get in pure python.
    """
    df = df.copy(deep=False)
    df['uid'] = df.index
    a = np.empty(df[col].sum(), dtype=np.int32)
    ids = np.empty(len(a), dtype=np.int32)
    idx = {0: 0}

    def filla(row):
        disagg_id = 0
        for i in range(row[col]):
            a[idx[0]] = row['uid']
            ids[idx[0]] = disagg_id
            disagg_id += 1
            idx[0] += 1

    df.apply(filla, axis=1)
    disagger = pd.DataFrame({'uid': a, 'disagg_id': ids})
    df = pd.merge(df, disagger, on='uid')
    df.drop('uid', axis=1, inplace=True)
    return df















