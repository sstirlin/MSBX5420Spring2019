# Introduction to JSON

We are going to download some data (from Call of Duty) locally to our VM.


## What is Call of Duty World League?

Call of Duty World League is a series of competitive play eSports tournaments:

https://www.callofduty.com/content/dam/atvi/callofduty/esports-new/2018-articles/CWL_Champs_2018_Recap_TOUT.jpg

https://www.youtube.com/watch?v=BmLUlJ5bFIU

We have curated data for 2018 and released it to the public.  We will use this for the next couple of
weeks to learn more about serialization and Spark.


## Download data locally to VM

First step is to download the Call of Duty World League data locally to your VM:
```
cd ~/work
mkdir week6
cd week6
git clone https://github.com/Activision/cwl-data.git
```

```
cd cwl-data/
cd data/
cd structured/
```

## Unpack the 2018 New Orleans .tar.gz file to have a look

```
gunzip structured-2018-01-14-neworleans.tar.gz
tar xvf structured-2018-01-14-neworleans.tar
```
alternatively, we could've done this all in one command
```
tar zxvf structured-2018-01-14-neworleans.tar.gz
```
Go ahead and look at what one of the json files looks like!
```
cd structured-2018-01-14-neworleans/
nano structured-1515984523-6592b573-b485-58b0-963e-6be0b4d02f6c.json
cd ..
```
Let's gzip the neworleans file back up:
```
gzip structured-2018-01-14-neworleans.tar
```

## JSON tutorial in Python

This JSON will be easier to explore in Python.
```
cd ~/work/week6
conda activate py37
conda install ujson
jupyter notebook
```

[Lecture notebook here](lecture_jsontutorial.ipynb)
