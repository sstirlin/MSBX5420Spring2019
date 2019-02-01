# Week 4 Homework

This week your homework will give you some solid experience with Spark.  You will be
analyzing weblogs from NASA and extracting insights.

## Quickstart

First, in your VM, make sure that your spark docker container is running:
```
docker ps
```

If your spark container is not listed then it might just be stopped.  See
if you can find it in the list of stopped containers:
```
docker ps -a
```
If so then you can restart it with `docker start spark`.

Otherwise, you will need to create a new container:
```
docker run -d --name spark  -p 8888:8888  \
    -v $HOME/work:/home/jovyan/work:rw  \
     jupyter/all-spark-notebook \
     start-notebook.sh --NotebookApp.token='' 
```

Use `docker ps` to verify that the container is now running.

Recall that this container is "batteries included", so it already contains
a running instance of Python, Jupyter, and Spark.

Browse to `localhost:8888` and Jupyter should show up.

## Download data

Back in the terminal, step into your work directory and create a new place for
this weeks homework to live:
```
cd ~/work
mkdir week4
cd week4
```

Now we will download two files containing weblog data that we will analyze.  You *could* download these
from your browser, but we're command-line junkies now.

There are two ways to download files
on the command line:  `wget` and `curl`.  Let's use `wget` today for no particular reason:
```
wget ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz
wget ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz
```
(Aside:  notice that NASA is providing these files *not* using the web protocol `http` that you are accustomed to,
but instead is using the "File Transfer Protocol" `ftp`.  Browsers can "speak" dozens of protocols, actually).




