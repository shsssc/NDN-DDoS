#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import sys


def mk_plot():
    fig = plt.figure()
    fig.set_size_inches(9, 5)
    ax = fig.add_subplot(111)

    labels = ['CPU time/req\n@Static Req',
              'CPU time/req\n@Dynamic Req',
              'Heap Memory\n@Static Req',
              'Heap Memory\n@Dynamic Req',
              '# of pkts/req',
              'bandwidth/req',
              ]

    cpu_squid_ys = [1, 1]
    cpu_nfd_ys = [0.21550698315275257, 0.20947775628626691]
    cpu_squid_stds = [0.0006522742739025215, 0.0010936178491593852]
    cpu_nfd_stds = [0.00036280117331401326, 0.0004923413450036468]

    mem_squid_ys = [1, 1]
    mem_nfd_ys = [0.17083457016451023, 0.1577453368507184]
    mem_squid_stds = [0.0035203431862874473, 0.0076501974400536394]
    mem_nfd_stds = [0.002268233064034195, 0.0011884331239747491]

    traffic_squid_ys = [1, 1]
    traffic_nfd_ys = [0.09093976639862228, 0.35486579074282354]
    traffic_squid_stds = [6.055048414479985e-06, 1.2628279462242874e-05]
    traffic_nfd_stds = [0.00025784116166895733, 0.0010050724516748575]

    squid_ys = cpu_squid_ys + mem_squid_ys + traffic_squid_ys
    nfd_ys = cpu_nfd_ys + mem_nfd_ys + traffic_nfd_ys
    squid_stds = cpu_squid_stds + mem_squid_stds + traffic_squid_stds
    nfd_stds = cpu_nfd_stds + mem_nfd_stds + traffic_nfd_stds

    x = np.arange(len(labels))
    width = 0.3
    squid_rects = ax.bar(x - width/2, squid_ys, width=width, label='CDN (Squid, TLS Traffic)')
    ax.errorbar(x - width/2, squid_ys, yerr=squid_stds, elinewidth=3, ls='none', ecolor='0.0', capsize=2)
    nfd_rects = ax.bar(x + width/2, nfd_ys, width=width, label='NDN (NFD, NDN over IP)')
    ax.errorbar(x + width/2, nfd_ys, yerr=nfd_stds, elinewidth=3, ls='none', ecolor='0.0', capsize=2)

    counter = 0
    ax.annotate('{:.2f}ms'.format(0.35),
                xy=(squid_rects[counter].get_x() + squid_rects[counter].get_width() / 2, squid_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}ms'.format(0.08),
                xy=(nfd_rects[counter].get_x() + nfd_rects[counter].get_width() / 2, nfd_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    counter += 1
    ax.annotate('{:.2f}ms'.format(1.03),
                xy=(squid_rects[counter].get_x() + squid_rects[counter].get_width() / 2, squid_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}ms'.format(0.22),
                xy=(nfd_rects[counter].get_x() + nfd_rects[counter].get_width() / 2, nfd_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    counter += 1
    ax.annotate('{:.2f}MB'.format(6.66),
                xy=(squid_rects[counter].get_x() + squid_rects[counter].get_width() / 2, squid_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}MB'.format(1.14),
                xy=(nfd_rects[counter].get_x() + nfd_rects[counter].get_width() / 2, nfd_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    counter += 1
    ax.annotate('{:.2f}MB'.format(7.35),
                xy=(squid_rects[counter].get_x() + squid_rects[counter].get_width() / 2, squid_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}MB'.format(1.16),
                xy=(nfd_rects[counter].get_x() + nfd_rects[counter].get_width() / 2, nfd_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    counter += 1
    ax.annotate('{:.2f}'.format(200.01),
                xy=(squid_rects[counter].get_x() + squid_rects[counter].get_width() / 2, squid_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}'.format(18.19),
                xy=(nfd_rects[counter].get_x() + nfd_rects[counter].get_width() / 2, nfd_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    counter += 1
    ax.annotate('{:.2f}KB'.format(58.86),
                xy=(squid_rects[counter].get_x() + squid_rects[counter].get_width() / 2, squid_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}KB'.format(20.89),
                xy=(nfd_rects[counter].get_x() + nfd_rects[counter].get_width() / 2, nfd_rects[counter].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

    ax.set_ylim(0, 1.1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.legend(ncol=2, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
    plt.savefig('final.pdf')  
    plt.show()

if __name__ == "__main__":
    mk_plot()
