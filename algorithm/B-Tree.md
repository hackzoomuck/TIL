### B-Tree

---

##### 소개 :

B-Tree는 self-balancing search tree입니다. 대부분의 다른 search trees(AVL, red-black tree)는 메인 메모리 안에 모든 것이 있다고 가정합니다.  B-Tree를 이해하려면, 메인 메모리에 fit할 수 없는 많은 데이터들에 대해서 생각해야 합니다. 

키의 수가 많으면, 데이터는 디스크에서 블록형태로 읽어집니다. 디스크 access time은 메인 메모리 access time에 비해 매우 높습니다.  B-Tree 사용 이유는 디스크 access수를 줄이는 것입니다.

대부분의 tree operations(search, insert, delete, max, min,...etc)는 트리의 높이가 h일때, O(h)의 디스크 access가 요구됩니다. B-tree는 뚱뚱한 트리입니다. B-Tree의 높이는 B-Tree 노드 안에 가능한 최대 키들을 넣어서 낮게 유지합니다. 일반적으로, B-Tree 노드 크기는 디스크 블록 크기와 같게 유지됩니다. B-Tree의 높이가 낮기 때문에 AVL트리, red-black tree 등과 같은 balanced Binary Search Trees에 비해 대부분의 작업에 대한 총 디스크 access가 크게 감소합니다. 



##### B-Tree 시간 복잡도

- n은 B-Tree의 elements의 총 개수

| operation | time complexity |
| --------- | --------------- |
| search    | O(log n)        |
| insert    | O(log n)        |
| delete    | O(log n)        |



##### B-Tree 속성

1. 모든 leaves은 같은 level에 있다.
2. B-Tree 

