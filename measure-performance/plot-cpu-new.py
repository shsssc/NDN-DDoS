#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import sys

def mkplot():
    # figure and plot
    fig = plt.figure()
    fig.set_size_inches(5, 4) 
    ax = fig.add_subplot(111)


    squid_vals = [3276/90000, 1080/10000]
    nfd_vals = [737/90000, 152/10000]
    # read data: cachehit, cachemiss
    labels = ['Cache Hit', 'Cache Miss']
    squid_total_cpu = [1, 1] # 3276, 1080
    nfd_total_cpu = [nfd_vals[0]/squid_vals[0], nfd_vals[1]/squid_vals[1]]
    squid_data_std = [0, 0]
    nfd_data_std = [0, 0]

    # plots
    x = np.arange(len(labels))
    width = 0.15
    rects1 = ax.bar(x - width/2, squid_total_cpu, yerr=squid_data_std, width=width, label='Squid')
    rects2 = ax.bar(x + width/2, nfd_total_cpu, yerr=nfd_data_std, width=width, label='NFD')

    ax.annotate('{:.2f}ms'.format(squid_vals[0] * 10),
                xy=(rects1[0].get_x() + rects1[0].get_width() / 2, rects1[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}ms'.format(squid_vals[1] * 10),
                xy=(rects1[1].get_x() + rects1[1].get_width() / 2, rects1[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}ms'.format(nfd_vals[0] * 10),
                xy=(rects2[0].get_x() + rects2[0].get_width() / 2, rects2[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}ms'.format(nfd_vals[1] * 10),
                xy=(rects2[1].get_x() + rects2[1].get_width() / 2, rects2[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

    ax.set_ylim(0, 1.1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.legend()
    plt.title("CPU Use (Avg. CPU time ms/request)")

    plt.savefig('plot-cpu-bar.pdf')  

if __name__ == "__main__":
    mkplot()
