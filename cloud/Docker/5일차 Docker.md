## 5일차. 1) 스웜 모드 볼륨

지우고 시작!

```
vagrant@swarm-manager:~$ docker service rm $(docker service ls -q)
vagrant@swarm-manager:~$ docker container rm -f $(docker container ls -aq)
vagrant@swarm-manager:~$ docker volume rm myvol test 793623c3ddb17fb94aa52ae46524006f16020f73201d45beebb011e5cfbae3ce
myvol
```



도커 데몬 명령어 중 run 명령어에서 -v 옵션을 사용할 때는 1)호스트와 디렉토리를 공유하는 경우와 2)볼륨을 사용하는 경우에 대한 구분이 없음

**스웜 모드에서는 서비스를 생성할 때 도커 볼륨을 사용할지, 호스트와 디렉토리를 공유할지를 명확하게 명시**



1.1 **volume 타입의 볼륨 생성**

| --mount [옵션:type] | --mount 옵션의 type값에 volume을 지정 = 도커 볼륨을 사용하는 서비스를 생성 |
| ------------------- | ------------------------------------------------------------ |
| source              | 사용할 볼륨(도커 데몬에 해당 볼륨이 존재하면 해당 볼륨을 사용하고 없으면 새로 생성)<br />source 옵션을 명시하지 않으면 임의의 16진수로 구성된 익명의 이름을 가진 볼흄을 생성 |
| target              | 컨테이너 내부에 마운트될 디렉토리 위치                       |
| 리눅스 마운트       | 리눅스는 하드 드라이브, 시디롬, USB 등등 기타 외의 물리적인 장치 파일 시스템으로 인식되어야 사용 할 수 있습니다. 이러한 하드웨어 장치를 액세스 하기 위해서는 특정한 위치에 연결해 주어야 하는데 이러한 과정을 마운트라고 합니다<br />1) 형식<br />mount  -t  <파일 시스템 타입>  <장치 파일>  <마운트 포인트>     #장치를 마운트 시킬 때<br /><파일 시스템 타입>은 생략해도 됨.<br />리눅스에서 장치들은 파일로 생성되어져 있음. 예를 들어 시디롬은 /dev/ 디렉토리에 cdrom 이라는 파일로 존재하고 있음.<br />마운트 포인트는 마운트 할려고 하는 장치를 사용자가 지정하는 디렉토리에 연결하고자 하는 위치임.<br />[참고링크] https://opentutorials.org/course/528 |

서비스의 컨테이너에서 볼륨에 공유할 컨테이너의 디렉토리에 파일이 이미 존재하면 이 파일들은 볼륨에 복사되고, 호스트에서 별도의 공간을 차지하게 됨.

```
vagrant@swarm-manager:~$ docker service create --name ubuntu --mount type=volume,source=test,target=/etc/vim/,volume-nocopy ubuntu:14.04 ping docker.com
zelj7pbp20nqie4m83ze3821s
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged

vagrant@swarm-manager:~$ docker run -it --name test -v test:/root ubuntu:14.04
root@2c281c53763e:/# exit
exit
vagrant@swarm-manager:~$ mkdir ~/host
vagrant@swarm-manager:~$ ls
config.yml  host
vagrant@swarm-manager:~$ docker service rm ubuntu
ubuntu
vagrant@swarm-manager:~$ docker service create --name ubuntu --mount type=bind,src=/home/vagrant/host,dst=/root/container ubuntu:14.04 ping docker.com
ukdu1g7vjlae118k77n8gf667
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged
vagrant@swarm-manager:~$ ls ./host
vagrant@swarm-manager:~$ ls -al ./host
total 8
drwxrwxr-x 2 vagrant vagrant 4096 Sep 18 01:52 .
drwxr-xr-x 7 vagrant vagrant 4096 Sep 18 01:52 ..
vagrant@swarm-manager:~$ cd host
vagrant@swarm-manager:~/host$ touch hello
vagrant@swarm-manager:~/host$ docker service ps ubuntu
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
yjpvqfcmbxd0        ubuntu.1            ubuntu:14.04        swarm-manager       Running             Running 48 seconds ago
vagrant@swarm-manager:~/host$ docker container exec ubuntu.1.yjpvqfcmbxd0 /bin/bash
Error: No such container: ubuntu.1.yjpvqfcmbxd0
vagrant@swarm-manager:~/host$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
c0b534f38f1e        ubuntu:14.04        "ping docker.com"   About a minute ago   Up About a minute                       ubuntu.1.yjpvqfcmbxd0x80z62xau23y4
vagrant@swarm-manager:~/host$ docker container exec -it c0b534f38f1e /bin/bash
root@c0b534f38f1e:/# cd /root/container/
root@c0b534f38f1e:~/container# ls
hello
root@c0b534f38f1e:~/container# touch hello_in_container
root@c0b534f38f1e:~/container# ls
hello  hello_in_container
root@c0b534f38f1e:~/container# exit
exit
vagrant@swarm-manager:~/host$ ls
hello  hello_in_container
```







