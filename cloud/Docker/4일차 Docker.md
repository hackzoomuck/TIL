## 4일차. 도커 스웜 네트워크

1. **ingress 네트워크**

| ingress 네트워크 | ingress 네트워크는 어떤 swarm node에 접근하더라도 서비스 내의 컨테이너에 접근할 수 있게 설정하는 라우팅 메시를 구성하고, 서비스 내의 컨테이너에 대한 접근을 라운드 로빈 방식으로 분산하는 로드 밸런싱을 담당.<br />- swarm cluster를 생성하면 자동으로 등록되는 네트워크<br />- swarm mode를 사용할 때만 유효<br />- swarm cluster에 등록된 모든 노드에 ingress 네트워크가 생성 |
| ---------------- | ------------------------------------------------------------ |
| 라우팅 메시      | 어떤 컨테이너에 접근해도 가용 가능한 컨테이너로 연결해줌.    |
| 로드 밸런싱      | 컴퓨터 네트워크 기술의 일종으로 둘 혹은 셋이상의 중앙처리장치 혹은 저장장치와 같은 컴퓨터 자원들에게 작업을 나누는 것을 의미한다. 이로써 가용성 및 응답시간을 최적화 시킬 수 있다. |

1.1 매니저 노드에서 네트워크 목록 확인

```
root@swarm-manager:~# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
596ff6dbe31b        bridge              bridge              local
691fac8a6d2b        docker_gwbridge     bridge              local
a43c0696687a        host                host                local
j54w1tkw7rso        ingress             overlay             swarm
56855e8227c8        none                null                local
```

```
root@swarm-manager:~# docker network ls | grep ingress
j54w1tkw7rso        ingress             overlay             swarm

root@swarm-worker3:~# docker network ls | grep ingress
j54w1tkw7rso        ingress             overlay             swarm
```

1.2 웹 서버 이미지로 서비스 생성 후 각 노드 주소로 접근, 접속하는 노드에 존재하지 않은 컨테이너 이름도 출력됨.



2. **오버레이 네트워크**

