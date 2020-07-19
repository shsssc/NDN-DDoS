#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import sys

def get_nfd_result_cachehit() -> str:
    return sys.argv[1]

def get_squid_result_cachehit() -> str:
    return sys.argv[2]

def get_nfd_result_cachemiss() -> str:
    return sys.argv[3]

def get_squid_result_cachemiss() -> str:
    return sys.argv[4]

def smooth(df):
    xnew = np.linspace(df['time(s)'].min(), df['time(s)'].max(), 1000)
    df['usertime(ticks)'] = df['usertime(ticks)'].diff()
    df['usertime(ticks)'].at[0] = 0
    df['systime(ticks)'] = df['systime(ticks)'].diff()
    df['systime(ticks)'].at[0] = 0
    df['cputime(ticks)'] = df['usertime(ticks)'] + df['systime(ticks)']
    spl = make_interp_spline(df['time(s)'], df['cputime(ticks)'])
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
    header_list = ['time(s)', 'pid', 'command', 'usertime(ticks)', 'systime(ticks)', 'vm_size(bytes)', 'cached_page_size(pages)']
    df1 = pd.read_csv(get_nfd_result_cachehit(), sep='\s+', names=header_list)
    df1['time(s)'] = df1['time(s)'] - df1['time(s)'][0]
    df2 = pd.read_csv(get_squid_result_cachehit(), sep='\s+', names=header_list)
    df2['time(s)'] = df2['time(s)'] - df2['time(s)'][0]
    df3 = pd.read_csv(get_nfd_result_cachemiss(), sep='\s+', names=header_list)
    df3['time(s)'] = df3['time(s)'] - df3['time(s)'][0]
    df4 = pd.read_csv(get_squid_result_cachemiss(), sep='\s+', names=header_list)
    df4['time(s)'] = df4['time(s)'] - df4['time(s)'][0]
    

    # plots
    xnew1, ynew1 = smooth(df2)
    xnew2, ynew2 = smooth(df4)
    ax.fill_between(xnew1, ynew1, ynew2)
    # ax.plot(xnew, ynew, '--', label='Squid', color='0.1')
    xnew, ynew = smooth(df1)
    ax.plot(xnew, ynew, '-', label='NFD', color='0.4')
    ax.set_ylim([df1['cputime(ticks)'].min(), df2['cputime(ticks)'].max() + 5])
    ax.set_xlim(0, 40)
    plt.xlabel("Time (seconds)")
    plt.ylabel("CPU Use (ticks)")
    plt.legend()

    # annotate
    # ax.annotate('about 5x', xy = (22, 8))
    # ax.arrow(20, 5, 0, 8, width=1, head_length = 3,length_includes_head=True)

    plt.savefig('plot-cpu-new-' + sys.argv[5] + '.pdf')  

if __name__ == "__main__":
    mkplot()