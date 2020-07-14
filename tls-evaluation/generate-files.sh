#! /bin/bash

mkdir -p static
mkdir -p dynamic
head -c 2kB /dev/urandom > static/static1
head -c 2kB /dev/urandom > static/static2
head -c 2kB /dev/urandom > static/static3
head -c 1kB /dev/urandom > dynamic/dynamic1
head -c 1kB /dev/urandom > dynamic/dynamic2
head -c 1kB /dev/urandom > dynamic/dynamic3
