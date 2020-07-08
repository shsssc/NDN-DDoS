default: attacker producer consumer
attacker: attacker.cpp
	g++ -o $@ attacker.cpp -lndn-cxx -lboost_system
consumer: consumer.cpp
	g++ -o $@ consumer.cpp -lndn-cxx -lboost_system
producer: producer.cpp
	g++ -o $@ producer.cpp -l ndn-cxx -lboost_system



