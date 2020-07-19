PID=`ps a |grep squid|grep sbin/squid|grep -v timeout|grep -v grep| sed -e 's/^[ \t]*//'|cut -d' ' -f1`
bash /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performance/genlog.sh "/home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performance/getperf.sh $PID" squid-measurement.log 0.5
