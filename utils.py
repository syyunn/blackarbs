def import_basic_modules():
    import os
    import sys

    import pandas as pd
    import pandas_datareader.data as web
    import numpy as np

    import statsmodels.formula.api as smf
    import statsmodels.tsa.api as smt
    import statsmodels.api as sm
    import scipy.stats as scs
    from arch import arch_model

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    p = print

    p('Machine: {} {}\n'.format(os.uname().sysname, os.uname().machine))
    p(sys.version)


def get_sample_data():
    import pandas as pd
    import pandas_datareader.data as web
    import numpy as np

    end = '2015-01-01'
    start = '2007-01-01'
    get_px = lambda x: web.DataReader(x, 'yahoo', start=start, end=end)[
        'Adj Close']

    symbols = ['SPY', 'TLT', 'MSFT']
    # raw adjusted close prices
    data = pd.DataFrame({sym: get_px(sym) for sym in symbols})
    # log returns
    lrets = np.log(data / data.shift(1)).dropna()
    print(lrets)


if __name__ == "__main__":
    # import_basic_modules()
    get_sample_data()
