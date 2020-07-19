PID=`ps a |grep "\./squid"|grep -v "grep"|cut -d " " -f2`
bash /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performancee/genlog.sh "/home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performance/getperf.sh $PID" squid-measurement.log 0.5
