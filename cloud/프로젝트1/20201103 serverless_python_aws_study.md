9:00-11:00 aws elasticsearch 공식 문서 예제 해보기
11:00-11:50 
13:00-17:50 python, serverless 
Amazon Elasticsearch Service에서 데이터 인덱싱
Elasticsearch REST API. Two APIs 존재: the index API and the _bulk API.
데이터를 검색하려면 먼저 색인을 생성 해야 합니다. 인덱싱은 검색 엔진이 빠른 검색을 위해 데이터를 구성하는 방법입니다. 결과 구조는 적절하게 인덱스라고 불립니다.
Elasticsearch에서 데이터의 기본 단위는 JSON 문서 입니다. 인덱스 내에서 Elasticsearch는 고유 ID를 사용하여 각 문서를 식별합니다 




[Amazon Elasticsearch Service에 대한 HTTP 요청 서명]
https://docs.aws.amazon.com/ko_kr/elasticsearch-service/latest/developerguide/es-request-signing.html
클라이언트 및 기타 일반 라이브러리를 사용하여, 서명된 HTTP 요청을 Amazon elasticsearch service에 보내는 방법.
_index, _bulk, _snapshot. 도메인 액세스 정책에 IAM 사용자 또는 역할이 포함되어 있는 경우??


 
1. 엘라스틱서치를 기본 백엔드로 사용하기 - 사람들이 블로그 글을 남기도록 하는 웹사이트를 가지고 있지만, 글을 검색하는 기능도 원한다고 하자. 엘라스틱서치를 사용하면 모든 글을 저장하고 질의도 제공할 수 있다.
 
전통적으로 검색엔진은 빠른 연관 검색 기능을 제공하기 위해서 안정된 데이터 저장소 위에 배포한다. 과거에는 검색엔진이 durable storage나 통계 같은 필요한 기능들을 제공하지 않았기 때문이다.
 
다른 NoSQL 저장소와 같이, 엘라스틱 서치는 트랜잭션을 지원하지 않는다. 그러나 트랜잭션이 필요하다면, "source of truth"로서 다른 데이터베이스를 사용하는 것도 고려할 수 있다. 정기적인 백업은 하나의 데이터 저장소를 사용할때 좋은 습관이다.
 
엘라스틱서치가 만능일 수는 없지만 전체 설계에 다른 저장소를 넣어서 복잡도를 증가시킬 가치가 있는지 저울질해봐야 한다. (천평?)


출처: https://12bme.tistory.com/471?category=682921 [길은 가면, 뒤에 있다.]




-------------------------------------------------------------------------------------------------------------------------------------
게이트웨이는 데이터를 디스크에 기록해서 노드가 내려가도 데이터를 잃지 않도록 하는 엘라스틱서치 컴포넌트이다. 노드를 시작했을때 게이트웨이는 데이터가 저장돼서 복구할 수 있는지 디스크를 살펴본다. 노드 이름에서 게이트웨이 세팅까지 로그에서 살펴본 대부분 정보는 설정 가능하다.

논리 배치 - 검색 애플리케이션이 무엇을 알아야 하는가.
색인과 검색을 위해 사용하는 구성 단위는 문서이고, 관계형 데이터베이스의 행과 같이 생각할 수 있다. 문서는 타입으로 나누고, 타입은 테이블이 행을 포함하는 것과 유사하게 문서를 포함한다. 하나 혹은 그 이상의 타입이 하나의 색인에 존재한다. 색인은 가장 큰 컨테이너이며 SQL계에서의 데이터베이스와 유사하다.
 
물리적 배치 - 엘라스틱서치가 뒷단에서 어떻게 데이터를 다루는가.
엘라스틱서치는 각각의 색인을 샤드로 나눈다. 샤드는 클러스터를 구성하는 서버 간에 이동할 수 있다. 보통 애플리케이션은 서버가 하나거나 그 이상이거나 같은 방식으로 엘라스틱서치와 동작하기 때문에 이것에 대해 상관하지 않는다. 그러나 클러스터를 관리할 때는 물리적으로 배치하는 방식이 성능/확장성/가용성을 결정하기 때문에 관심을 갖아야 한다.

