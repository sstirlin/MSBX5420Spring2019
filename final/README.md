# Recommendation system for online purchases

In this final you will use Elasticsearch to build a recommendation system for an online
retail company.

The inspiration is drawn from this article (building something similar for ingredients in recipes):

[A recommender system for ingredients in recipes](https://qbox.io/blog/building-simple-recommender-systems-for-elasticsearch-1) 

This final is fairly open-ended.  In other words, it resembles projects that you might encounter
in your jobs.  I am giving you the business requirement, but it is up to you to figure out a
Minimum Viable Product (MVP) to deliver.

## The dataset

The dataset consists of items purchased from an online retailer over the course of a year or two.
If you group by Invoice Num, you can see that items are purchased together in a "basket".

You will use Elasticsearch to
learn what items are frequently purchased together and use this information to make future recommendations
(much like Amazon's "Customers who bought this also bought <whatever>").  This is called an "item-item"
recommender.

Here is the dataset:

[Retail dataset](https://archive.ics.uci.edu/ml/datasets/online+retail#)

It is good practice to split your dataset into training and test sets.  Since they are
time-ordered, perhaps choose the first 80% of invoices as training, and the rest as a test set.
Use the test set to validate your recommendations.  Do they make sense?


## What you will submit

You will submit to Canvas a `.tar.gz` file that contains your project all zipped up.  It is mostly
up to you to decide how to structure your project, but remember that neatness and code readability are
extremely IMPORTANT.  If I cannot figure it out easily then I won't spend much time on it.

Your project should include a file named `README.md` explaining how to run your project,
expected inputs and outputs, and any other relevant information.
This document should be written in Markdown, which is a very common 
(and easy to learn) documentation format.

https://guides.github.com/features/mastering-markdown/


## Some guidance

The dataset comes as an `.xlsx` file (Excel).  It is possible to open up Excel files in `pandas` directly,
but if you want you can first open it in Excel and export to `.csv` before using `pandas` to read the file. 
You should group rows that have the same Invoice Num together (aka a "basket").  For each basket you
should produce a message that describes the basket.

Part of the challenge is to figure out what your json message should look like.  It needs to have all of the
information describing the basket, but also be "Elasticsearch friendly".  After all, Elasticsearch is what
is going to perform the analysis.

In a real system you would produce each message to Kafka, then run a separate program that consumes
from Kafka and flings to Elasticsearch (exactly the pattern that was used in Week 13 homework).

However, if you don't have time then go ahead and fling directly from pandas into
Elasticsearch (i.e. bypass Kafka).

As far as the Elasticsearch analysis is concerned, you shouldn't need to know much more about Lucene than was
presented in Week 15 lecture.  In fact, you can probably copy those queries/aggregations almost exactly
and get a reasonable recommender running.  The goal is to have some familiarity with Lucene, not become an
expert.


## Visualizations

"It is not enough for justice to be done.  It must be SEEN to be done." - a random movie quote that you won't know anyway

You will find in your jobs that others want to SEE your system running (whatever that means).  If you can figure
out some cool dashboards in Kibana then go for it.  If you manage to create something interesting
then include screenshots in your `.tar.gz` submission.

Often I find this aspect of building a system challenging.  Still, it is a fact of life.  The sooner you become
accustomed to concocting visualizations to satisfy non-technical people, the better.


## Hint 1

Since many of you are struggling to get started, I spent a few minutes stubbing out how I would start.  This is
certainly not the only way to approach this problem.

First, I wrote a conversion script to convert the `.xlsx` file to a `.csv`.  This script does some minor
data cleaning as well.  It is [here](hint1/convert_xlsx_to_csv.py).  It requires you to install an extra
package to work:
```
conda install xlrd
```
However, you can ignore this conversion step.  Look [here](hint1/Online_Retail.csv) for a nice cleaned CSV dataset.  You
may start here.

Next, I have stubbed out a [flinger](hint1/es_flinger.py) to Elasticsearch.  You can see how I am structuring each
message.  The message format might require some modifications later, but this should get you started.
