# Day 70 – Git Github & Version Control

## Git Github & Version Control Overview

Even though i little bit know about git and github like how i can push projects to github still in the Day 70 i learned so many new things about Git, Github and version control Day 70 that helps me understood how developers track changes in their code, work with others, and keep their projects safe online. I learned so many other things like how to use Git on my computer (local repository) and connect it to GitHub (remote repository) so my code is backed up online. I also learned how to work with branches, merge code, ignore certain files, clone existing projects, and even learned that how i can contribute to other people's projects using forks and pull requests. These are essential skills that every developer needs to know.

## What I Have Learned

* **Basic Git Bash Commands**: In Git Bash (a command line tool for Git), I learned several useful commands. touch filename creates a new file. start filename opens that file. mkdir foldername creates a new folder or directory. ls shows all files and folders in the current directory, and ls -a shows hidden files too.

* **Adding Files to Staging Area**: Before Git can save your changes, you need to add files to the staging area using git add filename. This is like telling Git "these are the files I want to save". You can add one file at a time or use git add . to add everything.

* **git init{Creating a Local Repository}**: When I run git init in a folder, Git creates a hidden folder called .git inside it. This turns my regular folder into a local repository - a place where Git starts tracking every change I make. Git saves different versions of my files so I can go back to any previous version if I need to

* **git commit{Saving Changes}**: After adding files to the staging area, I use git commit -m "message" to actually save them. The -m flag lets me write a short message explaining what changes I made (like "added login feature"). 

* **Checking Status and History**: git status shows me which files are changed, which are staged, and which are ready to commit. git log shows me the complete history of all commits I've made.

* **Removing Files from Staging**: If I accidentally added files I don't want to commit, I can use git rm --cached -r . to remove everything from the staging area. The --cached flag removes them from staging but keeps the files on my computer, and -r means remove recursively (all files and folders).

* **.gitignore{Ignoring Files}**: I learned about .gitignore - a special file where I list files or folders that Git should ignore and never track. This is useful for hiding secret files (like API keys), temporary files, or large folders that don't need to be in the repository. Once

* **git clone(Copying a Remote Repository)**: git clone <repository-link> downloads an entire repository from GitHub to my computer. This is how developers start working on existing projects. Cloning gives you everything - all files, all folders, and the entire commit history. and we can modify that existing project and add new features in it.

* **Branching(Creating Side Branches)**: Branching lets me create a separate copy of my code called a branch. I use git branch branch-name to create a new branch, and git checkout branch-name to switch to it. While working on a branch, I can add new features or experiment without affecting the main code. Branches are like having multiple versions of the same code where if we later wants those features to be added in the main branch than we can merge this side branch to main branch using merge branch name command.

* **Merging(Combining Branches)**: When I finish working on a seperate branch and I want to bring those changes back into the main branch, I can use git merge branch-name. First I switch to the main branch (git checkout main), then run git merge branch-name. Git combines all the changes from both branches. 

* **Forking(Copying Someone Else's Repository)**: Forking is like making a personal copy of someone else's GitHub repository. It's different from cloning because a fork stays on GitHub under my account, while a clone is only on my computer. Forking lets me take any open-source project and experiment with it without affecting the original project.

* **Pull Request{Proposing Changes to Original Project}**: After I make improvements in my forked copy, I can send a pull request to the original project owner. A pull request is like saying "Hey, I made some changes in my copy. Would you like to add them to your project?" The owner can review my changes and decide to accept (merge) or reject them. This is how most open-source contributions work.


## How It Works

### Git Basics

* **Creating and Opening Files**:  I use touch main.py to create a new python file. Then I use start main.py to open it in my default editor (pycharm). This is faster than using the mouse to create files.

* **Making a Folder a Git Repository**: I navigate to my project folder using cd foldername, then run git init. Git creates a hidden .git folder inside. Now Git will track every change I make in this folder.

* **Checking What's Happening**:  I use git status to see which files are changed, which are new, and which are ready to be committed. This is the most useful command because it tells me exactly what's going on.

* **Saving My Work (Committing)**: First I add files using git add . (the dot means "add everything"). Then I commit using git commit -m "added homepage". The message should be short but descriptive so I know what this commit contains later.

* **Ignoring Secret Files**:  I create a .gitignore file using touch .gitignore. Inside this file, I write names of files or folders Git should ignore, like secrets.txt or env/. Git will never track or back up these files.

### Remote Repositories (GitHub)

* **Downloading a Project from GitHub**:  I use git clone `git url link` to download the entire project to my computer. This gives me all the files, folders, and commit history. It's like making a full copy which i can letter modify and add new feature in that project.

### Branching and Merging

* **Creating a New Branch**: I use git branch new-feature to create a branch called "new-branch". Then I use git checkout new-branch to switch to it. Now I can add new code without touching the main branch same file code.

* **Switching Between Branches**: git checkout main takes me back to the main branch. git checkout new-branch takes me back to my new-branch. I can switch back and forth anytime.

* **Merging a Branch into Main**: First I switch to main using git checkout main. Then I run git merge new-branch. Git takes all the changes from "new-branch" and adds them to main. If there are no conflicts, it's automatic.

* **Contact Route**: When someone submits the contact form (POST request), it grabs their name, email, phone number, and message, sends an email to the site owner, and shows a success message. On GET request, it just shows the contact form.

### Branching and Merging

* **Forking Someone's Repository**: I go to a GitHub repository I want to contribute to and click the "Fork" button at the top right. GitHub creates a copy of the entire project under my account. Now I can clone my fork to my computer and make changes.

* **Making Changes in My Fork**: I clone my fork using git clone `url link`, make my changes, commit them, and push back to my fork on GitHub.

* **Creating a Pull Request**: On GitHub, I open my fork and click "Pull Request" button. I write a description explaining what changes I made and why. Then I submit it. The original project owner can see my pull request, review my code, and decide to merge it or ask for changes.

## Highlights

* **Git Basics**:Learned how to create files, folders, track changes, commit snapshots, and check status using simple commands.
* **Local Repository**: Understood that git init creates a hidden .git folder that stores every version of my code.
* **Staging Area**: Learned that git add puts files in a waiting area, and git commit takes the photo and saves it forever.
* **.gitignore**: Learned to keep secret files and temporary files out of Git so they never get uploaded to GitHub.
* **Remote Repository**: Connecting my local Git repo to GitHub using git remote add origin and uploaded my commits with git push.
* **Cloning**: Downloaded entire projects from GitHub to my computer using git clone to work on existing code.
* **Branching**: Created separate branches using git branch and switched between them using git checkout to work on new features safely.
* **Merging**: Combined branches back together using git merge.
* **Forking**: Learned how to Made my own copy of someone else's GitHub repository so I could experiment without affecting their project.
* **Pull Requests**: Sent change requests to original project owners so they could review and accept my contributions to their project.




