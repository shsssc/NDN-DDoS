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

def smooth(df, attribute):
    xnew = np.linspace(df['time(s)'].min(), df['time(s)'].max(), 1000)
    df[attribute] = df[attribute].diff()
    df[attribute].at[0] = 0
    spl = make_interp_spline(df['time(s)'], df[attribute])
    ynew = spl(xnew)
    for i in range(len(ynew)):
        if ynew[i] <= 0:
            ynew[i] = 0
    return xnew, ynew

def mkplot():
    # figure and plot
    fig = plt.figure()
    fig.set_size_inches(4.8, 3.2)
    ax = fig.add_subplot(111)

    # read data
    header_list = ['time(s)', 'pid', 'command', 'usertime(ticks)', 'systime(ticks)', 'vm_size(bytes)', 'cached_page_size(pages)']
    df1 = pd.read_csv(get_nfd_result(), sep='\s+', names=header_list)
    df1['time(s)'] = df1['time(s)'] - df1['time(s)'][0]
    df2 = pd.read_csv(get_squid_result(), sep='\s+', names=header_list)
    df2['time(s)'] = df2['time(s)'] - df2['time(s)'][0]

    # plots
    xnew, ynew = smooth(df1, 'usertime(ticks)')
    ax.plot(xnew, ynew)
    xnew, ynew = smooth(df1, 'systime(ticks)')
    ax.plot(xnew, ynew)
    xnew, ynew = smooth(df2, 'usertime(ticks)')
    ax.plot(xnew, ynew)
    xnew, ynew = smooth(df2, 'systime(ticks)')
    ax.plot(xnew, ynew)
    plt.show()

if __name__ == "__main__":
    mkplot()
