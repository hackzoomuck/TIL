## AWS Secrets Manger

AWS CLI를 위한 사용자 생성을 해야 함. 
IAM에서 사용자 생성.



[프로그래밍 방식 액세스]

- 다른 코드를 통해서 접근
  - SDK가 필요
  - SDK : 인터페이스(API)를 바로 쓰는 것이 아니라 개별 사용하는 언어로 한 번 감싸둔 것 

- 프로그램을 통해서 쓸때
- 액세스 키, 비밀 액세스 키 필요



[Management Console]

- gui이면 비밀번호 필요



아무나 api 호출하면 안된다. (그렇기에 액세스 키, 비밀 액세스 키 필요)

p@$$w0rd

[SDK]

- API에 바로 붙어서 쓰는 것은 드물고, 

권한 - 정책을 편집

app.js

```
const express = require('express');
const app = express();

// Use this code snippet in your app.
// If you need more information about configurations or implementing the sample code, visit the AWS docs:
// https://aws.amazon.com/developers/getting-started/nodejs/

// Load the AWS SDK, 자바스크립트 변수를 선언
var AWS = require('aws-sdk'),
    endpoint = "https://secretsmanager.ap-northeast-2.amazonaws.com",
    region = "ap-northeast-2",
    secretName = "production/aws-exercise",  //비밀값 저장소, Secret Manger의 보안 암호 이름
    secret,
    binarySecretData;

// Create a Secrets Manager client, api이용해서 접근하려면 자격증명을 해야함. 
var client = new AWS.SecretsManager({
    endpoint: endpoint,
    region: region,
    accessKeyId: 'Access key ID', // 본인의 Access key ID를 입력
    secretAccessKey: 'Secret access key' // 본인의 Secret access key를 입력
});

app.get('/', (req, res) => {
  client.getSecretValue({ SecretId: secretName }, function (err, data) { //secretmanger와 연결된 client, 비동기 방식: 던져놓고, 답이오면 사용. callback함수. 익명함수.
    if (err) {
      if (err.code === 'ResourceNotFoundException')
        console.log("The requested secret " + secretName + " was not found");
      else if (err.code === 'InvalidRequestException')
        console.log("The request was invalid due to: " + err.message);
      else if (err.code === 'InvalidParameterException')
        console.log("The request had invalid params: " + err.message);
    }
    else {
      // Decrypted secret using the associated KMS CMK
      // Depending on whether the secret was a string or binary, one of these fields will be populated
      if (data.SecretString !== "") {
        secret = JSON.parse(data.SecretString);
      } else {
        binarySecretData = data.SecretBinary;
      }
    }
	//사용자에게 보여지는 응답을 보낸다. 
    res.send(`SecretsManager로 실행되는 AWS exercise의 A project입니다.<br />
- Admin 패스워드(admin_password): ${secret.admin_password}<br />
- 비밀 값(secret_key): ${secret.secret_key}`);
  });
});

app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});

app.get('/health', (req, res) => {
  res.status(200).send();
});
```

