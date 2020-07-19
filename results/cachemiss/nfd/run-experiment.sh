echo measuring CPU+packet
sleep 1
timeout 60 /home/pikachu/ndn-cxx/NFD/build/bin/nfd &
sleep 4;
timeout 55 bash /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/measure-nfd-performance.sh &
timeout 55 tcpdump -nei lo tcp port 6363 > packets.log &
sleep 3;
timeout 45 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/producer --prefix /example/App --dynamic /dynamic1 --dynamic /dynamic2 --dynamic /dynamic3 --dynamic /dynamic4 --dynamic /dynamic5 --dynamic /dynamic6 > producer\ output &
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic1  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic2  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic3  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic4  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic5  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic6  --period 25642 > consumer\ output&
sleep 53;

echo ----------------
echo measuring memory
rm -rf ./massif*

sleep 1
timeout 70 /snap/bin/valgrind --tool=massif --time-unit=ms /home/pikachu/ndn-cxx/NFD/build/bin/nfd&
sleep 7;
timeout 45 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/producer --prefix /example/App --dynamic /dynamic1 --dynamic /dynamic2 --dynamic /dynamic3 --dynamic /dynamic4 --dynamic /dynamic5 --dynamic /dynamic6 > producer\ output &
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic1  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic2  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic3  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic4  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic5  --period 25642 > consumer\ output&
timeout 42.7 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /dynamic6  --period 25642 > consumer\ output&
sleep 66;
/home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performance/mem-log-convert.sh `ls ./massif*` > nfd_memory

chmod 777 ./*
