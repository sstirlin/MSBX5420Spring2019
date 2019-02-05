# Week 4 Homework

This week your homework will give you some experience with Spark and prepare
you for next week's exam (where you will be analyzing weblogs from NASA and extracting insights).

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

If you couldn't find the container at all then you need to create a new container:
```
docker run -d --name spark  -p 8888:8888  \
    -v $HOME/work:/home/jovyan/work:rw  \
     jupyter/all-spark-notebook \
     start-notebook.sh --NotebookApp.token='' 
```

Use `docker ps` to verify that the container is now running.

Recall that this container is "batteries included", so it already contains
a running instance of Python, Jupyter, and Spark.  **You do not need to start
Jupyter (using Anaconda).  An instance of Jupyter is already running in the docker container.**

Browse to `localhost:8888` and Jupyter should show up.

## Download data

Back in the terminal, step into your work directory and create a new place for
this week's homework to live:
```
cd ~/work
mkdir week4
cd week4
```

Now we will download two files from NASA containing weblog data.  We *could* download these
using a regular browser, but we're command-line junkies now.

There are two ways to download files
on the command line:  `wget` and `curl`.  Let's use `wget` today for no particular reason:
```
wget ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz
wget ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz
```
(Aside:  notice that NASA is *not* publishing these files using `http` (HyperText Transfer Protocol),
but instead they are using "File Transfer Protocol" `ftp`.  That's fine - browsers "speak" dozens of protocols).

## Inspect data

The weblogs (from 1995!) are stored as text files that have been compressed (zipped).  Each line
records a separate request.

### About compression

There are several popular compression algorithms in common use.  For example, you have certainly dealt with files
compressed using the PKZip algorithm (they have a `.zip` extension).

In Linux you will commonly see files compressed
using GNU Gzip (they have a `.gz` extension) and BZip2 (extension `.bz2`).
All of these formats are totally different and incompatible with each other!

### Decompress

Let's decompress one of these files to look at it
```
gunzip NASA_access_log_Jul95.gz
```

If you `ls` out the directory you will see the following files:
```
NASA_access_log_Aug95.gz
NASA_access_log_Jul95
```

We *could* open up the July logfile in `nano`, but this file is quite large (about 200 megabytes).
Instead, let's use the handy `tail` command to look at the last few lines of the file:
```
tail NASA_access_log_Jul95
```

The output should look like this:
```
slipper12055.iaccess.za - - [28/Jul/1995:13:32:22 -0400] "GET /images/USA-logosmall.gif HTTP/1.0" 200 234
163.205.53.14 - - [28/Jul/1995:13:32:22 -0400] "GET /shuttle/technology/images/srb_mod_compare_1-small.gif HTTP/1.0" 200 36902
maynard.isi.uconn.edu - - [28/Jul/1995:13:32:22 -0400] "GET /images/shuttle-patch-logo.gif HTTP/1.0" 200 891
163.205.53.14 - - [28/Jul/1995:13:32:22 -0400] "GET /shuttle/technology/images/srb_mod_compare_3-small.gif HTTP/1.0" 200 55666
163.205.53.14 - - [28/Jul/1995:13:32:22 -0400] "GET /shuttle/technology/images/srb_mod_compare_6-small.gif HTTP/1.0" 200 28219
163.205.53.14 - - [28/Jul/1995:13:32:23 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
tiger2.ocs.lsu.edu - - [28/Jul/1995:13:32:23 -0400] "GET /shuttle/missions/missions.html HTTP/1.0" 200 8677
199.0.2.27 - - [28/Jul/1995:13:32:23 -0400] "GET /images/ksclogo-medium.gif HTTP/1.0" 200 5866
tornado.umd.edu - - [28/Jul/1995:13:32:25 -0400] "GET /shuttle/missions/sts-74/sts-74-patch-small.gif HTTP/1.0" 200 5494
```

Each line is a separate log entry that records a request to NASA's website in July 1995.

The format is as follows:
```
requesting_host user_identity user_local_identity [timestamp] "requested_resource" return_code bytes_transferred
```

- `requesting_host` This is the IP address or DNS name of the host that made the request
- `user_identity` Ignore this.  It is often missing anyway (indicated by "-")
- `user_local_identity` Ignore this.  It is often missing anyway (indicated by "-")
- `timestamp` Date and time when the request occurred
- `requested_resource` The request itself.  It has the format `METHOD /path/to/resource PROTOCOL/VERSION`
- `return_code` The [HTTP return code](https://www.restapitutorial.com/httpstatuscodes.html).  For example, 200 means "success"
- `bytes_transferred` Number of bytes transferred.  Can be 0 or - if nothing was transferred

**Enrichment**:  You can learn more about [HTTP methods](https://www.w3schools.com/tags/ref_httpmethods.asp).
We probably won't do much HTTP programming in this class, but it is used everywhere to build
[REST](https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f) services.

### Compress again

Let's compress the log file again so that (later) we can demonstrate that Spark can decompress "on the fly":
```
gzip NASA_access_log_Jul95
```

## Download notebooks

You will submit 2 notebooks.  Use these commands to download them:

```
wget https://raw.githubusercontent.com/sstirlin/MSBX5420Spring2019/master/0402sparkweblogs/weblog_analysis1.ipynb
wget https://raw.githubusercontent.com/sstirlin/MSBX5420Spring2019/master/0402sparkweblogs/weblog_analysis2.ipynb
```

## Errata

### In `weblog_analysis1.ipynb`

There is an interesting issue that happens when you read the files using the command
```
logs_rdd = sc.textFile('NASA_access_log_*.gz')
```
As I mentioned in lecture, the ORDER that operations occur in Spark can be tricky business.  Here, there is no
guarantee which of the two files will be read in first.  In order to pass the unit tests below it we need to
fix the order.  Change the command to this instead:
```
logs_rdd = sc.textFile('NASA_access_log_Aug95.gz,NASA_access_log_Jul95.gz')
```
