## Reading package lists... Error!

vagrant@swarm-manager:~$ sudo apt install -y tree
Reading package lists... Error!
E: Problem parsing dependency 21
E: Error occurred while processing libkf5akonadisearch-plugins (NewVersion2)
E: Problem with MergeList /var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_bionic_universe_binary-amd64_Packages

[원인] `/var/lib/apt/lists` 파일이 손상된 듯 

[해결방법]

이전 것을 지우고 `sudo rm -rf /var/lib/apt/lists/*`하고  `sudo apt-get update `해준 뒤에 사용하면 된다.

