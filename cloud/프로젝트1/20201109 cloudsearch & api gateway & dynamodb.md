2020/11/9 일지

9:00-9:20 회의
9:20-10:00 iam, dynamodb 생성
10:00-11:20 cloudsearch로 변경, 생성, dynamodb에 테스트 데이터 추가
[링크 - 콘솔에서 cloudsearch 사용 방법 ](http://wildpup.cafe24.com/archives/1085)

[링크 - cloudsearch vs elasticsearch](https://kyupokaws.wordpress.com/2017/07/27/cloudsearch-vs-elasticsearch/)

- CloudSearch는 웹페이지를 크롤링하고 데이터화하여 해당 데이터를 바탕으로 검색하는 방식은 아니고 DynamoDB나 S3에 저장된 CSV로 저장된 데이터를 사용한다.
- 운영과 도입이 편리하다!

13:00-14:00 api gateway 
[링크 - api gateway와 cloud search 연동](http://aaronkenny.com/blog/using-aws-api-gateway-to-enable-cors-for-cloud-search/index.htm)

Cloud search url로 비동기 통신 요청을 할 수 없다. 그렇기에 api gateway를 만들어준다. 

Api gateway와 cloudsearch 연동

1. get method 생성
   - integration type : http proxy
   - http method : GET
   - endpoint url : http://내 클라우드 서치 엔드포인트 url/**2013-01-01/search**

2. Query string parameters 활성화
   - 'q' query string variable
     1) method request : url querystring parameter 에 'q' 추가
     2) integration request : url querystring parameter에 'q' 추가
3. CORS 활성화
4. 배포



16:00 - 18:00 python selenium on aws lambda
[링크 - python selenium on aws lambda](https://medium.com/@manivannan_data/python-selenium-on-aws-lambda-b4b9de44b8e1)



16:00-16:30 위 링크 읽어보기, 프로젝트 아키텍처 구상
