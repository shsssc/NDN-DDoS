#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import sys
import re

packet_len_re = re.compile(r'length (\w+):')


def get_nfd_filename() -> str:
    return sys.argv[1]


def get_squid_filename() -> str:
    return sys.argv[2]


def mkplot():
    # figure and plot
    fig = plt.figure()
    fig.set_size_inches(5, 4)
    ax = fig.add_subplot(111)

    # read data
    nfd_pkt_num_hit_values = []
    squid_pkt_num_hit_values = []
    nfd_traffic_hit_values = []
    squid_traffic_hit_values = []

    for i in range(1, 6):
        nfd_all_lines = None
        with open('results/cachehit/nfd-cpu-multiple/' + str(i) + '/packets.log') as f:
            nfd_all_lines = f.readlines()
        nfd_pkt_num_hit = 0
        nfd_traffic_hit = 0
        for line in nfd_all_lines:
            re = packet_len_re.search(line)
            if re:
                num = int(re.group(1))
                nfd_traffic_hit = nfd_traffic_hit + num
                nfd_pkt_num_hit += 1
        nfd_pkt_num_hit_values.append(nfd_pkt_num_hit)
        nfd_traffic_hit_values.append(nfd_traffic_hit)

        squid_all_lines = None
        with open('results/cachehit/squid-cpu-multiple/' + str(i) + '/packets.log') as f:
            squid_all_lines = f.readlines()
        squid_pkt_num_hit = 0
        squid_traffic_hit = 0
        for line in squid_all_lines:
            re = packet_len_re.search(line)
            if re:
                num = int(re.group(1))
                squid_traffic_hit = squid_traffic_hit + num
                squid_pkt_num_hit += 1
        squid_pkt_num_hit_values.append(squid_pkt_num_hit)
        squid_traffic_hit_values.append(squid_traffic_hit)

    nfd_pkt_num_hit_values = np.array(nfd_pkt_num_hit_values) / 9000
    squid_pkt_num_hit_values = np.array(squid_pkt_num_hit_values) / 9000
    nfd_traffic_hit_values = np.array(nfd_traffic_hit_values) / 9000
    squid_traffic_hit_values = np.array(squid_traffic_hit_values) / 9000

    labels = ['# of Packets', 'Amt. Traffic']
    squid_ys = [1, 1]
    nfd_ys = [nfd_pkt_num_hit_values.mean()/squid_pkt_num_hit_values.mean(), nfd_traffic_hit_values.mean()/squid_traffic_hit_values.mean()]
    squid_stds = [squid_pkt_num_hit_values.std()/squid_pkt_num_hit_values.mean(), squid_traffic_hit_values.std()/squid_traffic_hit_values.mean()]
    nfd_stds = [nfd_pkt_num_hit_values.std()/squid_pkt_num_hit_values.mean(), nfd_traffic_hit_values.std()/squid_traffic_hit_values.mean()]


    # plots
    x = np.arange(len(labels))
    width = 0.15
    rects1 = ax.bar(x - width/2, squid_ys, width, yerr=squid_stds, label='Squid')
    rects2 = ax.bar(x + width/2, nfd_ys, width, yerr=nfd_stds, label='NFD')

    ax.annotate('{:.2f}'.format(squid_pkt_num_hit_values.mean()),
                xy=(rects1[0].get_x() + rects1[0].get_width() / 2, rects1[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}KB'.format(squid_traffic_hit_values.mean()/1000),
                xy=(rects1[1].get_x() + rects1[1].get_width() / 2, rects1[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}'.format(nfd_pkt_num_hit_values.mean()),
                xy=(rects2[0].get_x() + rects2[0].get_width() / 2, rects2[0].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{:.2f}KB'.format(nfd_traffic_hit_values.mean()/1000),
                xy=(rects2[1].get_x() + rects2[1].get_width() / 2, rects2[1].get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

    ax.set_ylim(0, 1.1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    # plt.ylabel("")
    plt.legend()
    plt.title("Amount of Traffic (Avg. per request)")

    # annotate
    # ax.annotate('about 7x', xy = (37, 4))
    # ax.arrow(35, 2, 0, 4, width=2, head_length = 1.5, length_includes_head=True)

    plt.savefig('plot-traffic.pdf')


if __name__ == "__main__":
    mkplot()
