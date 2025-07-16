
Level 13:

Given
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. 

used ssh key to login to bandit 14 using ssh

`ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220`

and then just read the password for bandit 14.

`The password for bandit 14 = MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`


Level 14:

Given:
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

using netcat to connect on port 30000

```
nc 127.0.0.1 30000 -v
Connection to 127.0.0.1 30000 port [tcp/*] succeeded!
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

```

`The password for Level 15 = 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo`

Level 15: 

Given:
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

In this we have to use openssl toolkit to connect 

used this command and put in the password of current level:

```
openssl s_client -connect 10.0.1.228:30001
read R BLOCK
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

closed

```

`The password for level 16 = kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx'



Level 16:

Given:
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Used nmap to get the open port and services;

```
nmap localhost -p 31000-32000 -sV -v

```
Got multipe open port but 31790 open with ssl.

connect using openssl s_client
```
openssl s_client -connect localhost:31790  -quiet
```

we got an RSA and saved it in sshkey.private to use it to connect bandit 17\

```
cat sshkey.private                          
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

```

then used;
```
ssh -i /path/to/sshkey.private bandit17@bandit.labs.overthewire.org
```

Got it
now we just have to read the password of the level 17 so that when connect again we do not have to use the private key again
```
cat /etc/bandit_pass/bandit17 
EReVavePLFHtFlFsjn3hyzMlvSuSAcRD

```



`The password for Level 17 = EReVavePLFHtFlFsjn3hyzMlvSuSAcRD`


Level 17:

Given:

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

just used diff command to differentiate both files.

```
$ diff  passwords.old passwords.new 
42c42
< C6XNBdYOkgt5ARXESMKWWOUwBeaIQZ0Y
---
> x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

```

`The password for Level 18 = x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`

Level 18:

Given:
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

used this command:

```
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme

```

`The password for level 19 = cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

Level 19:

Given:
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

we just have to use setuid binary to execute command as bandit 20 user
command:
```
./bandit20-do cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

```

`
The password for Level 20 = 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
`

Level 20:

Given:
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

Explaination of Script:
The setuid binary provided in this level is a program that connects to localhost on a port you specify as an argument. Once connected, it waits to read a single line of input from that connection. It then compares the received line to the password from the previous level (bandit20). If the password is correct, the binary sends back the password for the next level (bandit21) through the same connection. To solve the level, you need to create a simple local server (using tools like nc) that listens on a chosen port and sends the bandit20 password when the binary connects. If done correctly, the server will receive the bandit21 password in response.

To solve this made  session using tmux 
On one session started listening on port 4444 with the password of the current level using netcat using this command:
```
echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l 4444

```
Then connected on port 4444 using the script:
```
./suconnect 4444
```

Done now we got the password for then next level 
```
echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l 4444
EeoULMCra2q0dSkYj561DX7s1CpBuOBt

```

`The password for the level 21 =EeoULMCra2q0dSkYj561DX7s1CpBuOBt`
