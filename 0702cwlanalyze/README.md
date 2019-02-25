# Homework Week 7

For the homework this week we will momentarily step away from Spark and
concentrate on some basic data engineering skills:

1. You will create an account on Github and start using `git` to manage
your work.  Please watch [this video](../0604git/README.md) to understand
the basics of using git and Github.

2. You will learn how to start programming in `bash`.  You will write
a script called `unpack.sh` that unzips and extracts the CWL json files.

3. You will perform a visualization analysis of the `json` files using Python (but no Spark).

4. You will upload the `json` files into HDFS so that we can analyze in Spark next week.


## Unpacking CWL data

You should already have the CWL data downloaded into your `~/work/week6` directory.
If not follow the instructions [here](../0602jsontutorial/README.md).

Make a new directory to work in:
```
cd ~/work
mkdir week7
cd week7
```
In the `week7` folder you need to unpack all of the 2018 data that is in
`~/work/week6/cwl-data/data/structured/*.tar.gz`.

**Again, let's only worry about 2018 data for this homework!!!**

For example, there is a file
`~/work/week6/cwl-data/data/structured/structured-2018-01-14-neworleans.tar.gz`.
When you unzip and untar it into `week7` you should get a directory  
`~/work/week7/structured-2018-01-14-neworleans/` that contains many json files.

You will write a bash script named `unpack.sh` to automate this.  Do NOT just manually unpack 
the `.tar.gz` files.  Instead, you will write a `for` loop in a bash script.

To learn how to write bash scripts you might start with this short [video](https://www.youtube.com/watch?v=F-gskSl4pwQ),
then move on to this [tutorial](https://ryanstutorials.net/bash-scripting-tutorial/).

Commit your `unpack.sh` script to a repo in Github.

In Canvas submit `unpack.sh` *and also* a link to your Github repo in the comments so that I can verify.


## Basic analysis in Python

Visualization is obviously very important in data science.  In this exercise you will learn
about processing json files and building custom visualizations
using `matplotlib`.

Each of the json files that you extracted is a single match that was played.
If you deserialize one of the json files using Python
(see last week's lecture) you will notice an `events` field.  This field contains a list
of events that occurred.

There are several event types (round start, round end, etc) but we are only
interested right now in `spawn` and `death`.

Start with the images found in `~/work/week6/cwl-data/maps/ww2/`.  Produce for each match
(each json file) a "spawn-death" 
png image that shows the spawns as BLUE dots and the deaths as RED dots (NOTE: why not green and red?).

For example, in the New Orleans directory there is a json file named
`structured-1515984523-6592b573-b485-58b0-963e-6be0b4d02f6c.json`.  Your notebook should process this file
and produce an image named `structured-1515984523-6592b573-b485-58b0-963e-6be0b4d02f6c.png`
that shows where all of the spawns and deaths occurred.

A full-fledged example can be found in `~/work/week6/cwl-data/research/PlotOnMap.ipynb`.  It is
your job to decipher it and adapt it to your needs.

Do all of this work in a notebook called `visualizejson.ipynb` and check it into your repo up
on Github.

In Canvas submit `visualizejson.ipynb` as well as one example image 
`structured-1515984523-6592b573-b485-58b0-963e-6be0b4d02f6c.png`
so that I can validate what you have done (your code should process ALL of the json files, but I
only want to look at one example to verify).


## Upload files to HDFS

Next week we will analyze this unpacked data in Spark, so we need to upload it
all to HDFS.  

Create a new Jupyter notebook named `upload_cwl_hdfs.ipynb` that uploads ALL
of your unpacked directories to `/Users/vagrant/` in HDFS.  Keep the directory
structure intact, i.e. when you do `client.list('/Users/vagrant/')` the output
should show directories like this:
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

Commit your `upload_cwl_hdfs.ipynb` file to your repo up on Github and also submit it to Canvas.
