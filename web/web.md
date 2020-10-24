## web

web은 공유가 철학이다.

web에 있는 모든 리소스는 **교차**, **기원**, **자원요청**이 가능하다.



**[기원]**

origin = 기원 = ???
=>  스킴(프로토콜) + 호스트명 + 포트번호
http://www.example.com:8888/abc.html
http://www.sample.com:8080/xyz.html 	⇒ 기원이 다르다.

![img](https://lh3.googleusercontent.com/1i4VzX-e8iXYCTVElO9r_1QZW-UZUTYQUzv_S5JTg-xHgqhzwVmr6XIHs6PcoOkuWZuDRpysuS0cov_Wd6Ze99TPpIpUJvMvIj3UDNboDxrKvnkjCe8IJiEMXdayrPpfzCDSKN7H)



**[HTTP 요청은 기본적으로 교차 기원 요청이 가능]**

```
<html>
    <head></head>
    <body>
        <img src="https://s.pstatic.net/shopping.phinf/20201015_8/65c73d10-71c2-4c20-a416-ed94184f1456.jpg?type=f214_292" />
        <img src="tile.png" />
 
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script src="https://pm.pstatic.net/dist/lib/search.jindo.20200326.js?o=www"></script>
    </body>
</html>
```

⇒ 기원이 다른 js 파일과 이미지 파일이 서비스(스크립트 파일은 다운로드되어서 실행되고, 이미지 파일은 다운로드되어서 화면에 출력)

http://127.0.0.1:8000/
https://s.pstatic.net
//ajax.googleapis.com
https://pm.pstatic.net



**[스크립트 내에서의 교차 기원 요청은 보안 상의 이유로 제한 ⇒ ajax = XMLHttpRequest 객체를 이용한 비동기 통신]**

⇒ SOP(Same Origin Policy: 동일 기원 정책, 동일 출처 정책) : 가져온 것을 브라우저가 막는 것(메모리에 못 올라가도록 함)
⇒ XMLHttpRequest 객체을 사용해서 가져오는 리소스는 해당 웹 애플리케이션과 동일 기원으로 제한

```
<html>
    <head></head>
    <body>
        <img src="https://s.pstatic.net/shopping.phinf/20201015_8/65c73d10-71c2-4c20-a416-ed94184f1456.jpg?type=f214_292" />
        <img src="tile.png" />
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    
 
        <script>
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    console.log(xhttp.responseText);
                }
            };
            xhttp.open("GET", "https://pm.pstatic.net/dist/lib/search.jindo.20200326.js?o=www", true);
            xhttp.send();
        </script>
    </body>
</html>
```

 ![img](https://lh6.googleusercontent.com/CfIxj9-YEZBo4AKkIPfBSuPIUZvEoMODJ5JB74IfWE6TlnMKI5KEM6xr2vMWXHBOJYb6-HN4n_CFDUX38H7MlDlMG7R49GZXmUyXjjAM9Q8MA26I43zUHeOYvWQU8lNhg4L3526Q)



SOP로 보안을 강화하게 되면, api같은 서비스를 사용하는데 문제가 생김



**[CORS(Cross Origin Resource Sharing : 교차 기원 자원 공유)]**
=> SOP 완화 정책
=> 브라우저가 XMLHttpRequest로 교차 기원 원청이 가능하도록 해 주는 것
=> Access-Control-Allow-Orgin 응답 헤더를 이용해서 자원 사용 여부를 허가

![img](https://lh4.googleusercontent.com/-6DxxPmTCQrEZ_BqapZrbKAjkZEdB38S-UuiVoxdyIV6ifZhUZT91TU-CFwngGJfa3lT6Ay5hmmzgz1yX9QLs6eU69Y5ilmBobS_2eEOuA2Gcytzw7Ke2cZCm-vE2MBUt7VG0LaT)



다른 도메인(서버)에서 리소스를 가져와서 쓸 수 있음. (교차, 기원, 요청이 가능한 구조)
ajax통신으로 가져오는 데이터는 origin이 다르면 가져올 수는 있으나 쓸 수가 없음. 데이터는 가져오지만 메모리에 올릴 수가 없음.(SOP) =WEB2.0으로 messy up됨=> CORS(Access-Control-Allow-Orgin 응답 헤더)로 완화, api에서 가져올 때 우리 사이트의 정보를 등록하면 (Access-Control-Allow-Orgin 헤더에 등록됨)우리 사이트에 정보를 준다. 

access token

auth0로 인증을 수행함. auth0와 통신해서 우리 사이트를 등록하고, auth0는 키를 줌. access key로 auth0에 접근하면 내가 원하는 정보를 준다. (access key로 서비스를 이용한다.)

스토리지에 토큰을 저장

