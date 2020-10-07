## aws configure를 잘못했을 때 

[ec2-user@ip-10-0-0-115 ~]$ ls -al

total 28

drwx------ 4 ec2-user ec2-user 4096 Oct 7 02:35 .

drwxr-xr-x 3 root   root   4096 Oct 7 02:33 ..

drwxrwxr-x 2 ec2-user ec2-user 4096 Oct 7 02:35 .aws	⇐ 디렉터리 삭제

-rw-r--r-- 1 ec2-user ec2-user  18 Jun 16 18:13 .bash_logout

-rw-r--r-- 1 ec2-user ec2-user 193 Jun 16 18:13 .bash_profile

-rw-r--r-- 1 ec2-user ec2-user 124 Jun 16 18:13 .bashrc

drwx------ 2 ec2-user ec2-user 4096 Oct 7 02:33 .ssh

[ec2-user@ip-10-0-0-115 ~]$ rm -rf .aws