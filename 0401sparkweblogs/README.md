# Week 4 Homework

This week your homework will give you some solid experience with Spark.  You will be
analyzing weblogs from NASA and extracting insights.

First, in your VM, make sure that your `spark` docker container is running:
```
docker ps
```

If your `spark` container does not show up then it might just be stopped.  See
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
