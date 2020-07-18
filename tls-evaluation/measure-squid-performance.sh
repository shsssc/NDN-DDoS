t=$1
PID=`ps a |grep "\./squid"|grep -v "grep"|cut -d " " -f2`
timeout $t bash ../measure-performance/genlog.sh "../measure-performance/getperf.sh $PID" squid-measurement.log 0.5
