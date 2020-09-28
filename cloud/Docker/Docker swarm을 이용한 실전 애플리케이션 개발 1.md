## Docker swarm을 이용한 실전 애플리케이션 개발 1

-----------

[요구조건]

- TODO를 등록, 수정, 삭제
- 등록된 TODO의 목록을 출력 
- 브라우저에서 사용할 수 있는 웹 애플리케이션
- 브라우저 외에서도 사용할 수 있도록 JSON API 엔드포인트를 제공 

[아키텍처] 

오케스트레이션 시스템 - 도커 스웜

[목적]

컨테이너 중심의 애플리케이션 개발에 대한 기초적인 기술을 습득

-----

#### [MySQL]  MySQL를 컨테이너로 실행

MySQL은 마스터-슬레이브 구조로 구성. INSERT, UPDATE, DELETE 쿼리는 마스터 DB, SELECT 쿼리는 슬레이브 DB로부터 읽어오게 역할을 분리함.

그리고 마스터 컨테이너에는 레플리카를 하나만 둔다.(마스터에 장애가 발생했을 때 슬레이브로 마스터를 대체하는 페일오버 기능은 사용하지 않음.)

[수행과정]

MySQL 컨테이너 여러 개를 마스터와 슬레이브로 묶는 과정 필요

- MySQL 컨테이너는 도커 허브에 등록된 mysql:5.7 이미즈를 기반으로 생성.
- 마스터-슬레이브 컨테이너는 두 역할을 모두 수행할 수 있는 하나의 이미지로 생성.
- 컨테이너에서 MYSQL_MASTER **환경변수의 값 유무**에 따라 마스터-슬레이브 동작을 결정.
- replicas 값을 조절해 슬레이브를 늘릴 수 있게 함. 이때 마스터, 슬레이브 모두 일시 정지를 허용.



유틸리티 설치

```
vagrant@swarm-manager:~$ sudo apt install -y tree
vagrant@swarm-manager:~$ sudo apt-get update
```



1. MySQL 이미지 생성을 위한 레퍼지토리 클론

   ```
   vagrant@swarm-manager:~$ git clone https://github.com/gihyodocker/tododb
   Cloning into 'tododb'...
   remote: Enumerating objects: 5, done.
   remote: Counting objects: 100% (5/5), done.
   remote: Compressing objects: 100% (4/4), done.
   remote: Total 38 (delta 0), reused 1 (delta 0), pack-reused 33
   Unpacking objects: 100% (38/38), done.
   ```

   ```
   vagrant@swarm-manager:~$ tree ./tododb
   ./tododb
   ├── Dockerfile
   ├── LICENSE
   ├── README.md
   ├── add-server-id.sh
   ├── etc
   │   └── mysql
   │       ├── conf.d
   │       │   └── mysql.cnf
   │       └── mysql.conf.d
   │           └── mysqld.cnf
   ├── init-data.sh
   ├── prepare.sh
   └── sql
       ├── 01_ddl.sql
       └── 02_dml.sql
   
   5 directories, 10 files
   ```

2. 데이터베이스 컨테이너 구성

   [도커 이미지 구성 내용]

   데이터 저장소 역할을 수행할 MySQL 서비스를 마스터-슬레이브 구조로 구축.

   마스터와 슬레이브 역할을 할 두 개의 MySQL 이 필요 => 별도의 Dockerfile 대신, 환경 변수 값으로 이미지 생성.

   







=> 컨테이너 여러 개로 구성된 데이터저장소를 구축하는 방법 공부!







서비스 포트가 중점 (인프라 관점), 라우팅 기준은 디렉토리, 디렉토리 패스가 / 에이피아이 _ 자기자신

포트 기준으로 어떻게 묶기는 지를 보기, 경로들을 보기 그거를 노드 코드

엔트리포인트는 런이랑 같음 엔트리포인트의 파라메터로 CMD 



[깨달은 점] 애플리케이션 실무에서는 스웜만으로 어련운 점이 있다는 것을 실감 -> 쿠버네티스로 해결 가능하다.

메소드에 따라서 겟하면 데이터 읽고 포스트하면 수정하고 풋하면 생성 딜리트 삭제하는 메소드를 가지고 서버사이드의 명령을 수행하는 기능을 한정함. 