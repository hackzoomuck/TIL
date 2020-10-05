[**Identity and Access Management (IAM)**]

AWS 사용자는 user들( AWS 계정과 AWS 안의 이용가능한 APIs/Servies )의 접근과 권한을 관리한다.



[**S3 Lifecycle Policy**]

데이터는 보통 제한된 시간 내에 useful하다. 그 기간에 데이터의 접근도 빈번하다. 사용을 안할때의 데이터는 아카이브 할 수 있고 아카이브 스토리지는 일반적으로 더 비용이 효율적이다.

AWS는 Glacier(긴 기간 아카이브 스토리지 서비스, 다른 스토리)

[**S3**]

- 버킷 속성에서 정적 웹 사이트 호스팅을 할 수 있음. 서버 기술이 필요 없는 정적 웹 사이트를 호스트 가능(Route 53이용가능)



[**Route 53**]

AWS에서 제공하는 DNS이다. 내가 사용하고자하는 도메인 검색해 가용한지 보고 사야한다. 

* 특이점 : AWS 내부 서비스로 연결해준다.

DNS : 도메인에 해당하는 IP 주소를 반환해주는 것. 



[**명령어 nslookup**]

명령어로 도메인을 볼 수 있다.

nslookup www.naver.com
서버:    dns.google
Address:  8.8.8.8

권한 없는 응답:
이름:    e6030.a.akamaiedge.net
Address:  23.46.23.18
Aliases:  www.naver.com
          www.naver.com.nheos.com
          www.naver.com.edgekey.net