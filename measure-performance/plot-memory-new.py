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
    header_list = ['n', 'time(ms)', 'total(B)', 'useful-heap(B)', 'extra-heap(B)', 'stacks(B)']
    df1 = pd.read_csv(get_nfd_result_cachehit(), sep='\s+', names=header_list)
    df1['total(MB)'] = df1['total(B)'].str.replace(",", "").astype(int) / 1000000
    df2 = pd.read_csv(get_squid_result_cachehit(), sep='\s+', names=header_list)
    df2['total(MB)'] = df2['total(B)'].str.replace(",", "").astype(int) / 1000000
    df3 = pd.read_csv(get_nfd_result_cachemiss(), sep='\s+', names=header_list)
    df3['total(MB)'] = df3['total(B)'].str.replace(",", "").astype(int) / 1000000
    df4 = pd.read_csv(get_squid_result_cachemiss(), sep='\s+', names=header_list)
    df4['total(MB)'] = df4['total(B)'].str.replace(",", "").astype(int) / 1000000

    labels = ["Cache Hit", "Cache Miss"]
    squid_data = [1, 1]
    squid_data_std = [df2['total(MB)'].std(), df4['total(MB)'].std()]
    nfd_data = [df1['total(MB)'].mean() / df2['total(MB)'].mean(), df3['total(MB)'].mean() / df4['total(MB)'].mean()]
    nfd_data_std = [df1['total(MB)'].std(), df3['total(MB)'].std()]

    # plots
    # error = np.random.normal(0.1, 0.02, df2.shape[0])
    # plt.fill_between(df2['time(ms)'], df2['total(MB)']-error, df2['total(MB)']+error)
    
    x = np.arange(len(labels))
    width = 0.15
    rects1 = ax.bar(x - width/2, squid_data, yerr=squid_data_std, width=width, label='Squid')
    rects2 = ax.bar(x + width/2, nfd_data, yerr=nfd_data_std, width=width, label='NFD')

    ax.annotate('{:.2f}MB'.format(df2['total(MB)'].mean()),
                xy=(rects1[0].get_x() + rects1[0].get_width() / 2, rects1[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}MB'.format(df4['total(MB)'].mean()),
                xy=(rects1[1].get_x() + rects1[1].get_width() / 2, rects1[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}MB'.format(df1['total(MB)'].mean()),
                xy=(rects2[0].get_x() + rects2[0].get_width() / 2, rects2[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}MB'.format(df3['total(MB)'].mean()),
                xy=(rects2[1].get_x() + rects2[1].get_width() / 2, rects2[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.legend()
    plt.title("Heap Memory Use")

    # annotate
    # ax.annotate('about 7x', xy = (37, 4))
    # ax.arrow(35, 2, 0, 4, width=2, head_length = 1.5, length_includes_head=True)

    plt.savefig('plot-memory-new' + sys.argv[5] + '.pdf')  

if __name__ == "__main__":
    mkplot()
