#! /bin/bash

timeout 60 ./tls-load-gen.sh 10 https://localhost/cachable/static1&
timeout 60 ./tls-load-gen.sh 10 https://localhost/cachable/static2&
timeout 60 ./tls-load-gen.sh 10 https://localhost/cachable/static3&

timeout 60 ./tls-load-gen.sh 10 https://localhost/dynamic/dynamic1&
timeout 60 ./tls-load-gen.sh 10 https://localhost/dynamic/dynamic2&
timeout 60 ./tls-load-gen.sh 10 https://localhost/dynamic/dynamic3&


