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

def mkplot():
    # figure and plot
    fig = plt.figure()
    fig.set_size_inches(4, 4)
    ax = fig.add_subplot(111)

    # read data
    df1 = pd.read_csv(get_nfd_result(), sep='\s+')
    df1['total(KB)'] = df1['total(B)'].str.replace(",", "").astype(int) / 1000
    df1['time(ms)'] = df1['time(ms)'].str.replace(",", "").astype(int)
    df2 = pd.read_csv(get_squid_result(), sep='\s+')
    df2['total(KB)'] = df2['total(B)'].str.replace(",", "").astype(int) / 1000
    df2['time(ms)'] = df2['time(ms)'].str.replace(",", "").astype(int)

    # plots
    ax.plot(df1['time(ms)'], df1['total(KB)'], '.-r', label='NFD', )
    ax.plot(df2['time(ms)'], df2['total(KB)'], '.--g', label='Squid')
    #ax.plot(df2['time(ms)'], df2['total(B)'], 'r-')
    plt.show()

if __name__ == "__main__":
    mkplot()
