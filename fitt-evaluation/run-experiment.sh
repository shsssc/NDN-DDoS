timeout 70 ./producer --prefix /example/App --static /static1 --static /static2 --static /static3 --dynamic /dynamic1 --dynamic /dynamic2 --dynamic /dynamic3 > producer\ output &
timeout 60 ./consumer --prefix /example/App --name /static1 --name /static2 --name /static3 --name /dynamic1 --name /dynamic2 --name /dynamic3 --period 100 > consumer\ output&
