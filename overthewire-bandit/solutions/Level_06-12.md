Level 06:

Given a user and group of file we can easily find using this command:
```
find / -user bandit7  -group bandit6 -size 33c
```

To eliminate permission error in output i used `2>/dev/null`
- number 2 is fot stderr which means it show error in output
- we are send it to /dev/null so that we do not get in out put

using this command got this:

```
/var/lib/dpkg/info/bandit7.password

```

password for Level 07 : morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

Level 07:

Given:
password is stored next millionth in data.txt
used:
```
cat data.txt | grep millionth

```

password for level 08 : dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

Level 08:

Given:
password line is the only line which occurs only one time
used this:
```
sort data.txt | uniq -u -c 
```

password for level 09: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

Level 09:

given:
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

used:
```
strings data.txt | grep '====='
```
got this:
```
strings data.txt | grep '====='
========== the
========== password{k
=========== is
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

```

password for level 10:  FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

Level 10:
given:
the password is encoded in base64 

```
base64 -d data.txt 
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```
password for level 11: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

Level 11:

given:
ROT 13
we can use tr to get the actual value

```
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```
password for level 12: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4



Level 12:

Given:
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed.

- used xxd to with -r (reverse) to get the binary
- Then got repeatdly compressed file in bzip, gzip, and tar.
- approximetly upto 10 times.

  At the got this txt file.
```
  /tmp/lvl_12_tmp$ cat data8.txt 
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

```
`Password for lvl 13 is = FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`
