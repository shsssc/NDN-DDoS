We evaluate the computation and communication overhead of NDN forwarding daemon (NFD), an open-source NDN network forwarder, and Squid, one of the most widely used web proxy.
Specifically, we simulate today's practice of Maas and NDN/FITT's DDoS mitigation with the same hardware settings (i.e., Core i9 4.6GHZ, 32GB DDR4 RAM) and same number of clients requesting same amount of data and computation (6 clients asking for both static content and dynamically-computed content simulatiously).
We first measure the CPU and memory use of a single-thread Squid and NFD/FITT under the same load.
It shows NFD/FITT has a much less overhead than Squid: under the same load of traffic, Squid requires 3-7x memory and 5x CPU more than NFD/FITT.
We also measure the total amount of traffic at the IP layer involved in a single MaaS Squid server versus a single NDN/FITT node; it shows to fetch same amount of content and computation results, Squid over TLS requires around 10x more packets and 2.8x more bandwidth than NFD/FITT over overlaid NDN.
In practice, since MaaS service requires TLS-terminating traffic forwarding on both CDN server and MaaS server, the computation and communication overhead can be much larger than that in NDN/FITT case.