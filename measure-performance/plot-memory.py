#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import sys

def get_nfd_result() -> str:
    if len(sys.argv) < 3:
        print(
            "Usage:", sys.argv[0], "nfd_csv squid_csv \n", file=sys.stderr)
        exit(-1)
    return sys.argv[1]

def get_squid_result() -> str:
    if len(sys.argv) < 3:
        print(
            "Usage:", sys.argv[0], "nfd_csv squid_csv \n", file=sys.stderr)
        exit(-1)
    return sys.argv[2]

def smooth(df):
    xnew = np.linspace(df['time(ms)'].min(), df['time(ms)'].max(), 1000)
    spl = make_interp_spline(df['time(ms)'], df['total(MB)'])
    ynew = spl(xnew)
    for i in range(len(ynew)):
        if ynew[i] <= 0:
            ynew[i] = 0
    return xnew, ynew

def mkplot():
    # figure and plot
    fig = plt.figure()
    fig.set_size_inches(5, 4)
    ax = fig.add_subplot(111)

    # read data
    df1 = pd.read_csv(get_nfd_result(), sep='\s+')
    df1['total(MB)'] = df1['total(B)'].str.replace(",", "").astype(int) / 1000000
    df1['time(ms)'] = df1['time(ms)'].str.replace(",", "").astype(int) / 1000
    df2 = pd.read_csv(get_squid_result(), sep='\s+')
    df2['total(MB)'] = df2['total(B)'].str.replace(",", "").astype(int) / 1000000
    df2['time(ms)'] = df2['time(ms)'].str.replace(",", "").astype(int) / 1000

    # plots
    # xnew, ynew = smooth(df2)
    # ax.plot(xnew, ynew, '--', label='Squid', color = '0.1')
    # xnew, ynew = smooth(df1)
    # ax.plot(xnew, ynew, '-', label='NFD', color = '0.4')

    ax.plot(df1['time(ms)'], df1['total(MB)'], '--', label='Squid', color = '0.1')
    ax.plot(df2['time(ms)'], df2['total(MB)'], '-', label='NFD', color = '0.4')

    ax.set_ylim([df1['total(MB)'].min(), df2['total(MB)'].max() + 2])
    ax.annotate('about 7x', xy = (37, 4))
    ax.arrow(35, 2, 0, 4, width=2, head_length = 1.5, length_includes_head=True)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Heap Use (MB)")
    plt.legend()
    plt.savefig('plot-memory.pdf')  

if __name__ == "__main__":
    mkplot()
