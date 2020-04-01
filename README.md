# sphinx-gitlab-quickstart
Creates a git repository for a Sphinx project using jinia templates and a UI for creation

This creates a Sphinx project as a git repository and adds files for automated document builds using a Makefile and gitlab CI. 
It is using template files with the django template engine and a small tkinter GUI to set your project up.
It contains an Example for an a4 size Document.

It is only tested on Ubuntu 18.04.04 with python 3.7 and texlive

Usage:
*******

clone this repository to a Linux box

install the required software texlive, pandoc, ghostscript, python3
install requirements with pip from requirements.txt

cd to sphinx-gitlab-quickstart and run start.sh
Click on run this configuration Button
cd ../my-first-project
Here you will find a very complete Sphinx project

If you change the Project name, selecting the Project directory will update 
most variables, even if you do not change it.

type make and the project will be built as pdf, size reduced pdf, epub, html and docx

look into the build directory.

Gitlab CI
=========

You will need to install the gitlab-runner as described by gitlab. The user gitlab-runner
must live in /home/gitlab-runner. The user gitlab-runner must be able to build the my-first-project,
then the CI for a shell runner will work to.

**the curses part is not yet implemented**




