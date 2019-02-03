# MSBX 5420 - Spring 2019 Syllabus
Leeds School of Business, University of Colorado Boulder

## Contact Information

**Instructor:**  Dr. Spencer Stirling (spencer DOT stirling AT colorado DOT edu)

**Office hours:**  
- Thursdays 10:00am-11:30am at the study tables in the Koelbel atrium


## Course Description

In this course we will study how to store, process, and extract insights from *unstructured data*.
For us, unstructured data is any data that cannot be directly queried using SQL.  It arises in several situations:

- The data has simply not been loaded into a relational database yet.
- The data is too big to be loaded into a traditional relational database.
- The data might not naturally make sense in the SQL paradigm (e.g. images, emails, videos).

The main problem is to figure out how to process unstructured data *at large scale*.
We will learn how to distribute large datasets across dozens, hundreds, or even thousands of machines.  This is “Big Data”.

In particular, we will study the following:

- How to store large datasets in the **HDFS** filesystem (part of the **Hadoop** family of technologies).
  This creates a so-called **data lake**.
- How to process large datasets using **Spark** (a glorified task scheduler).
  We will also discuss the history of processing technologies such as Hadoop’s MapReduce, Tez, YARN, and Pig.
- (Where appropriate) How to model data in **Hive**, a SQL-like “view” on files in the data lake.

We will also distinguish between *data at rest* (in the data lake) versus *data in motion* (streaming in from the outside world).
For streaming data we will study:

- How to store streaming data in **Kafka**, a modern message queueing system.
- How to consume messages *from* Kafka and analyze them in near-realtime using **Spark Streaming**.
- How to *join* Kafka streams together (analogous to joining tables in SQL).

Finally, we will learn about so-called “NoSQL” datastores such as Elasticsearch and Cassandra.
We will see that these are well-suited targets for streaming data.


## Course Objectives

By the end of this course students should be able to:

- Use standard software development tools such as the Linux command line (`bash`), `git`, and `docker`.
- Store and manipulate files in HDFS.
- Write `pyspark` scripts from within a python notebook (`jupyter`), and perform analysis to extract insights.
- Create both "external" and internal `hive` tables, and understand the difference.  
  Use Hive and/or Presto to extract insights.
- Consume streaming messages from Kafka, and join/enrich streaming data using `ksql`
- Stream data into NoSQL datastores such as Elasticsearch or Cassandra, and visualize using Kibana.


## Course Materials

**Laptop:**  please bring your laptop EVERY day (including the first).  Your laptop should have minimum 4 cores and 8GB of ram (recommend 16GB or higher).
We will be installing VirtualBox and running a virtual machine (VM) that simulates a cluster.

**Course website:**  everything for this course will be available on Canvas, https://canvas.colorado.edu,
and on Github, https://github.com/sstirlin/MSBX5420Spring2019


## Grading

|Component                |Pct |
|-------------------------|----|
|Homework and Quizzes     |35% |
|Exam 1                   |20% |
|Exam 2                   |20% |
|Final                    |25% |


## Homework

Each week you will be assigned homework in order to gain practical experience.
This is the most important component of the class (in a perfect world your grade would be based 100% on homework).

It is fine to work in groups, but every student will individually submit artifacts (e.g. source code, screenshots, data files, etc).
All will be individually graded.  Late submissions will not be accepted.
Homework will be submitted online via Canvas. 

You should try EVERY line of code in the tutorials yourself, and from scratch.  DO NOT copy/paste.
Learning to code involves a surprising amount of "muscle memory".  The hours of frustrated fiddling (on
niggling details) will turn you into a wizard, and wizards make $$$.


## [Schedule](../README.md#schedule-subject-to-change)


### Academic Integrity 

All students of the University of Colorado at Boulder are responsible for knowing and adhering to the academic integrity policy of this institution. Violations of this policy may include: cheating, plagiarism, aid of academic dishonesty, fabrication, lying, bribery, and threatening behavior. All incidents of academic misconduct shall be reported to the Honor Code Council (honor@colorado.edu; 303-735-2273). Students who are found to be in violation of the academic integrity policy will be subject to both academic sanctions from the faculty member and non-academic sanctions (including but not limited to university probation, suspension, or expulsion). Other information on the Honor Code can be found at http://www.colorado.edu/policies/honor.html and at http://honorcode.colorado.edu. 

### Classroom Behavior 

Students and faculty each have responsibility for maintaining an appropriate learning environment. Those who fail to adhere to such behavioral standards may be subject to discipline. Professional courtesy and sensitivity are especially important with respect to individuals and topics dealing with differences of race, color, culture, religion, creed, politics, veteran’s status, sexual orientation, gender, gender identity and gender expression, age, disability, and nationalities. Class rosters are provided to the instructor with the student's legal name. I will gladly honor your request to address you by an alternate name or gender pronoun. Please advise me of this preference early in the semester so that I may make appropriate changes to my records. See policies at http://www.colorado.edu/policies/classbehavior.html and at http://www.colorado.edu/studentaffairs/judicialaffairs/code.html#student_code 

### Disability Services 

If you qualify for accommodations because of a disability, please submit to your professor a letter from Disability Services in a timely manner (for exam accommodations provide your letter at least one week prior to the exam) so that your needs can be addressed. Disability Services determines accommodations based on documented disabilities. Contact Disability Services at 303-492-8671 or by e-mail at dsinfo@colorado.edu. 
If you have a temporary medical condition or injury, see Temporary Injuries under Quick Links at Disability Services website (http://disabilityservices.colorado.edu/) and discuss your needs with your professor. 

### Policy Regarding Religious Observances 

Campus policy regarding religious observances requires that faculty make every effort to deal reasonably and fairly with all students who, because of religious obligations, have conflicts with scheduled exams, assignments or required attendance. Assignment and case report deadlines are not extended due to religious observance. If you cannot attend a class due to religious observance, please inform the instructor in advance. Please inform the instructor as soon as possible if you have an exam schedule conflict due to religious observance so alternative arrangements can be made. See full details at http://www.colorado.edu/policies/fac_relig.html. 

### Discrimination and Harassment 

The University of Colorado Boulder (CU-Boulder) is committed to maintaining a positive learning, working, and living environment. The University of Colorado does not discriminate on the basis of race, color, national origin, sex, age, disability, creed, religion, sexual orientation, or veteran status in admission and access to, and treatment and employment in, its educational programs and activities. (Regent Law, Article 10, amended 11/8/2001). CUBoulder will not tolerate acts of discrimination or harassment based upon Protected Classes or related retaliation against or by any employee or student. For purposes of this CU-Boulder policy, "Protected Classes" refers to race, color, national origin, sex, pregnancy, age, disability, creed, religion, sexual orientation, gender identity, gender expression, or veteran status. Individuals who believe they have been discriminated against should contact the Office of Discrimination and Harassment (ODH) at 303-492-2127 or the Office of Student Conduct (OSC) at 303-492-5550. Information about the ODH, the above referenced policies, and the campus resources available to assist individuals regarding discrimination or harassment can be obtained at http://hr.colorado.edu/dh/.
