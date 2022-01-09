# Let's build the simplest and most usefull commands together


# life saver unix commands

clear cmd promptline
```
clear
```

checks which directory you are in
```
pwd
```

Bir alt komut
```
cd ..
```
makes directory 
```
mkdir test
```
delete directory or file
```
rm -r test
```

move folder
```
mv /Folder/Subfolder/test /Folder/AnotherFolder
```
to read content we use it.
```
cat read.txt
```

create file
```
vim text.txt
```
```
insert and press (i) 
```

quits
```
:q 
```
quits without saving
```
:q!
```
saves and quits
```
:wq
```



# life saver git commands

helps the commands of git
```
git help
```

see the version of git
```
git --version
```
if you are into the project directory you can create git env by
```
git init
```
to see the status what is happening inside git 
```
git status
```
adds files to the Git index, which is a staging area for objects prepared to be commited
```
git add.
```
commits the files that have been added and creates a new revision with a log
```
git commit -m "first commit"
```
pushs files to the github
```
git push -u origin master
```
let you create and switch to a new branch. "b" stands for branch
```
git checkout -b uca
```

creates a user name 
```
git config --global user.name "utku"
```
shows the current branch
```
git branch
```
adds origin via https or ssh. (better configure ssh)
```
git remote add origin https://....git ya da ssh olanı
```

while in committing, you can see the past logs 
```
git log
```
check the commit message
```
git log --oneline
```
same as log
```
git log --graph
```
removes the file from staging area
```
git rm --cached file.txt
```
change the commit message
```
git commit --amend -m "changed commit"
```
creates ssh key
```
ssh-keygen
```
get the key generated and paste it to the github
```
cat~/.ssh/id_rsa.pub 
```

remove the .idea folder from git
```
git checkout master -- .gitignore
```
```
git rm --cached -r .idea
```