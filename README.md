# oz_LiveSession


# flask
웹 서버 : 클라이언트의 요청에 따라 html, css, js와 같은 정적 파일을 응답하여 제공하는 소프트웨어    
        http 프로토콜을 사용하여 클라이 언트와 통신

was : 클라이언트의 요청에 대해 동적인 처리를 담당하는 영역, 웹서버와 다르게 로직을 처리

> 차이가 있지만 웹 서버로 통합해서 부르는 경우가 많음


venv(표준 가상환경 모듈)
python 표준 라이브러리에 포함되어 별도 설치 없이 사용 가능
가볍고 빠른 가상환경, 3.3 버전이상이면 사용 가능
```
myenv는 가상환경 이름 '.venv'가 예시에 많음
python -m venv myenv

source .venv/bin/activate
(Windows)myenv\Scripts\activate

deactivate
```

```
pip3 install flask
```

```
flask run
flask routes

lsof -i:5000
kill (쓰고있는 번호)
```

상태코드
200 : 성공
201 : 생성됨
400 : 잘못된 요청
401 : 인증 실패
404 : 찾을 수 없음
500 : 서버 오류
