timeout 45 ./producer --prefix /example/App --static /static1 --static /static2 --static /static3 --static /static4 --static /static5 --static /static6 > producer\ output &
timeout 39.1 ./consumer --prefix /example/App --name /static1  --period 2634 > consumer\ output&
timeout 39.1 ./consumer --prefix /example/App --name /static2  --period 2634 > consumer\ output&
timeout 39.1 ./consumer --prefix /example/App --name /static3  --period 2634 > consumer\ output&
timeout 39.1 ./consumer --prefix /example/App --name /static4  --period 2634 > consumer\ output&
timeout 39.1 ./consumer --prefix /example/App --name /static5  --period 2634 > consumer\ output&
timeout 39.1 ./consumer --prefix /example/App --name /static6  --period 2634 &
