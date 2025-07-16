Level 31:

Given:
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

We did the same steps as previous levels to clone the repo
in the level we have this :
```
bandit31@bandit:/tmp/bandit_31_ran/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

```

we have to push this key.txt file 

```
bandit31@bandit:/tmp/bandit_31_ran/repo$ cat key.txt 
May I come in?bandit31@bandit:/tmp/bandit_31_ran/repo$ git add -f key.txt 
bandit31@bandit:/tmp/bandit_31_ran/repo$ git commit -m 'Added key.txt'
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
bandit31@bandit:/tmp/bandit_31_ran/repo$ GIT_SSH_COMMAND='ssh -p 2220' git push origin master 
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes\
Please type 'yes', 'no' or the fingerprint: yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 327 bytes | 327.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost/home/bandit31-git/repo'
bandit31@bandit:/tmp/bandit_31_ran/repo$ 

```

`The password for level 32 = 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`

Level 32:
Given:

After all this git stuff, it’s time for another escape. Good luck!

we are stuck in a uppercase shell we have to escape it

```
>> LS
sh: 1: LS: Permission denied
>> ls
sh: 1: LS: Permission denied
>> $0
$ cat /etc/bandit_pass/bandit33
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
$ 

```

`The password for Level 33 = tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0`

Level 33:

Solved all the levels

```
bandit33@bandit:~$ ls
README.txt
bandit33@bandit:~$ cat README.txt 
Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know!
bandit33@bandit:~$ 

```
