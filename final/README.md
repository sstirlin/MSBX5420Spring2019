# Recommendation system for online purchases

In this final you will use Elasticsearch to build a recommendation system for an online
retail company.

The inspiration is drawn from this article (building something similar for ingredients in recipes):

[A recommender system for ingredients in recipes](https://qbox.io/blog/building-simple-recommender-systems-for-elasticsearch-1) 

This final is fairly open-ended.  In other words, it resembles projects that you might encounter
in your jobs.  I am telling you the business requirement, but it is up to you to figure out a
Minimum Value Product (MVP) to deliver.

## The dataset

The dataset consists of a list of items purchased.  Grouping by Invoice Num, you can see
that items often appear together in the same market basket.  You will use Elasticsearch to
understand these co-occurrences and use them to make future recommendations (much like Amazon's
"Customers who bought this also bought <whatever>".

[Retail dataset](https://archive.ics.uci.edu/ml/datasets/online+retail#)

A great thing to do is to split this dataset into training and test sets.  Since they are
time-ordered, perhaps choose the first 80% of invoices as training, and the rest as a test set.


## What you will submit

You will submit to Canvas a `.tar.gz` file that contains your project all zipped up.  It is mostly
up to you to decide how to structure your project, but remember that neatness and code readability are
extremely IMPORTANT.  If I cannot figure out what you are doing then I'm likely to stop looking at it.

Your project should include a file named `README.md` explaining how to run your project,
expected inputs and outputs, etc.  This document should be written in Markdown, which is a very common 
(and easy to learn) documentation format.

https://guides.github.com/features/mastering-markdown/


## Some guidance

The dataset comes as an `.xlsx` file (Excel).  You should use `pandas` to read it in.  You will probably
want to group rows that have the same Invoice Num together (aka a "basket").  For each basket you
should produce a message that describes the basket.

Part of the challenge is to figure out what your json messages should look like.  They need to have all of the
information describing the basket, but also be "Elasticsearch friendly".  After all, Elasticsearch is what
is going to give you the recommendations.

In a real system you would produce each message to Kafka, then run a separate program that consumes
from Kafka and flings to Elasticsearch (in other words, exactly the pattern that was used in Week 13 homework).

However, if you don't think you will have time then go ahead and fling directly from pandas into
Elasticsearch (i.e. bypass Kafka).

As far as the Elasticsearch analysis is concerned, you shouldn't need to know much more about Lucene than was
presented in Week 15 lecture.  In fact, you can probably copy those queries/aggregations almost exactly
and get a reasonable recommender running.  The goal is to have some familiarity with Lucene, not become an
expert.


## Visualizations

"It is not enough for justice to be done.  It must be SEEN to be done." - a random movie quote that you won't know anyway

You will find in your jobs that bosses want to SEE your system running (whatever that means).  If you can figure
out some cool dashboards in Kibana then go for it.  If you manage to create something interesting
then include screenshots in your `.tar.gz` submission.

Often I find this aspect of building a system challenging.  Still, it is a fact of life.  The sooner you get used
to concocting visualizations to satisfy non-technical people, the better.
