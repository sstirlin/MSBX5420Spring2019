# Homework Week 7

For the homework this week we will momentarily step away from Spark and
concentrate on some basic data engineering tasks:

1. You will create an account on Github and start using `git` to manage
your work.  Please watch [this video](../0604git/README.md) to understand
the basics of using git and Github.

2. You will learn some basics about programming in `bash`.  You will write
a script called `unpack.sh` that unzips the CWL datasets.

3. You will perform some manual analysis of the `json` files in Python (without Spark).

4. You will upload the `json` files into HDFS for analysis in Spark next week.


# Unpacking CWL data

You should already have the CWL data downloaded into your `~/work/week6` directory.
If not follow the instructions [here](../0602jsontutorial/README.md).

Make a new directory to work in:
```
cd ~/work
mkdir week7
cd week7
```
In the week7 folder you need to unpack all of the 2018 data that is in
`~/work/week6/cwl-data/data/structured/`.

For example, there is a file
`~/work/week6/cwl-data/data/structured/structured-2018-01-14-neworleans.tar.gz'.
When you unzip and untar it into `week7` you should get a directory  
`~/work/week7/structured-2018-01-14-neworleans/` that contains many json files.
Repeat this for ALL of the 2018 data.

You will write a bash script named `unpack.sh` to automate this.  Do NOT just manually process 
the filenames one at a time.  Instead, you will write a `for` loop in a bash script.

To learn how to write bash scripts you might start with this short [video](https://www.youtube.com/watch?v=F-gskSl4pwQ),
then move on to this [tutorial](https://ryanstutorials.net/bash-scripting-tutorial/).

Commit your `unpack.sh` script to a repo named `week7` in Github.

In Canvas submit a link to your `week7` repo in the comments so that I can verify.


## Basic analysis in Python




## Upload files to HDFS `upload_cwl_hdfs.ipynb`

Next week we will analyize this unpacked data in Spark, so we need to upload it
all to HDFS.  

Create a new Jupyter notebook named `upload_cwl_hdfs.ipynb` that uploads ALL
of your unpacked directories to `/Users/vagrant/` in HDFS.  Keep the directory
structure intact, so when you do `client.list('/Users/vagrant/')` the output
should look like this (these are all directories containing json files):
```
['structured-2018-01-14-neworleans',
 'structured-2018-03-11-atlanta',
 'structured-2018-04-01-birmingham',
 'structured-2018-04-08-proleague1',
 'structured-2018-04-19-relegation',
 'structured-2018-04-22-seattle',
 'structured-2018-06-17-anaheim',
 'structured-2018-07-29-proleague2',
 'structured-2018-08-19-champs']
```
Some useful functions for you can be found in the Python library `os`, in particular
in `os.path`.  Another very useful library is `glob`.

Commit your `upload_cwl_hdfs.ipynb` file to your `week7` repo up on Github.
