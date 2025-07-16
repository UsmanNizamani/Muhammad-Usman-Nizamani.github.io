Level 26:
Given:
Good job getting a shell! Now hurry and grab the password for bandit27!

In this we have to go back to bandit 25 to set shell to bash
so we can interact with bandit 26

```
~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
: set shell=/bin/bash


```


Now the shell is bash 
```

~                                                                                                                             
~                                                                                                                             
~                                                                                                                             
:shell
[No write since last change]
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27 
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
bandit26@bandit:~$ 

```

`The password for the level 27 = upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`


Level 27:

Given:
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.
```

bandit27@bandit:/tmp/bandit_27_ran$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/bandit_27_ran$ cd repo/
bandit27@bandit:/tmp/bandit_27_ran/repo$ cat README 
The password to the next level is: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```

`The password to the level 28 = Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN`



Level 28:
Given:
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

We can not directly clone this repo we have to use this command:

```
GIT_SSH_COMMAND='ssh -p 2220' git clone ssh://bandit28-git@localhost/home/bandit28-git/repo

```

```
bandit28@bandit:/tmp/bandit_28_ran$ GIT_SSH_COMMAND='ssh -p 2220' git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password: 
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/bandit_28_ran$ git log -p -1
fatal: not a git repository (or any of the parent directories): .git
bandit28@bandit:/tmp/bandit_28_ran$ cd repo/
bandit28@bandit:/tmp/bandit_28_ran/repo$ git log -p -1
commit 674690a00a0056ab96048f7317b9ec20c057c06b (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000

    fix info leak

diff --git a/README.md b/README.md
index d4e3b74..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
+- password: xxxxxxxxxx
:...skipping...
commit 674690a00a0056ab96048f7317b9ec20c057c06b (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000

    fix info leak

diff --git a/README.md b/README.md
index d4e3b74..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
+- password: xxxxxxxxxx
 
~
~
~
~

```

`The password for level 29 =4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`

Level 29:

Given:
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

Clone the repository and find the password for the next level.

Cloned the repo into /tmp/bandit_29_ran using this command which tells git to use port 2220
```
GIT_SSH_COMMAND='ssh -p 2220' git clone ssh://bandit29-git@localhost/home/bandit29-git/repo

```

There is no password in README.md so we have to check logs

```
bandit29@bandit:/tmp/badnot_29_ran/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

```

We just have look for the other braches and got this :
```
bandit29@bandit:/tmp/badnot_29_ran/repo$ git branch
* master
bandit29@bandit:/tmp/badnot_29_ran/repo$ git branch -r
  origin/HEAD -> origin/master
  origin/dev
  origin/master
  origin/sploits-dev
bandit29@bandit:/tmp/badnot_29_ran/repo$ git checkout dev
branch 'dev' set up to track 'origin/dev'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/badnot_29_ran/repo$ git log -p -`
> ^C
bandit29@bandit:/tmp/badnot_29_ran/repo$ git log -p -1
commit a97d0dbf8fd910ead6fcf648829ff55c1a629c8e (HEAD -> dev, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:21 2025 +0000

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..bc6ad3d 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials
 
 - username: bandit30
-- password: <no passwords in production!>
+- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
```


`The password for level 30 = qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`


Level 30:
Given:
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.


First cloned the repo in /tmp/bandit_30_ran using this command:
```
GIT_SSH_COMMMAND='ssh -p 2220' git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
```

Got this in README.md file :
```
bandit30@bandit:/tmp/bandit_30_ran/repo$ cat README.md 
just an epmty file... muahaha

```

Check for tagging using :
`git tag`

got this:

```
bandit30@bandit:/tmp/bandit_30_ran/repo$ git tag 
secret
bandit30@bandit:/tmp/bandit_30_ran/repo$ git checkout secret 
fatal: reference is not a tree: secret
bandit30@bandit:/tmp/bandit_30_ran/repo$ git show secret 
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy

```

`The password for level 31 = fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`
