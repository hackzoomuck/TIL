## **JavaScript 함수 정의**

**]JavaScript 함수 정의]**

함수 선언문 (function statement)

함수 표현식 (function expression) 

Function() 생성자 함수



**[함수 선언문 방식으로 함수를 생성]**

// 함수 선언
function add (x, y) { return x + y; }
키워드  이름 |  인자, 매개변수, 파라미터  | 함수 몸체  

// 함수 호출
console.log(add(3, 4));



**[함수 표현식 방식으로 함수를 생성** **⇒ 함수 리털러로 함수를 만들고, 생성된 함수를 변수에 할당]**

JavaScript에서는 함수도 하나의 값으로 취급

```var x = 1;			// x라는 변수에 1을 할당
var y = 2;			// y라는 변수에 2를 할당
var add = function(x, y) { 	// add라는 변수에 매개변수로 전달되는 두수를 더한 값을 반환하는 익명함수를 할당
	return x + y; 
};											   // ⇐ 함수 표현식 방식으로 함수를 생성할 때는 세미콜론을 넣어주는 것을 권장
var sum = add;			// 변수처럼 다른 변수에 재할당
console.log(add(3, 4));	// 7
console.log(sum(3, 4));	// 7
```



**[함수 표현식]** 

- 익명 함수 표현식
- 기명 함수 표현식 
  - 함수 표현식에서 사용된 함수 이름은 외부 코드에서 접근이 불가능
  - 함수 내부에서 해당 함수를 재귀적으로 호출할 때 또는 디버깅 할 때 사용

```
var add = function sum(x, y) { return x + y; };
 
console.log(add(3, 4));     // 7
console.log(sum(3, 4));     // sum is not defined
```

```
var myFactorial = function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n-1);
}
 
console.log(myFactorial(5));    // 120
console.log(factorial(5));      // factorial is not defined
```



함수 선언문으로 정의한 함수는 외부에서 호출이 가능하도록, 자바스크립트 엔진에 의해서 **함수 이름과 함수 변수 이름이 동일한 기명 함수 표현식**으로 변경

function add(x, y) { return x + y; }
							⇓
var add = function add(x, y) { return x + y; }



**[Function() 생성자 함수를 이용한 함수 생성]**

Function() 기본 내장 생성자 함수
https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function
함수 선언문, 함수 표현식 방식도 내부적으로는 Function() 생성자 함수를 이용해서 생성

new Function ([arg1[, arg2[, ...argN]],] functionBody)

```
var add = new Function('x', 'y', 'return x + y');
console.log(add(3, 4)); 
```



[**함수 호이스팅(function hosting)**] : (호이스팅)스코프가 위로 올라가는 것

함수 선언문 형태로 정의한 함수는 함수의 유효 범위가 코드의 맨 처음부터 시작 ⇒ 함수를 정의한 위치와 관계 없이 호출이 가능

```
console.log(add(1, 2));     // 3
 
function add(x, y) { 
    return x + y;
}
 
console.log(add(3, 4));     // 7
```

함수 호이스팅이 발생하는 원인(이유)
⇒ JavaScript의 변수 생성(instantiation)과 초기화(initialization) 작업이 분리되어 진행되기 때문



함수 표현식 방식과 함수 호이스팅 

```
console.log(x);             // undefine
var x = 2;
console.log(x);             // 2
 
console.log(y);             // y is not defined
 
var z;
console.log(z);             // undefined
 
console.log(add(1, 2));     // add is not a function
var add = function(x, y) { 
    return x + y;
}
console.log(add(3, 4));     // 7
```