노드들의 상태를 바꿔줄 필요가 생김, 마스터 노드가 워커노드를 제어. 마스터 노드의 원래 기능에 충실하기 힘듦. 마스터 노드에 컨테이너 할당되지 않도록 한다. 이 노드에 컨테이너가 할당되지 않도록 함. docker node update -availability  노드의 상태를 변경 할 수 있음.



active is can allocate container

```
vagrant@swarm-manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
iujrapyvoqfyj9ylol90wdptp *   swarm-manager       Ready               Active              Leader              19.03.6
mld02rho3yix5ock2oxbnqazt     swarm-worker2       Ready               Active                                  19.03.6
xy3tnrvjq1xktzdrsoodld4f4     swarm-worker3       Ready               Active                                  19.03.6
```



스웜 매니저에게 노드를 할당하지 말라고 하는 것. drain 상태

```
# 노드의 상태를 확인
vagrant@swarm-manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
iujrapyvoqfyj9ylol90wdptp *   swarm-manager       Ready               Active              Leader              19.03.6
mld02rho3yix5ock2oxbnqazt     swarm-worker2       Ready               Active                                  19.03.6
xy3tnrvjq1xktzdrsoodld4f4     swarm-worker3       Ready               Active                                  19.03.6

# swarm-worker2 노드를 drain 상태로 변경
vagrant@swarm-manager:~$ docker node update --availability drain swarm-worker2
swarm-worker2

# swarm-worker2 노드가 drain 상태인 것을 확인
vagrant@swarm-manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
iujrapyvoqfyj9ylol90wdptp *   swarm-manager       Ready               Active              Leader              19.03.6
mld02rho3yix5ock2oxbnqazt     swarm-worker2       Ready               Drain                                   19.03.6
xy3tnrvjq1xktzdrsoodld4f4     swarm-worker3       Ready               Active                                  19.03.6

# nginx 서비스를 생성(5개의 컨테이너를 기동)
vagrant@swarm-manager:~$ docker service create --name nginx --replicas 5 nginx
98fnmtg2ht8930yf89gonon6c
overall progress: 5 out of 5 tasks
1/5: running   [==================================================>]
2/5: running   [==================================================>]
3/5: running   [==================================================>]
4/5: running   [==================================================>]
5/5: running   [==================================================>]
verify: Service converged

# 서비스 생성 여부 확인
vagrant@swarm-manager:~$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
98fnmtg2ht89        nginx               replicated          5/5                 nginx:latest
ukdu1g7vjlae        ubuntu              replicated          1/1                 ubuntu:14.04

# 서비스 실행 노드를 확인(swarm-worker2에는 할당되지 않음)
vagrant@swarm-manager:~$ docker service ps nginx
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR                              PORTS
lugmtadqkcz6        nginx.1             nginx:latest        swarm-worker3       Running             Running 29 seconds ago
6asgdfnovbds         \_ nginx.1         nginx:latest        swarm-worker3       Shutdown            Failed 34 seconds ago    "starting container failed: OC…"
nu3hijotclzs        nginx.2             nginx:latest        swarm-manager       Running             Running 37 seconds ago
r1zgx8ud0t3n        nginx.3             nginx:latest        swarm-worker3       Running             Running 34 seconds ago
xdso422pdnk3        nginx.4             nginx:latest        swarm-worker3       Running             Running 34 seconds ago
z9801sk0d9mu        nginx.5             nginx:latest        swarm-manager       Running             Running 37 seconds ago
```

드레인되면 다른 노드로 서비스 컨테이너 옮겨짐.