엘라스틱서치에서 문서의 색인을 만들때 색인 안의 타입에 문서를 넣는다. get-together 색인은 두가지 타입을 포함한다. 이벤트/그룹/타입은 문서들을 포함하게 된다. 색인-타입-ID 조합은 엘라스틱서치에서 하나의 문서를 유일하게 식별한다. 검색할때 특정 색인의 특정 타입에서 문서를 찾거나 여러 타입 혹은 여러 색인에 걸쳐 검색할 수 있다.

문서
엘라스틱서치가 문서기반이라고 했는데, 이것은 색인과 검색하는 데이터의 가장 작은 단위가 문서라는 것을 의미한다. 엘라스틱서치에서 문서는 몇가지 중요한 특징을 가지고 있다.
독립적이다. 문서는 필드(name)와 값(Elasticsearch Denver)을 가지고 있다.
계층을 가질 수 있다. 문서 안의 문서로 생각하자. 필드의 값은 위치 필드의 값이 문자열인 것과 같이 단순형일 수 있다. 다른 필드와 값들을 포함할 수 있다. 예를 들어, 위치 필드는 도시/거리주소 등을 모두 포함할 수 있다.
유연한 구조로 되어있다. 문서는 미리 정의된 스키마에 의존하지 않는다.
엘라스틱서치에서 문서는 스키마가 없다고 말한다. 모든 문서가 같은 필드를 가질 필요가 없으므로, 같은 스키마일 필요가 없다는 뜻이다. 필드를 추가하거나 생략할 수 있긴 하지만, 각 필드의 타입은 중요하다. 그 때문에 엘라스틱서치는 모든 필드/타입 그리고 다른 설정에 대한 매핑을 보관하고 있다. 이 매핑은 색인의 타입마다 다르다. 그래서 때로는 엘라스틱서치 용어에서 타입이 매핑 타입으로 불리기도 한다.
 
타입
타입은 테이블이 행에 대한 컨테이너인 것과 같이 문서에 대한 논리적인 컨테이너다. 문서를 다른 타입의 다른 구조에 넣게 된다. 각 타입에서 필드의 정의는 매핑이라고 부른다. 각각의 필드는 서로 다르게 다룬다. 엘라스틱서치가 스키마가 없다면 왜 문서는 타입에 속해 있으며 각 타입은 스키마와 같은 매핑을 포함할까?
문서가 꼭 스키마가 필요하지 않기 때문에 Schema-free하다고 말한다. 매핑에 정의한 모든 필드를 포함할 필요는 없고, 새로운 필드를 생성할지도 모른다. 우선, 매핑은 타입에서 지금까지 색인한 모든 문서의 모든 필드를 포함한다. 하지만 모든 문서가 모든 필드를 가질 필요는 없다. 또한 새로운 문서가 매핑한 존재하지 않는 필드와 함께 색인하면, 엘라스틱서치는 자동으로 새로운 필드를 매핑에 추가한다. 필드를 추가하기 위해 타입이 무엇인지 추측한다.
매핑 타입은 문서를 논리적으로만 나눈다. 물리적으로 같은 색인의 문서는 속해 있는 매핑 타입에 관련 없이 디스크에 쓰인다.

색인(Index)
색인은 매핑 타입의 컨테이너다. 엘라스틱서치 인덱스는 관계형 데이터베이스와 같이 독립적인 문서 덩어리이다. 각각의 색인은 디스크에 같은 파일 집합으로 저장한다. 모든 매핑 타입의 모든 필드를 저장하고, 고유의 설정을 한다. 각 색인은 refresh_interval이라는 설정으로 새로 색인한 문서를 검색할수 있도록 하는 간격을 정의한다.
 
엘라스틱서치를 여러대의 서버에서 실행하고, 모든 서버에서 구동하는 같은 색인의 샤드들을 가질 수 있다.
 

