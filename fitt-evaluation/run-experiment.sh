timeout 50 ./producer --prefix /example/App --dynamic /dynamic1 --dynamic /dynamic2 --dynamic /dynamic3 --dynamic /dynamic4 --dynamic /dynamic5 --dynamic /dynamic6 > producer\ output &
timeout 43 ./consumer --prefix /example/App --name /dynamic1 --name /dynamic2 --name /dynamic3  --name /dynamic4 --name /dynamic5 --name /dynamic6 --period 25646 > consumer\ output&
