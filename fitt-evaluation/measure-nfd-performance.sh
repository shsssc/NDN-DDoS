PID=`ps a|grep nfd|grep -v grep |cut -d" " -f1`
bash ../measure-performance/genlog.sh "../measure-performance/getperf.sh $PID" nfd-measurement.log 0.5
