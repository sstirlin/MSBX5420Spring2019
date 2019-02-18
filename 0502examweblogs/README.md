# Exam 1 instructions

You will need to submit a single notebook into Canvas (note:  I want the notebook itself, NOT the HTML version).
You can download it using this command:
```
wget https://raw.githubusercontent.com/sstirlin/MSBX5420Spring2019/master/0502examweblogs/exam1.ipynb
```

Watch this help video to help you with Problem 1!

https://drive.google.com/file/d/1qdE3s9zfRIJGDkcqW3vuQVyF18mHsvhK/view?usp=sharing


## Errata

### Problems 2-5

Please ONLY use `good_rdd` to make your estimates for these problems.  You shouldn't need any of
the other RDDs that we worked with in Problem 1.

### Problem 3

Two mistakes here (to my embarrassment).  First, I intended for you to compute the fraction of
**UNsuccessful** requests.  Also, I forgot to tell you the name of the variable to store you estimate.
Use `unsuccessful_ratio`.

### Problem 1

Parsing `requested_resource` is actually broken into a 2-part problem.  In the first part we are ASSUMING that
there are always 3 fields, like this:
```
GET /a/cool/resource.html HTTP/1.0
```
In the second part we discover that isn't true.  In fact there are sometimes only 2 fields, like this
```
GET /a/cool/resource.html
```
or even this
```
GET  HTTP/1.0
```
Your "better" regex needs to take these into account.  At the end of the day you should only find 1 bad entry.
