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
(Aside:  notice that NASA is *not* using the web protocol `http` that you are accustomed to,
but instead the "File Transfer Protocol" `ftp`.  Browsers can "speak" dozens of protocols, actually).

## Inspect data

These are compressed (zipped) text files containing logs from NASAs web servers (back in 1995!).

### About compression

There are several popular compression algorithms in common use.  For example, you have certainly dealt with files
compressed using the PKZip algorithm (they have a `.zip` extension).

In Linux you will commonly see files compressed
using GNU Gzip (they have a `.gz` extension) and BZip2 (extension `bz2`).  There are other older formats as well.
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

We *could* open up the July logfile in `nano`, but this file is quite large (about 200 megabytes) and is hard work
for `nano`.  We can use the handy `tail` command in Linux to look at the last few lines of the file:
```
tail NASA_access_log_Jul95
```

This spits out the last several log lines of the file.  It should look like this:
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
- `user_identity` Usually missing (indicated by "-").  We will not use this
- `user_local_identity` Usually missing (indicated by "-").  We will not use this
- `timestamp` Timestamp in "DD/MMM/YYYY:HH:MM:SS -TIMEZONE" format
- `requested_resource` The request that was made in the format "METHOD /path/to/resource PROTOCOL_VERSION".  For HTTP the METHOD can
  be GET, PUT, POST, and DELETE
- `return_code` The HTTP return code.  For example, 200 means "success"
- `bytes_transferred` Number of bytes transferred to requestor.  Can be 0 or - if nothing was transferred.

### Compress again

Let's compress the log file again so that (later) we can demonstrate that Spark can decompress "on the fly":
```
gzip NASA_access_log_Jul95
```

## Download notebook

TODO
