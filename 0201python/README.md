This week there is no lecture (because of MLK), so please watch the five videos below that
I have prepared.  Your homework is described in the videos.

## Homework TL;DR

You need to submit to Canvas 4 files:

```
hello_world.ipynb
hello_world.html
self_driving_twitter_sentiment.ipynb
self_driving_twitter_sentiment.html
```

## Videos (introduction to Python for data scientists)

Apologies for the lousy sound quality - I was forced to use a different laptop this week!

https://drive.google.com/file/d/1k5Yflp-S3THiVhEKSwf2j3yD3U362P2x/view?usp=sharing
https://drive.google.com/file/d/1Zb9GHhHY6ILG6fW1YbHnIMgOdgbsMnBP/view?usp=sharing
https://drive.google.com/file/d/16RiW7WG1E5li_oBYGLMHY4pURxJXJeow/view?usp=sharing
https://drive.google.com/file/d/1VId_DvwmcuiSUGqnZG041zXM2zxemZEM/view?usp=sharing
https://drive.google.com/file/d/1SBxyH_lqo-TQp9sZ-hZZ7K-bF9qauB-I/view?usp=sharing


## Quickstart to get Python running (described in first video)

To start your Linux virtual machine do the following in your host operating system (probably Windows or OSX):
```sh
# This is a comment.  Don't type commands in that start with #

# Open up a command prompt (Windows) or terminal (OSX)
cd msbx5420vagrant
vagrant up
```

After it boots up run the following in your Linux VM:
```sh
# Open up a terminal and type the following commands

# Create a python 3.7 environment (should only need to do this once)
conda create -n py37 python=3.7

# Activate your python environment (needs to be done every time you open up a new terminal)
conda activate py37

# Let's install some packages (should only need to run this once)
conda install jupyter pandas plotly
pip install textblob

# Let's organize our work by creating some directories
mkdir projects
cd projects
mkdir python_tutorial
cd python_tutorial

# Now let's start Jupyter
jupyter notebook

# A browser should open up in your VM now.  You are in Jupyter NOW!!!
# Click New->Python 3 to start a new Python 3 notebook.
```
