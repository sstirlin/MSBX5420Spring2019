# Unpacking CWL data and uploading to HDFS

You will create your own account up in Github (choose your username wisely -
this is your developer "persona" long past the end of this course).

Create a new repo
named `week6`.  In this repo you will commit two files:

- `unpack.sh`
- `upload_cwl_hdfs.ipynb`

In Canvas you will submit a *link* to your repo.


## `unpack.sh`

As we have seen, the json files are all tarred and gzipped.  We need
to unpack them all (limiting ourselves to 2018 data only).

We will automate this using a `bash` script.

First let's have a look at the zipped files:
```
cd ~/work/week6/
cd cwl-data/data/structured/structured-2018*.tar.gz
```

Recall that we unzipped our New Orleans file with the following command:
```
tar zxvf cwl-data/data/structured/sstructured-2018-01-14-neworleans.tar.gz
```

Write a bash script (using `nano`) named `unpack.sh` that automates
unpacking all of these `.tar.gz` files.  You will have to google around
to learn some bash scripting basics.  YOU ARE READY!

Then run it like this:
```
bash unpack.sh
```

## `upload_cwl_hdfs.ipynb`

Once all of the `.tar.gz` files have been unpacked, we need to upload them to
HDFS.

Create a new Jupyter notebook named `upload_cwl_hdfs.ipynb` that uploads ALL
of your unpacked directories to `/Users/vagrant/` in HDFS (keep the directory
structure intact).

Some useful functions for you can be found in the Python library `os`, in particular
in `os.path`.  Another one to check out is `glob`.
