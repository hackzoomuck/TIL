<h3>git branch 한 것 clone하기</h3><br.

---

데스크탑에서 작업중이던 branch를 해당 branch에 push합니다.

이후 다른 작업 공간에서 사용하기 위해서는 다음과 같이 합니다.



1. master의 repo를 clone 합니다.

   ```
   git clone [원격 저장소 url]
   ```

   

2. branch 목록보기 합니다. (로컬 브랜치 목록보는 명령어)

   ``````
   git branch -a 
   ``````

   

3. 작업할 branch로 변경합니다.

   ``````
   git checkout [브랜치명]
   ``````

   



