## 함수 종류

**[콜백 함수 (callback function)]**

개발자가 명시적으로 코드를 통해 호출하는 함수가 아니고, 
개발자는 함수를 등록만 하고, 이벤트가 발생했을 때 또는 특정 시점에 도달했을 때 시스템에서 호출하는 함수

특정 함수의 인자로 넘겨서 코드 내부에서 호출되는 함수
예) 이벤트 핸들러



**[즉시 실행 함수 (immediate function)]**

함수를 정의함과 동시에 바로 실행하는 함수
최초 한번의 실행만을 필요로하는 초기화 구문에 사용
함수 리터럴을 괄호로 둘러싼 후 함수가 바로 호출될 수 있도록 괄호를 추가

```javascript
function add(x, y) {
    console.log(x + y);
}
add(3, 4);      //
 
(function add(x, y) {
    console.log(x + y);
})(3, 4);
 
(function (x, y) {
    console.log(x + y);
})(3, 4);
 
(function add(x, y) {
    console.log(x + y);
}(3, 4));
 
(function (x, y) {
    console.log(x + y);
}(3, 4));
```

```javascript
(function() {
    $(document).ready(function() {
        userController.init(configConstants);
    });
}());
```



[**함수를 반환하는 함수**]

```javascript
var self = function() {
    console.log('a');
 
    return function() {
        console.log('b');
    };
};
 
self();         // a
console.log('------------');
self = self();  // a
self();         // b
```



[**내부 함수 (inner function)**]

함수 내부에 정의된 함수

```javascript
function parent() {
    var a = 100;
    var b = 200;
 
    function child() {
        var b = 300;
 
        console.log(a);     // 100
        console.log(b);     // 300
    }
 
    child();
}
 
parent();
child();                    // child is not defined
```



부모 함수에서 내부 함수를 외부로 반환하면, 부모 함수 밖에서도 내부 함수를 호출이 가능

```javascript
function parent() {
    var a = 100;
    var b = 200;
 
    return function child() {
        var b = 300;
 
        console.log(a);     // 100
        console.log(b);     // 300
    };
}
 
var inner = parent();
inner();                    // 클로져(closure)              
                            // https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Closures
                            // 실행이 끝난 parent()와 같은 부모 함수 스코프의 변수를 참조하는 함수
```



[**arguments 객체**]

```javascript
function add(x, y) {
    console.dir(arguments);
    return x + y;
}
 
console.log(add(1, 2));     // 3
console.log(add(1, 2, 3));  // 3    인자 개수가 초과하면 -> 무시
console.log(add(1));        // NaN  인자 개수가 모자라면 -> undefined 값이 할당
```

함수가 호출될 때 파라미터(인자)와 함께 암묵적으로 **arguments 객체**가 함수 내부로 전달
함수를 호출할 때 넘긴 파라미터를 **배열 형태**로 저장한 객체                                          
실제 배열이 아닌 유사 배열 객체    

파라미터의 개수가 정확하게 정해지지 않은 함수를 구현할 때 또는 파라미터의 개수에 따라서 처리를 다르게 구현해야 하는 함수를 정의할 때 사용

```javascript
function sum() {
    var result = 0;
    for (var i = 0; i < arguments.length; i ++) {
        result += arguments[i];
    }
    return result;
}
 
console.log(sum(1));                // 1
console.log(sum(1, 2));             // 3
console.log(sum(1, 2, 3, 4, 5));    // 15
```



**[함수 호출 패턴과 this 바인딩]**

자바스크립트에서 함수를 호출하면 파라미터와 함께 arguments 객체와 this 인자가 함수 내부로 암묵적으로 전달함수가 호출되는 방식(호출 패턴)에 따라 this가 다른 객체를 참조



**객체의 메서드를 호출할 때 this 바인딩**
객체의 메서드 = 객체의 프로퍼티가 함수인 경우 ⇒ 해당 함수를 메서드라고 함
메서드 내부 코드에서 사용된 this ⇒ 해당 메서드를 **호출한 객체에 바인딩**

```javascript
var myObj = {
    name: 'crpark', 
    sayName: function() {
        console.log(this.name);
    }
};
 
var otherObj = {
    name: 'other'
};
 
otherObj.sayName = myObj.sayName;
 
myObj.sayName();        // crpark
otherObj.sayName();     // other
```



**함수를 호출할 때 this 바인딩**
함수 내부 코드에 사용된 this는 **전역 객체**에 바인딩				
브라우저 → windows 객체				
node.js → global 객체

```javascript
var text = "This is JavaScript";
console.log(text);          // This is JavaScript
console.log(window.text);   // This is JavaScript
console.dir(window);
 
var say = function() {
    console.log(this);      // Window {window: Window, self: Window, document: document, name: "", location: Location, …}
    console.log(this.text); // This is JavaScript
};
say();
```

![img](https://lh6.googleusercontent.com/7WtNMLVayy3Xiu2L8a679JL-JYLh1OO6D1gFQw4CCbu-6P5PtkKzpr97U33NlamFCrxFPgg-Z2yxWxoePz_xOTF0HrVhcZ-XHZMyVe787kkKsbPTgDeSBDxBYFj5DI5Z-hwmvw6l) 



내부 함수의 this도 전역 객체에 바인딩

```
var value = 100;
 
var myObject = {
    value: 1,
    func1: function() {
        this.value += 1;
        console.log(`func1() called. this.value = ${this.value}`);          // #1 → 2
 
        func2 = function() {
            this.value += 1;
            console.log(`func2() called. this.value = ${this.value}`);      // #2 → 101
 
            func3 = function() {
                this.value += 1;
                console.log(`func3() called. this.value = ${this.value}`);  // #3 → 102
            }
            func3();
        }
        func2();
    }
};
myObject.func1();
```

\#1 ⇒ myObject 객체의 메서드 코드에 포함된 this ⇒ 호출한 객체에 바인딩되므로 myObject.value 프로퍼티 값을 증가

#2, #3 ⇒ func1 함수 내부에 정의된 func2 함수와 func2 함수 내부에 정의된 func3 함수 내부 코드에서 사용하는 this ⇒ 글로벌 객체를 참조하므로 글로벌 변수로 정의(var value = 100;)된 값이 증가



#2와 #3에서 사용하는 this를 myObject를 참조하도록 하고 싶을 때는??? ⇒ 객체를 나타내는 this를 값을 가지는 변수 that (단순한 변수 이름)을 정의

```
var value = 100;
 
var myObject = {
    value: 1,
    func1: function() {
        var that = this;									// var _this = this;
        this.value += 1;    
        console.log(`func1() called. this.value = ${this.value}`);          // 2
 
        func2 = function() {
            that.value += 1;
            console.log(`func2() called. this.value = ${that.value}`);      // 3
 
            func3 = function() {
                that.value += 1;
                console.log(`func3() called. this.value = ${that.value}`);  // 4
            }
            func3();
        }
        func2();
    }
};
myObject.func1();
```



```
var x = true;

x == true	⇒ true
x == false 	⇒ false


var x;

x == true 	⇒ false
x == false	⇒ false

x = !x;		⇒ x == true

x == true	⇒ true
x == false	⇒ false

x = !!x;	⇒ x가 true이면 x는 true가 되고, x가 false이거나 undefine이면 x는 false가 됨
```



