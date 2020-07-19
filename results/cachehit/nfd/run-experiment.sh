echo measuring CPU+packet
sleep 1
timeout 60 /home/pikachu/ndn-cxx/NFD/build/bin/nfd &
sleep 4;
timeout 55 bash /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/measure-nfd-performance.sh &
timeout 55 tcpdump -nei lo tcp port 6363 > packets.log &
sleep 3;
timeout 45 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/producer --prefix /example/App --static /static1 --static /static2 --static /static3 --static /static4 --static /static5 --static /static6 > producer\ output &
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static1  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static2  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static3  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static4  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static5  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static6  --period 2634 > consumer\ output&
sleep 53;

echo ----------------
echo measuring memory
rm -rf ./massif*

sleep 1
timeout 70 /snap/bin/valgrind --tool=massif --time-unit=ms /home/pikachu/ndn-cxx/NFD/build/bin/nfd&
sleep 7;
timeout 45 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/producer --prefix /example/App --static /static1 --static /static2 --static /static3 --static /static4 --static /static5 --static /static6 > producer\ output &
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static1  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static2  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static3  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static4  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static5  --period 2634 > consumer\ output&
timeout 39.1 /home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/fitt-evaluation/consumer --prefix /example/App --name /static6  --period 2634 > consumer\ output&
sleep 66;
/home/pikachu/ndn-cxx/gitrepos/NDN-DDoS/measure-performance/mem-log-convert.sh `ls ./massif*` > nfd_memory


