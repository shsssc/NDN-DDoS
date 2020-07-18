## Experiment arrangement

First we use `ab` to find the bottleneck speed of TLS. Then we adjust NDN client to that speed.

Thus, the sending frequency and total number of packets (the timeline) will be the same. While TLS is at maximum speed.

## log file format

The log file is in the following format:

```
timestamp pid command usertime(ticks) systime(ticks) vm_size(bytes) cached_page_size(pages)
```
