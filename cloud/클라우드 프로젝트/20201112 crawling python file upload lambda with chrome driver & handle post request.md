2020/11/12 프로젝트 일지

해야할 일

- crawling python file upload lambda with chrome driver

9:15-10:35
[크롤링 파이썬 람다에 올리기 링크](http://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python/)
 람다 생성하려다가 vpc를 만들어서 사용해볼까 알아보는 중. -> 일단 람다에 얹어보고 나중에 해봐야겠다.

```
IPv4 CIDR 블록
VPC에 대한 IPv4 주소 범위를 지정해야 합니다. IPv4 주소 범위를 CIDR(Classless Inter-Domain Routing) 블록으로 지정합니다(예: 10.0.0.0/16). CIDR 블록 크기는 /16 ~ /28 넷마스크여야 합니다.
```

10:35-12:00

```
Selenium 스크레이퍼는 Chrome 브라우저를 포함해야하기 때문에 큽니다. 따라서“Upload file form Amazon S3”를 선택합니다. 
```

```
환경 변수를 설정해야합니다. Chrome 브라우저를 업로드 할 예정이므로 Lambda에 위치를 알려야합니다. 따라서 이러한 키와 값을 입력하십시오.

PATH = /var/task/bin
PYTHONPATH = /var/task/src:/var/task/lib
```

```
이 함수에 가장 기본적인 Lambda 권한을 부여한 것을 기억하십니까? 내 스크립트가 S3에 데이터를 쓰도록하려면이를 수행 할 수있는 권한을 부여해야합니다. 여기에서 역할이 시작됩니다. 그리고 Amazon의 ID 및 액세스 관리 시스템 인 IAM에서 역할을 구성해야합니다.
```



14:30-17:20
\1. 경로 custom - api gateway에 리소스 custom 생성
\2. 메소드 post - 생성, lambda(postcrawl)
\3. 헤더 Authorization, 람다함수에서 처리하려했으나 event['authorization'] 읽히지 않음, api gateway에서 처리하기로 함. 
\4. 테이블 생성
\5. 200 : 요청은 정상이었으나, 테이블 생성 x
  201: 요청 정상, 테이블 생성도 일어남
  400: 유저 아이디가 요청에 없음
  403: 토큰 이상

-H 'Authorization: Bearer token' -d "userId=string"

- 유저아이디/헤더 검증해서 토큰있는 사용자들 요청만 처리하기
