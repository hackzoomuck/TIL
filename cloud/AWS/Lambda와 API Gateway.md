## AWS와 통합

출처 : AWS 기반 서버리스 아키텍처/위키북스

#### Lambda에서 JWT(Json Web Token) 다루는 법

Lambda 함수 호출 방법 : 2가지
1) aws sdk
2) api gateway를 경유



[API Gateway로 Lambda 함수 호출]

클라이언트(웹 사이트)가 API Gateway를 통해 Lambda 함수를 호출 

<img src="C:\Users\LEEJ\AppData\Roaming\Typora\typora-user-images\image-20201023110142499.png" alt="image-20201023110142499" style="zoom: 80%;" />



[Lambda 함수를 구현]

함수에 대한 새 IAM 역할 만들기.
Lambda 함수 생성.
컴퓨터에서 Lambda 함수 코드를 작성. 
Lambda함수 배포.



CloudWatch에 Lambda의 로그가 있음.

