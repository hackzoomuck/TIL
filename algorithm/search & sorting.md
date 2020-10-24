# search & sorting



### [search]

- https://github.com/gyoogle/tech-interview-for-developer/blob/master/Algorithm/Binary Search.md

#### 1. binary search

------

[내용]

탐색 범위를 이분할해서 찾는 방식

[전략]

- sorted data여야 함
- left, right, mid = (left+right)/2 값 설정
- mid 위치의 값과 구하려는 값 비교
- 구할 값 > arr[mid] 이면 left = mid+1, 구할 값 < arr[mid] right=mid-1
- left > right 될 때까지 반복

[코드]

```cpp
int binarySearch(int A[], int left, int right, int target){
      while(left <= right){
          int mid = (left + right) / 2;
          if(A[mid] == target) return mid;
          if(A[mid] > target) right = mid - 1;
          else left = mid + 1;
      }
      return -1;
 }
```

[시간복잡도]

전체 탐색 : O(N) 이분 탐색 : O(logN)



### [sorting]

- https://github.com/GimunLee/tech-refrigerator/blob/master/Algorithm/거품 정렬 (Bubble Sort).md#거품-정렬-bubble-sort
- https://github.com/GimunLee/tech-refrigerator/blob/master/Algorithm/선택 정렬 (Selection Sort).md#선택-정렬-selection-sort
- https://github.com/GimunLee/tech-refrigerator/blob/master/Algorithm/삽입 정렬 (Insertion Sort).md#삽입-정렬-insertion-sort
- https://github.com/gyoogle/tech-interview-for-developer/blob/master/Algorithm/HeapSort.md

------

![Untitled (1)](C:\Users\LEEJ\Downloads\Untitled (1).png)



#### 1. bubble sort

------

[내용]

두 인접한 원소를 비교하여 정렬하는 방법 거품이 수면으로 올라가는 모습과 비슷하기에 지어진 이름 Selection Sort와 유사함

[전략] n개의 원소

