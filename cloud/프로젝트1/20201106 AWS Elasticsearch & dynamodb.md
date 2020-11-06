1. AWS Elasticsearch와 dynamodb를 사용한 사람의 리뷰 읽어보기

2. Elasticsearch에 대해서 개념 익히기

3. ###### Amazon DynamoDB에서 Amazon ES로 스트리밍 데이터 로드

   (전제)

   - DynamoDB 테이블 생성

     - aws cli 다운 [[링크]](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/install-cliv2-mac.html)

       ```
       ijieun@ijieun-ui-MacBookPro ~ % which aws
       /usr/local/bin/aws
       ijieun@ijieun-ui-MacBookPro ~ % aws --version
       aws-cli/2.0.62 Python/3.7.4 Darwin/19.6.0 exe/x86_64
       ```

     - dynamodb에 이미지 저장? [[링크]](https://www.quora.com/Can-DynamoDB-store-images)

       이미지를 데이터베이스에 보관하고 즉시 렌더링하려는 것은 개발자가 확장 측면에서 내릴 수있는 최악의 결정입니다.
       평균적으로 이미지 크기는 약 800kb입니다. 그리고 데이터베이스에서 이미지를 가져 오기 위해 네트워크 호출을하고 있습니다.
       전체 네트워크 대역폭을 차지하는 것과 같으며 웹 사이트가 대규모로 작동 할 때 많은 요청을 차단합니다.
       **Amazon S3 Bucket**의 모든 **정적 자산**을 유지하고 이미지에 액세스 할 수있는 URL을 가져온 다음 사용하는 데이터베이스에 URL을 저장하는 것입니다.
       이제 이미지를 렌더링 할 때가되면 CDN 링크를 제공하면 이미지를 저장하고 검색하는 데 최소 10 배 더 빠르고 가장 효율적인 방법이 될 것입니다.

     - primary key [[링크]](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey)

       - partition key :  파티션 키의 해시 값을 이용해 저장할 파티션을 결정하고, 기본 키를 파티션 키로 사용할 경우 2개 이상의 항목이 동일한 파티션 키 값을 가질 수 없다. 즉, RDBMS에서 primary key와 같은 역할을 한다.
       - sort key :  파티션 키와 정렬 키를 함께 기본 키로 이용한다. 여전히 저장할 파티션 공간은 파티션 키의 해시 값을 이용해 결정하지만, 같은 파티션 키라면 정렬 키 값을 기준으로 정렬되어 저장된다. 이 경우, 2개 이상의 항목이 동일한 파티션 키 값을 가질 수는 있지만, 정렬 키까지 같은 값을 가질 수 없다. 즉, RDBMS에서 파티션 키와 정렬 키를 합쳐 unique constraint를 걸어 놓은 것과 같다.

