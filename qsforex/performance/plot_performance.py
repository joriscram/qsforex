#!/usr/bin/python
# -*- coding: utf-8 -*-

# plot_performance.py

import matplotlib.pyplot as plt
import pandas as pd
from qsforex.utilities import filepaths as fp

def create_perf_plt_csv(output_file_name = 'equity.csv'):
    output_path = fp.get_output_path(output_file_name)
    data = pd.DataFrame.from_csv(output_path)
    create_perf_plot(data)

def create_perf_plot(data):
    # Plot three charts: Equity curve,
    # period returns, drawdowns
    fig = plt.figure()
    # Set the outer colour to white
    fig.patch.set_facecolor('white')

    # Plot the equity curve
    ax1 = fig.add_subplot(311, ylabel='Portfolio value, %')
    data['Equity'].plot(ax=ax1, color="blue", lw=2.)
    plt.grid(True)

    # Plot the returns
    ax2 = fig.add_subplot(312, ylabel='Period returns, %')
    data['Returns'].plot(ax=ax2, color="black", lw=2.)
    plt.grid(True)

    # Plot the returns
    ax3 = fig.add_subplot(313, ylabel='Drawdowns, %')
    data['Drawdown'].plot(ax=ax3, color="red", lw=2.)
    plt.grid(True)

    # Plot the figure
    plt.show()


if __name__ == "__main__":
   create_perf_plot()
