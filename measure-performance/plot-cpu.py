#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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
    fig.set_size_inches(4.8, 3.2)
    ax = fig.add_subplot(111)

    # read data
    header_list = ['time(ms)', 'pid', 'command', 'usertime(ticks)', 'systime(ticks)', 'vm_size(bytes)', 'cached_page_size(pages)']
    df1 = pd.read_csv(get_nfd_result(), sep='\s+', names=header_list)
    df2 = pd.read_csv(get_squid_result(), sep='\s+', names=header_list)

    # plots
    ax.plot(df1['time(ms)'], df1['usertime(ticks)'], 'r-')
    ax.plot(df1['time(ms)'], df1['systime(ticks)'], 'r-')
    ax.plot(df2['time(ms)'], df2['usertime(ticks)'], 'r-')
    ax.plot(df2['time(ms)'], df2['systime(ticks)'], 'r-')
    plt.show()

if __name__ == "__main__":
    pass
