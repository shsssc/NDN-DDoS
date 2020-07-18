#!/bin/bash
#convert valgrind log to a table and print to stdout
ms_print $1 |grep 0 |grep -v "|"|grep -v "\->"|grep -v "\."