출처: https://12bme.tistory.com/471?category=682921 [길은 가면, 뒤에 있다.]


서버리스 프레임 워크 및 Python을 사용하여 AWS DynamoDB 데이터를 AWS Elasticsearch에 인덱싱하는 방법


ijieun@ijieun-ui-MacBookPro wohousesa % curl -o- -L https://slss.io/install | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   178  100   178    0     0    154      0  0:00:01  0:00:01 --:--:--   154
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
100  3348  100  3348    0     0   1165      0  0:00:02  0:00:02 --:--:--  1165

 Installing Serverless!

 Downloading binary...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   644  100   644    0     0   1566      0 --:--:-- --:--:-- --:--:--  1566
100  122M  100  122M    0     0  2052k      0  0:01:01  0:01:01 --:--:-- 5604k

 Added the following to /Users/ijieun/.zshrc:

# Added by serverless binary installer
export PATH="$HOME/.serverless/bin:$PATH"

   ┌─────────────────────────────────────────────────────────────────────────────────────┐
   │                                                                                     │
   │   Serverless Framework successfully installed!                                      │
   │                                                                                     │
   │   To start your first project, please open another terminal and run “serverless”.   │
   │                                                                                     │
   │   You can uninstall at anytime by running “serverless uninstall”.                   │
   │                                                                                     │
   └─────────────────────────────────────────────────────────────────────────────────────┘

ijieun@ijieun-ui-MacBookPro wohousesa % serverless
zsh: command not found: serverless
ijieun@ijieun-ui-MacBookPro wohousesa % serverles                                 
zsh: command not found: serverles
ijieun@ijieun-ui-MacBookPro wohousesa % serverless
zsh: command not found: serverless
ijieun@ijieun-ui-MacBookPro wohousesa % export PATH="$HOME/.serverless/bin:$PATH"
ijieun@ijieun-ui-MacBookPro wohousesa % serverless

Serverless: No project detected. Do you want to create a new one? Yes
Serverless: What do you want to make? AWS Python
Serverless: What do you want to call this project? dynamodb-indexer

Project successfully created in 'dynamodb-indexer' folder.

You can monitor, troubleshoot, and test your new service with a free Serverless account.

Serverless: Would you like to enable this? No
You can run the “serverless” command again if you change your mind later.


No AWS credentials were found on your computer, you need these to host your application.

Serverless: Do you want to set them up now? Yes
Serverless: Do you have an AWS account? No

If your browser does not open automatically, please open the URL: https://portal.aws.amazon.com/billing/signup

Serverless: Press Enter to continue after creating an AWS account 

If your browser does not open automatically, please open the URL: https://console.aws.amazon.com/iam/home?region=us-east-1#/users$new?step=final&accessKey&userNames=serverless&permissionType=policies&policies=arn:aws:iam::aws:policy%2FAdministratorAccess

Serverless: Press Enter to continue after creating an AWS user with access keys 
Serverless: AWS Access Key Id: AKIA2CBNEADHSZB43U6V
Serverless: AWS Secret Access Key: ww2Xsavf7R6Pjzj1F6D5jzZ5wjXWNWpUyLp0QTcd

AWS credentials saved on your machine at ~/.aws/credentials. Go there to change them at any time.

Serverless: Would you like the Framework to update automatically? Yes

Auto updates were succesfully turned on.
You may turn off at any time with "serverless config --no-autoupdate"

Serverless: Would you like to setup a command line <tab> completion? Yes
Serverless: Which Shell do you use ? bash
Serverless: We will install completion to ~/.bashrc, is it ok ? Yes

Command line <tab> completion was successfully setup. Make sure to reload your SHELL.
You may uninstall it by running: serverless config tabcompletion uninstall

ijieun@ijieun-ui-MacBookPro wohousesa % curl -o- -L https://slss.io/install | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   178  100   178    0     0    154      0  0:00:01  0:00:01 --:--:--   154
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
100  3348  100  3348    0     0   1165      0  0:00:02  0:00:02 --:--:--  1165

 Installing Serverless!

 Downloading binary...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   644  100   644    0     0   1566      0 --:--:-- --:--:-- --:--:--  1566
