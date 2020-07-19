#! /bin/bash

PY=/usr/local/Cellar/python@3.8/3.8.3_2/bin/python3

$PY measure-performance/plot-cpu.py results/cachemiss/nfd/nfd-measurement.log results/cachemiss/squid/squid-measurement.log cachemiss
$PY measure-performance/plot-memory.py results/cachemiss/nfd/nfd_memory results/cachemiss/squid/squid_memory cachehit

$PY measure-performance/plot-cpu.py results/cachehit/nfd/nfd-measurement.log results/cachehit/squid/squid-measurement.log cachehit
$PY measure-performance/plot-memory.py results/cachehit/nfd/nfd_memory results/cachehit/squid/squid_memory cachehit