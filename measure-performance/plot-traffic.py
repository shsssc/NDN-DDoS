#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import sys
import re

packet_len_re = re.compile(r'length (\w+):')


def get_nfd_filename() -> str:
    if len(sys.argv) < 3:
        print(
            "Usage:", sys.argv[0], "nfd_csv squid_csv \n", file=sys.stderr)
        exit(-1)
    return sys.argv[1]


def get_squid_filename() -> str:
    if len(sys.argv) < 3:
        print(
            "Usage:", sys.argv[0], "nfd_csv squid_csv \n", file=sys.stderr)
        exit(-1)
    return sys.argv[2]


def mkplot():
    # figure and plot
    fig = plt.figure()
    fig.set_size_inches(5, 4)
    ax = fig.add_subplot(111)

    # read data
    nfd_all_lines = None
    squid_all_lines = None
    with open(get_nfd_filename()) as f:
        nfd_all_lines = f.readlines()
    with open(get_squid_filename()) as f:
        squid_all_lines = f.readlines()
    nfd_pkt_num = 0
    squid_pkt_num = 0
    nfd_traffic = 0
    squid_traffic = 0
    for line in nfd_all_lines:
        re = packet_len_re.search(line)
        if re:
            num = int(re.group(1))
            nfd_traffic = nfd_traffic + num
            nfd_pkt_num += 1
    for line in squid_all_lines:
        re = packet_len_re.search(line)
        if re:
            num = int(re.group(1))
            squid_traffic = squid_traffic + num
            squid_pkt_num += 1

    labels = ['# of Packets', 'Amount of Traffic']
    squid_ys = [1, 1]
    nfd_ys = [nfd_pkt_num/squid_pkt_num, nfd_traffic/squid_traffic]

    # plots
    x = np.arange(len(labels))
    width = 0.15
    rects1 = ax.bar(x - width/2, squid_ys, width, label='Squid')
    rects2 = ax.bar(x + width/2, nfd_ys, width, label='NFD')

    ax.annotate('{:.2f}K'.format(squid_pkt_num/1000),
                xy=(rects1[0].get_x() + rects1[0].get_width() / 2, rects1[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}MB'.format(squid_traffic/1000000),
                xy=(rects1[1].get_x() + rects1[1].get_width() / 2, rects1[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}K'.format(nfd_pkt_num/1000),
                xy=(rects2[0].get_x() + rects2[0].get_width() / 2, rects2[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}MB'.format(nfd_traffic/1000000),
                xy=(rects2[1].get_x() + rects2[1].get_width() / 2, rects2[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

    ax.set_ylim(0, 1.1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    # plt.ylabel("")
    plt.legend()
    plt.title("Amount of Traffic through Squid and NFD")

    # annotate
    # ax.annotate('about 7x', xy = (37, 4))
    # ax.arrow(35, 2, 0, 4, width=2, head_length = 1.5, length_includes_head=True)

    plt.savefig('plot-traffic.pdf')


if __name__ == "__main__":
    mkplot()
