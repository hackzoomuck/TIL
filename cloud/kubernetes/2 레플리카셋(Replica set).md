minikube - 쿠버네티스에서 클러스터

minikube start

쿠8 가장 작은 단위 포드, 포드는 1개이상의 컨테이너로 구성되어있는 컨테이너 집합. 서비스를 위해

여러개가 묶여야하는 케이스가 있음. 파드로 컨테이너로 묶어준다. 파드로 묶어줌으로 동일한 namespace를 공유하기에 쉽게 공유 가능. 하나의 application을 동작 가능할 수 있도록 함.



ex_pod.yml

spec : 내용물



kubetctl get pods

kubetctl get po



----

### 레플리카셋(Replica set)

https://kubernetes.io/ko/docs/concepts/workloads/controllers/replicaset/

포드를 관리하는 단위. 항상 정해진 개수의 포드가 실행되는 것을 보장해준다.

일반적으로 deployment를 이용해서 많이 사용함. 

```
vagrant@ubuntu:~$ minikube status
! Executing "docker container inspect minikube --format={{.State.Status}}" took an unusually long time: 7.182396497s
* Restarting the docker service may improve performance.
minikube
type: Control Plane
host: Stopped
kubelet: Stopped
apiserver: Stopped
kubeconfig: Stopped

vagrant@ubuntu:~$ minikube start

vagrant@ubuntu:~$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

```

컨테이너나 파드를 개별 사용자가 생성, 삭제하는 것은 올바른 방법은 아님.

파드 상위 객체인 레플리카 셋 필요. 