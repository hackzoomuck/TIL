## PROGRAMMERS - SQL 고득점 Kit [SUM, MAX, MIN]



- 최댓값 구하기

  ```
  SELECT MAX(DATETIME)
  FROM ANIMAL_INS
  ```

- 최솟값 구하기

- ```
  SELECT MIN(DATETIME)
  FROM ANIMAL_INS
  ```

- 동물 수 구하기
- ```
  SELECT COUNT(*) COUNT
  FROM ANIMAL_INS
  ```

- 중복 제거하기

  ```
  SELECT COUNT(DISTINCT NAME) name
  FROM ANIMAL_INS
  WHERE NAME IS NOT NULL
  ```

  