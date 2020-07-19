PID=` ps a |grep nfd|grep bin/nfd|grep -v timeout|grep -v grep| sed -e 's/^[ \t]*//'|cut -d' ' -f1`
bash /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performance/genlog.sh "/home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performance/getperf.sh $PID" nfd-measurement.log 0.5
