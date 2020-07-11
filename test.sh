#!/bin/bash
timeout 10 ./producer --prefix /example/App --static /static1 --static /static2 --static /static3 --dynamic /dynamic1 --dynamic /dynamic2 --dynamic /dynamic3 > producer\ output &
timeout 10 ./consumer --prefix /example/App --name /static1 --name /static2 --name /static3 --name /dynamic1 --period 4 > consumer\ output&

