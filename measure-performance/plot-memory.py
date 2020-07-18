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
    df1 = pd.read_csv(get_nfd_result(), sep='\s+')
    df2 = pd.read_csv(get_squid_result(), sep='\s+')
    
    # plots
    ax.plot(df1['time(ms)'], df1['total(B)'], 'r-')
    ax.plot(df2['time(ms)'], df2['total(B)'], 'r-')
    plt.show()

if __name__ == "__main__":
    pass
