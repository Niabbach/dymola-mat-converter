import pandas as pd
import numpy as np

def normalize(dm):
    datasets = [k for k in dm.mat if k.startswith("data")]
    main = max(datasets, key=lambda k: dm.mat[k].shape[1])
    time = dm.mat[main][0]

    timeseries = {"time": time}
    static = {}

    for name in dm.names():
        try:
            val = dm.data(name)
            if isinstance(val, np.ndarray):
                if val.shape == time.shape:
                    timeseries[name] = val
                else:
                    static[name] = val.tolist()
        except:
            pass

    return pd.DataFrame(timeseries), static
