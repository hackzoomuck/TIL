## SQL

[SELECT]

SELECT 열
FROM 테이블
WHERE 조건



[SUM, MAX, MIN]



[GROUP BY]

SELECT     	열
FROM 	   	테이블
WHERE 		조건
GROUP BY  그룹열
HAVING	   그룹조건



[IS NULL]

SELECT 열
FROM 테이블명
WHERE 열 IS NULL



[JOIN]

테이블 결합
SELECT 테이블1.열1, 테이블2.열2, 테이블2.열3 
FROM 테이블1
JOIN 테이블2 ON 조건(테이블1.열 = 테이블2.열);



[String, Date]