100  122M  100  122M    0     0  2052k      0  0:01:01  0:01:01 --:--:-- 5604k

 Added the following to /Users/ijieun/.zshrc:

# Added by serverless binary installer
export PATH="$HOME/.serverless/bin:$PATH"

   ┌─────────────────────────────────────────────────────────────────────────────────────┐
   │                                                                                     │
   │   Serverless Framework successfully installed!                                      │
   │                                                                                     │
   │   To start your first project, please open another terminal and run “serverless”.   │
   │                                                                                     │
   │   You can uninstall at anytime by running “serverless uninstall”.                   │
   │                                                                                     │
   └─────────────────────────────────────────────────────────────────────────────────────┘

ijieun@ijieun-ui-MacBookPro wohousesa % serverless
zsh: command not found: serverless
ijieun@ijieun-ui-MacBookPro wohousesa % serverles                                 
zsh: command not found: serverles
ijieun@ijieun-ui-MacBookPro wohousesa % serverless
zsh: command not found: serverless
ijieun@ijieun-ui-MacBookPro wohousesa % export PATH="$HOME/.serverless/bin:$PATH"
ijieun@ijieun-ui-MacBookPro wohousesa % serverless

Serverless: No project detected. Do you want to create a new one? Yes
Serverless: What do you want to make? AWS Python
Serverless: What do you want to call this project? dynamodb-indexer

Project successfully created in 'dynamodb-indexer' folder.

You can monitor, troubleshoot, and test your new service with a free Serverless account.

Serverless: Would you like to enable this? No
You can run the “serverless” command again if you change your mind later.


No AWS credentials were found on your computer, you need these to host your application.

Serverless: Do you want to set them up now? Yes
Serverless: Do you have an AWS account? No

If your browser does not open automatically, please open the URL: https://portal.aws.amazon.com/billing/signup

Serverless: Press Enter to continue after creating an AWS account 

If your browser does not open automatically, please open the URL: https://console.aws.amazon.com/iam/home?region=us-east-1#/users$new?step=final&accessKey&userNames=serverless&permissionType=policies&policies=arn:aws:iam::aws:policy%2FAdministratorAccess

Serverless: Press Enter to continue after creating an AWS user with access keys 
Serverless: AWS Access Key Id: AKIA2CBNEADHSZB43U6V
Serverless: AWS Secret Access Key: ww2Xsavf7R6Pjzj1F6D5jzZ5wjXWNWpUyLp0QTcd

AWS credentials saved on your machine at ~/.aws/credentials. Go there to change them at any time.

Serverless: Would you like the Framework to update automatically? Yes

Auto updates were succesfully turned on.
You may turn off at any time with "serverless config --no-autoupdate"

Serverless: Would you like to setup a command line <tab> completion? Yes
Serverless: Which Shell do you use ? bash
Serverless: We will install completion to ~/.bashrc, is it ok ? Yes

Command line <tab> completion was successfully setup. Make sure to reload your SHELL.
You may uninstall it by running: serverless config tabcompletion uninstall

https://www.serverless.com/blog/serverless-python-packaging

ijieun@ijieun-ui-MacBookPro ~ % serverless create --template aws-python3 --name numpy-test --path numpy-test 
Serverless: Generating boilerplate...
Serverless: Generating boilerplate in "/Users/ijieun/numpy-test"
 _______                             __
|   _   .-----.----.--.--.-----.----|  .-----.-----.-----.
|   |___|  -__|   _|  |  |  -__|   _|  |  -__|__ --|__ --|
|____   |_____|__|  \___/|_____|__| |__|_____|_____|_____|
|   |   |             The Serverless Application Framework
|       |                           serverless.com, v2.9.0
 -------'

Serverless: Successfully generated boilerplate for template: "aws-python3"

