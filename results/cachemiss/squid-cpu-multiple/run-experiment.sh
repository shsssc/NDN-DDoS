echo measuring CPU+packet
killall squid
rm -v /dev/shm/squid*.shm
rm -rf /usr/local/squid/var/run/squid.pid
sleep 3
timeout -s SIGINT 60 /usr/local/squid/sbin/squid -d1 -N &
sleep 4;
timeout 55 bash /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/tls-evaluation/measure-squid-performance.sh &
timeout 55 tcpdump -nei lo tcp port 443 > packets.log &
sleep 3;
#must manually start server

timeout 50 ab -n 10000 -c 6 https://127.0.0.1/dynamic/dynamic1 > ab_output&

sleep 53;

tar czvf packets.tar.gz packets.log
chmod 777 ./*
rm -rf packets.log
