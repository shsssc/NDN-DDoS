#! /bin/bash

python3 measure-performance/plot-memory.py results/6_concurrent_4.2ms_space_10000_req/nfd_memory results/6_concurrent_4.2ms_space_10000_req/squid_memory
python3 measure-performance/plot-cpu.py results/6_concurrent_4.2ms_space_10000_req/nfd-measurement.log results/6_concurrent_4.2ms_space_10000_req/squid-measurement.log