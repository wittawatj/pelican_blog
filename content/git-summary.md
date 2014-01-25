Title: Basics on Git and Github
Date: 2013-08-14
Slug: git-summary
Tags: git

## Key Facts

* Git is a distributed version control system. 
Every collaborator gets the same copy of the project and all its change history. 
Consequently, it is possible to work offline. 
Every contributor receives a copy of the project by "cloning" its remote repository. 
After one's work is finished, it is "push"ed back to the remote repository so that 
everyone sees the changes. 

* There is no distinction of between clients and servers as all nodes have the same information.
Conceptually, push and pull can be done directly to peers. 

* Git never removes data. Only pointers are modified. 

* Git stores snapshots not patches. Internally, Git runs SHA checksum on every file. 
Every commit is just a list of file names and their corresponding checksums. 
The database mapping checksum to its content is shared among commits.
If the content of a file in two commits are the same, only the checksum needs to be stored in the two commits.
If the file is modified, a new mapping of checksum to the modified file is created and stored.

* If a file A is copied to file B, only one mapping of checksum to content is stored. 
In the commit snapshot, A is then stored along with its checksum, and B is also stored along
with the same checksum.

## Basic Commands

* Configure a global user name  

        git config --global user.name "your_name" 

* Configure your email. These user name and email will be recorded when we commit. 

        git config --global user.email "your_email"

* Initialize a git repository. A hidden folder called ".git" will be created inside the folder.
  
        git init <project_folder> 

* Show status e.g., untracked files, current brance, files modified from the last commit, etc.
This must be used inside the project folder.

        git status

* Add **content** of the file to the staging area (changes to be recorded in the next commit). 
Use . in place of <file_name> to add all files.  Use `git status` to see which files are in
the index area. 

        git add <file_name>

* Remove files from the staging area. 

        git rm --cached <file_to_remove>

* Commit. After the commit, the staging area (index) is cleaned up.
So, we need to do `git add ....` again. Note that `git commit` will commit whatever content
at the time when `git add` was run. It does not refers to the current working directory.

        git commit -m "commit message" 

* Automatically add modified files to the index and commit. New files will not be added.

        git commit -am "commit message"

* Show commit logs. Variations include `git log --oneline` to show only commit messages.

        git log 

* Show the difference between the working directory and the index. 
If the index is empty, this will compare the working directory with the last commit ?

        git diff

* Show the difference between the index and last commit. 

        git diff --cached 

## Remote Repository

In order to share code with others, we need to set up a remote repository.
A popular free Git remote repository for open-source software is [Github](https://github.com/).
Register for an account and the first thing to do is to set up a SSH key in the "account setting"
menu under the "SSH Keys" tab. The goal for this step is so that Github can correctly authenticate
the push (uploading the repository). Click "add new key" and copy your **public key** (id_rsa.pub) in the box.
On Linux, RSA key pairs can be found under `~/.ssh/` or generated with `ssh-keygen`. 

Before pushing a local repository to a remote repository, we need to add the target remote repository.
Go to the working directory and issue a command:

        git remote add origin git@github.com:you_git_user/your_project_name.git

This basically says that we want to add a new remote repository called "origin" and the URL of 
the repository is as specified in the last argument. This URL can be found after a repository is created
on Github. 

To actually push a local repository, use

        git push -u origin master

which means we want to push (upload) the master branch (default branch) to "origin".

It may be possible that a push operation is rejected possibly because the master branch on the remote
repository (called "origin/master") has a newer content than the local repository. 
In this case, it is necessary to do `git fetch` to pull the new content to the local repository,
do the merging between master and origin/master branches, and try to push again.
By default, `git fetch` will fetch all branches. 

## Branch and Merge

In Git, a branch is just a tagged snapshot.
Internally a branch is a pointer to a commit snapshot. 
Branches are useful in many ways: testing a new idea, implementing new features, etc.

* List all branches of the project.

        git branch

* Create a new branch out of the current branch. The current branch is *not* switched.

        git branch <branch_name>

* Switch the current branch to the specified branch.

        git checkout <branch_name>

* Merge the specified branch to the current branch. 

        git merge <branch_name>

* Note that a merge conflict can occur when both branches change the same file at the same location.
If that happens, Git will stop the final commit and raise the merge conflict status.
Use `git status` to see which files have the merge conflict.
Files having merge conflict problems will have a standard merge conflict mark-up at the location
where the conflict arises. This can be seen with usual text editors or diff visualizing tools e.g., [Meld](http://meldmerge.org/).
After the confict is resolved, use `git add ...` and run commit to complete the merge.
If there is no conflict, commit will be automatically done.

* `git pull` is a wrapper script for fetch and merge. Use of `git pull` is discouraged. 
It is simpler and more understandable to stay with fetch and merge.

* See the changes in branch A that are not in branch B

        git log A ^B

Source: 

* [Git tutorial on Youtube by 308tube](https://www.youtube.com/watch?v=mYjZtU1-u9Y)
* [Introduction to Git with Scott Chacon of GitHub](https://www.youtube.com/watch?v=ZDR433b0HJY)
 
