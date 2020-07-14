#!/bin/bash
## 1: pid
## 2: command
## 14:user time in 100hz ticks
## 15 sys time in 100hz ticks
## 23: virtual memory size
## 24: rss in page count
# printf "time pid name user_time sys_time vms rss\n"
cat /proc/$1/stat |cut -d" " -f1,2,14,15,23,24 |ts "%.s"
