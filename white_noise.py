def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    import pandas as pd
    import matplotlib.pyplot as plt
    import statsmodels.tsa.api as smt
    import statsmodels.api as sm
    import scipy.stats as scs

    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):
        fig = plt.figure(figsize=figsize)
        # mpl.rcParams['font.family'] = 'Ubuntu Mono'
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))

        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        # Autocorrelation
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.5)
        # Partial Autocorrelation
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.5)
        # QQ Plot
        sm.qqplot(y, line='s', ax=qq_ax)
        qq_ax.set_title('QQ Plot')
        # Probability plot
        scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        plt.tight_layout()
    return plt


if __name__ == "__main__":
    import numpy as np
    np.random.seed(1)

    # plot of discrete white noise
    mean = 1.0
    randser = np.random.normal(loc=mean, size=1000)
    plt = tsplot(randser, lags=30)
    plt.show()
