2020/11/10 일지

해야할 일

- python 과 dynamodb와 연동
- python -> lambda (serverless, venv)

9:00-11:00 venv 가상환경 공부
venv에 package, module 설치 

- preferences-> project:project_name->python interpreter
- python run 해봄
- [파이썬에서 디비에 저장하는 공식 문서 예제 링크](https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html)

14:00-16:00 boto3 [link](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

- 로컬 python project와 dynamodb 연동
  - boto3
  - aws configure 설정(iam)
- dynamodb에 data 업로드
- cloudsearch에 data 업로드

```
from pprint import pprint
import boto3

def put_data(product_code, category, product_detail_page_link, product_image_link, product_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('product_table')
    response = table.put_item(
        Item={
            'product_code': product_code,
            'category': category,
            'product_detail_page_link': product_detail_page_link,
            'product_image_link': product_image_link,
            'product_name': product_name
        }
    )
    return response

if __name__ == '__main__':
     # data_resp = put_data('SL-K703GX', 'printer',\
     #                      'https://www.samsung.com/sec/support/model/SL-K703GX/#downloads',\
     #                      'https://images.samsung.com/is/image/samsung/sec_SCX-3400-HYP_008_Front_gray%3F%24L1-Thumbnail%24',\
     #                      '삼성 흑백 레이저복합기\nSCX-3400/HYP\n(20ppm)\n')
     # print("Put search_data succeeded:")
     # pprint(data_resp, sort_dicts=False)
     crawl()
```