```
# swarm-worker2 노드를 active 상태로 전환
vagrant@swarm-manager:~$ docker node update --availability active swarm-worker2
swarm-worker2

# swarm-worker2 로드밸런싱되지 않음
vagrant@swarm-manager:~$ docker service ps nginx
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR                              PORTS
lugmtadqkcz6        nginx.1             nginx:latest        swarm-worker3       Running             Running 4 minutes ago
6asgdfnovbds         \_ nginx.1         nginx:latest        swarm-worker3       Shutdown            Failed 4 minutes ago    "starting container failed: OC…"
nu3hijotclzs        nginx.2             nginx:latest        swarm-manager       Running             Running 4 minutes ago
r1zgx8ud0t3n        nginx.3             nginx:latest        swarm-worker3       Running             Running 4 minutes ago
xdso422pdnk3        nginx.4             nginx:latest        swarm-worker3       Running             Running 4 minutes ago
z9801sk0d9mu        nginx.5             nginx:latest        swarm-manager       Running             Running 4 minutes ago

# scale down
vagrant@swarm-manager:~$ docker service scale nginx=1
nginx scaled to 1
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged

# 컨테이너 확인
vagrant@swarm-manager:~$ docker service ps nginx
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR                              PORTS
lugmtadqkcz6        nginx.1             nginx:latest        swarm-worker3       Running             Running 5 minutes ago
6asgdfnovbds         \_ nginx.1         nginx:latest        swarm-worker3       Shutdown            Failed 5 minutes ago    "starting container failed: OC…"

# scale up (로드밸런싱 된다.)
vagrant@swarm-manager:~$ docker service scale nginx=5
nginx scaled to 5
overall progress: 5 out of 5 tasks
1/5: running   [==================================================>]
2/5: running   [==================================================>]
3/5: running   [==================================================>]
4/5: running   [==================================================>]
5/5: running   [==================================================>]
verify: Service converged

# 활성화된 상태인 노드에 컨테이너가 골고루 배치되었는지 확인하기
vagrant@swarm-manager:~$ docker service ps nginx
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE               ERROR                              PORTS
lugmtadqkcz6        nginx.1             nginx:latest        swarm-worker3       Running             Running 6 minutes ago
6asgdfnovbds         \_ nginx.1         nginx:latest        swarm-worker3       Shutdown            Failed 6 minutes ago        "starting container failed: OC…"
yvkl6cfz4rq2        nginx.2             nginx:latest        swarm-worker3       Running             Running 33 seconds ago
oqiyhleoxju7        nginx.3             nginx:latest        swarm-manager       Running             Running 19 seconds ago
oyuu8vqyusxd         \_ nginx.3         nginx:latest        swarm-worker2       Shutdown            Failed 50 seconds ago       "starting container failed: OC…"
wwylmwylzri0         \_ nginx.3         nginx:latest        swarm-worker2       Shutdown            Failed 55 seconds ago       "starting container failed: OC…"
bl2bl4n3bkez         \_ nginx.3         nginx:latest        swarm-worker2       Shutdown            Failed about a minute ago   "starting container failed: OC…"
ili8uvq0ko2f        nginx.4             nginx:latest        swarm-worker3       Running             Running 16 seconds ago
upgfv3c29zw8         \_ nginx.4         nginx:latest        swarm-worker2       Shutdown            Failed 50 seconds ago       "starting container failed: OC…"
3kr06c2iw6rq         \_ nginx.4         nginx:latest        swarm-worker2       Shutdown            Failed 55 seconds ago       "starting container failed: OC…"
xzsojt66r04n         \_ nginx.4         nginx:latest        swarm-worker2       Shutdown            Failed about a minute ago   "starting container failed: OC…"
8rm24e4wgc0d        nginx.5             nginx:latest        swarm-manager       Running             Running 36 seconds ago
```

pause은 기존의 것은 유지되고 추가될 때, 나머지 노드에 추가된다. 



노드 라벨 추가

노드에 여러개의 라벨을 붙여놓는다. 노드들 마다 크로스되는 것이 있음. 내가 필요에 따라서 '하드디스크'만 쓰는 것만 조회, 노드를 조회, 관리하기 위해서 사용한다. 

이름=키(스토리지=스스디)

서비스 제약조건을 걸때 사용한다. 이 서비스가 아무런 제약을 주지 않으면 라운드로빈 방식으로 컨테이너를 생성, 특정 노드에만 이 서비스가 작동되면 좋겠다. 

consantrate