| 오버레이 네트워크 | 오버레이 네트워크는 여러 개의 도커 데몬을 하나의 네트워크 풀로 만드는 네트워크 가상화 기술의 하나로,<br />도커에 오버레이 네트워크를 적용하면 여러 도커 데몬에 존재하는 컨테이너가 서로 통신할 수 있음.<br />여러 개의 swarm node에 할당된 컨테이너는 오버레이 네트워크의 서브넷에 해당하는 IP 대역을 할당받고 이 IP를 통해 서로 통신함. |
| ----------------- | ------------------------------------------------------------ |
| eth0              | ingress 네트워크와 연결된 NIC                                |
| NIC               | **네트워크 인터페이스 컨트롤러**(network interface controller, NIC)는 컴퓨터를 네트워크에 연결하여 통신하기 위해 사용하는 하드웨어 장치이다.<br />[OSI 계층](https://ko.wikipedia.org/wiki/OSI_모델) 1([물리 계층](https://ko.wikipedia.org/wiki/물리_계층))과 계층 2([데이터 링크 계층](https://ko.wikipedia.org/wiki/데이터_링크_계층)) 장치를 가지는데, [맥 주소](https://ko.wikipedia.org/wiki/맥_주소)를 사용하여 낮은 수준의 주소 할당 시스템을 제공하고 네트워크 매개체로 물리적인 접근을 가능하게 한다. 사용자들이 케이블을 연결하거나 무선으로 연결하여 네트워크에 접속할 수 있다. |
|                   | ingress 네트워크는 오버레이 네트워크 드라이버를 사용         |

2.1 스웜 클러스터 내의 컨테이너가 할당받은 IP 주소 확인

```
root@swarm-manager:~# docker ps --format "table {{.ID}}\T{{.Status}}\t{{.Image}}"
CONTAINER ID\TSTATUS       IMAGE
b6ec0acc290a\TUp 8 hours   alicek106/book:hostname
5dc91fe1f55d\TUp 8 hours   registry:2.6
26f7d360f9ed\TUp 9 hours   mysql:5.7
1135403c6c22\TUp 9 hours   nginx:latest
73297552cd29\TUp 9 hours   nginx:1.11
fd53a6d75ef8\TUp 9 hours   nginx:1.10
```

```
root@swarm-worker2:~# docker exec 00d339d771f8 ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:0a:00:00:15
          inet addr:10.0.0.21  Bcast:10.0.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1450  Metric:1
          RX packets:12 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:637 (637.0 B)  TX bytes:328 (328.0 B)

eth1      Link encap:Ethernet  HWaddr 02:42:ac:12:00:06
          inet addr:172.18.0.6  Bcast:172.18.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:39 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:3050 (3.0 KB)  TX bytes:372 (372.0 B)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:764 (764.0 B)  TX bytes:764 (764.0 B)
          
root@swarm-manager:~# docker exec b6ec0acc290a ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:0a:00:00:14
          inet addr:10.0.0.20  Bcast:10.0.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1450  Metric:1
          RX packets:17 errors:0 dropped:0 overruns:0 frame:0
          TX packets:9 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:1267 (1.2 KB)  TX bytes:952 (952.0 B)

eth1      Link encap:Ethernet  HWaddr 02:42:ac:12:00:06
          inet addr:172.18.0.6  Bcast:172.18.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:39 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:3034 (3.0 KB)  TX bytes:372 (372.0 B)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:764 (764.0 B)  TX bytes:764 (764.0 B) 
          
root@swarm-worker3:~# docker exec d08d4c834277 ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:0a:00:00:13
          inet addr:10.0.0.19  Bcast:10.0.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1450  Metric:1
          RX packets:12 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:637 (637.0 B)  TX bytes:328 (328.0 B)

eth1      Link encap:Ethernet  HWaddr 02:42:ac:12:00:06
          inet addr:172.18.0.6  Bcast:172.18.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:38 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:3008 (3.0 KB)  TX bytes:372 (372.0 B)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:764 (764.0 B)  TX bytes:764 (764.0 B)
```

2.2 포트 포워딩을 설정하지 않아도 컨테이너 간 전송이 가능

ingress network 가상네트워크로 묶여 있어서 쉽게 통신이 가능하다.

swarm-manager 노드의 컨테이너에서 swarm-worker3 노드의 컨테이너로 ping 전송 

```
root@swarm-manager:~# docker exec b6ec0acc290a ping -c 1 10.0.0.19
PING 10.0.0.19 (10.0.0.19) 56(84) bytes of data.
64 bytes from 10.0.0.19: icmp_seq=1 ttl=64 time=1.06 ms

--- 10.0.0.19 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.060/1.060/1.060/0.000 ms
```



3. **docker_gwbridge 네트워크**

   게이트웨이 역할.
   
   오버레이 네트워크를 사용하지 않는 컨테이너는 기본적으로 존재하는 브리지 네트워크를 사용해 외부와 연결함. 그러나, ingress를 포함한 모든 오버레이 네트워크는 브리지 네트워크와 다른 docker_gwbridge 네트워크와 함께 사용됨.

| docker_gwbridge 네트워크 | docker_gwbridge 네트워크는 외부로 나가는 통신 및 오버레이 네트워크의 트래픽 종단점(VTEP) 역할을 담당.<br />docker_gwbridge 네트워크는 컨테이너 내부의 네트워크 인터페이스 카드 중 ech1과 연결. |
| ------------------------ | ------------------------------------------------------------ |
| bridge                   | 브리지는 OSI모델의 데이타링크 계층 중 MAC계층에서 일을 수행하며, 두 세그먼트 사이에서 데이타링크 계층간의 패킷 전송을 담당하는 장치이다. 즉, 2개 이상의 독립된 세그먼트를 결합해서, 결과적으로 하나의 network인 것처럼 보이게 한다.<br />브리지는 들어오는 데이터 패킷을 분석하여 브리지가 주어진 패킷을 다른 세그먼트의 네트워크로 전송할 수 있는지를 결정할 수 있다. |
| network bridge           | 호스트 서버의 네트워크를 연결하여 가상화된 머신들도 동일한 네트워크를 사용하도록 하는 것. |



4. **사용자 정의 오버레이 네트워크**

4.1 사용자 정의 오버레이 네트워크 생성

```
root@swarm-manager:~# docker network create --subnet 10.0.9.0/24 -d overlay myoverlay
zad1tstahfdh6vbta48p1tozk
```

4.2 생성한 오버레이 네트워크 확인

```
root@swarm-manager:~# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
596ff6dbe31b        bridge              bridge              local
691fac8a6d2b        docker_gwbridge     bridge              local
a43c0696687a        host                host                local
j54w1tkw7rso        ingress             overlay             swarm
zad1tstahfdh        myoverlay           overlay             swarm <= swarm cluster만 사용
56855e8227c8        none                null                local
```

4.3 오버레이 네트워크를 서비스에 적용해 컨테이너 생성

```
root@swarm-manager:~# docker service create --name overlay_service --network myoverlay --replicas 2 alicek106/book:hostname
3rrm5ue467oo0vwyrl72igr4s
overall progress: 2 out of 2 tasks
1/2: running   [==================================================>]
2/2: running   [==================================================>]
verify: Service converged
```

4.4 생성된 컨테이너에 할당된 오버레이 네트워크 IP 주소 확인(eth0)

```
root@swarm-manager:~# docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE                     PORTS
kfqbonl6xeuj        hostname            replicated          4/4         alicek106/book:hostname   *:8000->80/tcp
56wpygmlng0u        mysql               replicated          1/1                 mysql:5.7
og7hvc6xjwjr        myweb               replicated          4/4                 nginx:latest              *:80->80/tcp
te7jiihqi865        myweb2              replicated          3/3                 nginx:1.11
ycs8dnp95bb5        myweb3              replicated          4/4                 nginx:1.10
3rrm5ue467oo        overlay_service     replicated          2/2                 alicek106/book:hostname
ieouk32sscna        web                 replicated          1/1                 nginx:latest
ginm8fpkocag        yml_registry        replicated          1/1                 registry:2.6              *:5000->5000/tcp

root@swarm-manager:~# docker service ps overlay_service
ID                  NAME                IMAGE                     NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
0n7trp8cwtll        overlay_service.1   alicek106/book:hostname   swarm-worker2       Running             Running 6 minutes ago
vsbz56mmb8y4        overlay_service.2   alicek106/book:hostname   swarm-manager       Running             Running 5 minutes ago

root@swarm-manager:~# docker ps | grep overlay_service.2.vsbz56mmb8y4
1171324db469        alicek106/book:hostname   "apachectl -DFOREGRO…"   6 minutes ago       Up 6 minutes        80/tcp                overlay_service.2.vsbz56mmb8y4ba0clcu990rcv

root@swarm-manager:~# docker exec overlay_service.2.vsbz56mmb8y4ba0clcu990rcv ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:0a:00:09:04
          inet addr:10.0.9.4  Bcast:10.0.9.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1450  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

eth1      Link encap:Ethernet  HWaddr 02:42:ac:12:00:05
          inet addr:172.18.0.5  Bcast:172.18.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:13 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:1006 (1.0 KB)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```



