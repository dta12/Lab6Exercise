# NameGrader
An open source project by Dastan Abdulla and Brian Kim
# Software Use
This program asks the user for their name and the length of their name. After that, It returns an algorithmic score based on the relative position of each letter in their name and the alphabet.
# How to use it
## Installation
Begin by installing git on your system. AFter that, Clone the main repoistory labeled "Lab6Exercise" by copying the command below into your terminal of choice. After that, go into /src and then you have two choices there; either open the .py file, or open the .ipynb file which is a jupyter notebook file. If you go with the notebook path, you will need an Ide that recognizes ipynb files. Two possible options are the web jupyter software, or visual studio code. Both of the files behave in the same manner, it is up to you to decide which one you prefer. <br/>
``
$ git clone https://github.com/dta12/Lab6Exercise
``

## Usage
To begin using the software, either compile the .py file and then run it, or run the first code block in the .ipynb file. In both cases, they will ask you for your name. AFter typing that in and pressing enter, it will ask you for the number of letters in your name( do not count whitespaces, or any punctuation mark such as a hyphen). AFter typing both of these things in, the program will output a numeric result which is the score your name recieved. The score itself does not equate to any realistic value and it does not carry any meaning.
## How to contribute
To contribute to the project, you will need to fork the main repository wth the SSH protocol. Your changes need to occur in the forked repository. After applying the fork, clone the forked repo onto your locally system by following the command below. <br/>
``
git clone <forked-repo-link>
``<br/>
to be able to make changed onto the forked repoistory you need to run the command below. <br/>
``
git remote add upstream 
``<br/>
after the above setup, to make sure you have the most recent updated master repo you need to run the command below. <br/>
``
git pull upstream master
``<br/>
which will update your local clone on your machine to the most recent version. <br/>
Finally to apply changes to the forked repo, you need to enter the command below.<br/>
``
git push origin master
``<br/>
to contribute your changes to the project, you need to make a pull request for your forked repository and then the project maintainer will examine it and decide whether to add the changes or not. <br/>
#Miscellany
We chose to use the permissive MIT license since it has few limitations to use our project in whatever way the user wants. It grants users the ability to modify and/or distribute for private and commercial use, with the condition that our copyright and license is included.