- 1회전 : index = 0(이하 숫자로만) 0과 1번 원소, 1과 2번 원소, 2와 3번 원소 ~ n-1(마지막)원소를 비교해서 조건이 맞지 않으면 서로 교환
- 2회전 : 맨 끝 원소는 조건에 맞는 (가장 큰, 가장 작은) 원소로 임, 그렇기에 정렬에서 제외하고 1회전과 동일한 과정을 반복한다. (회전이 증가할때마다 1개씩 정렬에서 제외된다.

[코드]

```cpp
for (i = 0; i < N; i++) {
 for (j = 0; j < N-(i+1); j++) {
	 if (data[j] > data[j+1]) {
	 // 자리교환
	 temp = data[j+1];
	 data[j+1] = data[j];
	 data[j] = temp;
	 }
	}
 }
```

[시간 복잡도] 1회전 : n-1 비교 2회전 : n-2 비교 n-1회전 : 1 비교

⇒ (n-1) + (n-2) + ... + 2+1 = n(n-1)/2 로, **O(n^2)**이다.

원소의 정렬과 무관하게 2개의 원소를 비교하기에 **최선, 평균, 최악** 모두 **O(n^2)**이다.

[공간 복잡도]

배열 내에서 교환이 이루어지기에 **O(n)**이다.

[장점]

- 구현 간단, 직관적
- 제자리 정렬(in-place sorting) 배열 내에서 교환방식으로 정렬이 이루어지기에 다른 메모리가 필요하지 않음
- 안정 정렬(stable stort)이다.

[단점]

- 시간복잡도가 O(n^2)로 비효율적임.
- unordered 원소는 정렬되기 위해 많은 교환연산이 일어남.



#### 2. selection sort

------

[내용] Bubble Sort과 유사한 알고리즘 ⇒ 해당 순서에 원소를 넣을 위치가 정해져 있음, 어떤 원소를 넣을지 선택하는 알고리즘

Insertion Sort와 헷갈릴 수 있음 ⇒ Selection Sort는 배열에서 해당 자리를 선택하고 그 자리에 오는 값을 찾는 것

[전략]

1. 주어진 배열 중에 최소값을 찾습니다.
2. 그 값을 맨 앞에 위치한 값과 교체합니다.
3. 배열을 같은 방법으로 교체합니다.

[코드]

```cpp
void selectionSort(int *list, const int n)
{
    int i, j, indexMin, temp;

    for (i = 0; i < n - 1; i++)
    {
        indexMin = i;
        for (j = i + 1; j < n; j++)
        {
            if (list[j] < list[indexMin])
            {
                indexMin = j;
            }
        }
        temp = list[indexMin];
        list[indexMin] = list[i];
        list[i] = temp;
    }
}
```

[시간복잡도] n개의 원소

1회전 : n-1 번 비교 2회전 : n-2 번 비교 n-1회전 : 1 번 비교

⇒ (n-1) + (n-2) + ... + 2+1 = n(n-1)/2 로, **O(n^2)**이다. 최선, 평균, 최악의 경우 시간복잡도는 O(n^2) 으로 동일함.

[공간복잡도]

배열 내에서 교환이 이루어지기에 **O(n)**이다.

[장점]

- 알고리즘 단순
- 정렬을 위한 비교 횟수는 많지만, Bubble Sort에 비해 실제로 교환하는 횟수는 적음 ⇒ 많은 교환이 일어나야 하는 자료상태에서 비교적 효율적.
- 제자리 정렬(in-place sorting) : Bubble Sort와 마찬가지로 다른 메모리 공간을 필요로 하지 않음.

[단점]

- 시간복잡도 O(n^2)로 비효율
- 불안정 정렬(Unstable Sort)임.



#### 3. Insertion Sort

------

[내용]

손 안의 카드를 정렬하는 방법과 유사 Selection Sort와 유사하지만, 좀 더 효율적인 정렬 알고리즘입니다 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘.

loop invarient(loop가 시작되는 위치에서 항상 만족하는 어떤 성질) : i단계에서 index i를 처리 할 것이고, 이 앞의 i개의 element가 있고 오름차순으로 정렬되어있다.

[전략]

- index 0은 그 자리에 저장
- tmp = index가 1인 값
- tmp와 이전 원소들을 비교하며 정렬
- 2번으로 돌아가 다음 위치(index)의 값을 tmp에 저장하고, 반복

[코드]

```cpp
void InsertionSort(int * arr){
    int i, j;
    int key;
 
    for(i=1; i< MAX_LEN; i++){
        key = arr[i];
        
        for(j=i-1; j>=0; j--){
        
            if(arr[j] > key){       
                arr[j+1] = arr[j];  
            }else{                  
                break;
            }
        
        }
        
        arr[j+1] = key;             
    }
}
```

[시간복잡도]

최악의 경우(역으로 정렬) Selection Sort와 같이, (n-1)+(n-2)+...+2+1 = n(n-1) ⇒ **O(n^2)** 최선의 경우(다 정렬) 1번씩 비교 ⇒ **O(n)**

평균 : ⇒ **O(n^2)**

![Untitled (2)](C:\Users\LEEJ\Downloads\Untitled (2).png)

![Untitled (3)](C:\Users\LEEJ\Downloads\Untitled (3).png)

[공간복잡도]

배열 내에서 교환이 이루어지기에 **O(n)**이다.

[장점]

- 알고리즘 단순
- 대부분의 원소가 이미 정렬되어 있는 경우, 매우 효율적
- 제자리 정렬(in-place sorting)
- 안정 정렬(stable sort)
- Selection Sort나 Bubble Sort과 같은 O(n^2) 알고리즘에 비교하여 상대적으로 빠릅니다.

[단점]

- 평균과 최악의 시간복잡도가 O(n^2)으로 비효율적입니다.
- Bubble Sort와 Selection Sort와 마찬가지로, 배열의 길이가 길어질수록 비효율적입니다.

[결론]

Selection Sort와 Insertion Sort는 k번째 반복 이후, 첫번째 k 요소가 정렬된 순서로 온다는 점에서 유사합니다. 하지만, Selection Sort는 k+1번째 요소를 찾기 위해 나머지 모든 요소들을 탐색하지만 Insertion Sort는 k+1번째 요소를 배치하는 데 필요한 만큼의 요소만 탐색하기 때문에 훨씬 효율적으로 실행된다는 차이가 있습니다.



#### 4. Heapsort

------

[내용]

maxheap, minheap tree를 구성해 정렬하는 방법, 내림차순 정렬: 최대 힙, 오름차순 정렬:최소 힙

- heap structure : 

  complete binary tree

  -binary tree T는 다음 조건을 만족하면 heap structure이다(h=트리 높이)

  - T는 적어도 h-1까지 complete하다. (fully binary tree)
  - 모든 leaves는 깊이가 h-1 또는 h이다.
  - 깊이 h의 리프에 대한 모든 경로는 깊이 h-1의 리프에 대한 모든 경로의 왼쪽에 있습니다.
  - 삽입할 때 왼쪽부터 차례대로 추가하는 이진 트리

- Partial order tree property : 부모, 자식

- maxheap : 부모로 갈수록 키값이 커진다. 최대값이 root에, 최소는 leaf 중에 있음

- minheap : 부모로 갈수록 키값이 작아진다. 최소값이 root에, 최대는 leaf 중에 있음

[전략]

maxheap을 기준으로 설명하겠습니다.

- 만일 정렬된 요소들이 힙안에 배열된다면,

1. 루트에서 요소를 반복적으로 제거하여 역순으로 정렬 된 시퀀스를 만들 수 있습니다.
2. 나머지 요소를 재정렬하여 부분 순서 트리 속성을 다시 설정하는 등

- heapSort(E, n)

```c
1. n개의 정렬된 집합 E에서 H 구성하기 (heap 만들기) => O(n)
2. for(i=n;i>=1;i--){
		curMax = getMax(H); 
		deleteMax(H);
		E[i] = curMax;
}
```

- deleteMax(H)

```c
1. H의 가장 낮은 level의 가장 오른쪽 요소를 K에 복사.
2. H의 가장 낮은 level의 가장 오른쪽 요소를 삭제.
3. fixHeap(H,K);
```

- fixHeap(H,K)

```c
if(H is a leaf){
		insert K in root(H);
}
else{
	1. leftsubtree 또는 rightsubtree 중 root에 더 큰 키가 있는 것을 largerSubHeap로 설정한다.
	if(K.key >= root(largerSubHeap.key){
			insert K in root(H);
	}
	else{
			insert root(largerSubHeap) in root(H);
			fixHeap(largerSubHeap, K);
	} 
}
return;
```

[코드]

[시간복잡도]

fixHeap은 최악의 경우 힙의 높이가 h일때, 2h비교가 요구된다. W(n) =~ 2log(n) : 1. 서브힙의 루트끼리 비교하고 2. 그 값과 부모와 비교

- 모든 deletions을 다하면,

<img src="C:\Users\LEEJ\Downloads\_2020-10-22__7.34.59.png" alt="_2020-10-22__7.34.59" style="zoom: 50%;" />

- 정리 : 최악의 경우 힙소트가 수행한 키 비교수는 2nlog(n) + O(n)

⇒ **O(nlog(n))**이다.

[공간복잡도]

O(n)

[장점]

- 가장 크거나 가장 작은 값을 구할 때
- 최대 k만큼 떨어진 요소들을 정렬할 때

[단점]

- 퀵정렬과 합병정렬의 성능이 좋기 때문에 힙 정렬의 사용빈도가 높지는 않음.
- 불안정 정렬