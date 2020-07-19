echo measuring CPU+packet

killall squid
rm -v /dev/shm/squid*.shm
rm -rf /usr/local/squid/var/run/squid.pid

sleep 3
timeout -s SIGINT 55 /usr/local/squid/sbin/squid -d1 -N &
sleep 4;
timeout 50 bash /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/tls-evaluation/measure-squid-performance.sh &
timeout 50 tcpdump -nei lo tcp port 443 > packets.log &
sleep 3;
#must manually start server

timeout 45 ab -n 90000 -c 6 https://127.0.0.1/static/static1 > ab_output&

sleep 53;


tar czvf packets.tar.gz packets.log
rm -rf packets.log
chmod 777 ./*
