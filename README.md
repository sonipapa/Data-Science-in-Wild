# CS/INFO 5304 Assignment 0: Programming in Spark

This assignment involves 5 steps:

	**Step 1-3**: setting up Apache-Spark
	
	**Step 4**: count each word in document `wiki.txt`
	
	**Step 5**: count each digram in document `wiki.txt` and compute conditional digram probability for each digram in document `wiki.txt`.

## Step 4 and 5

### How to run the code

Launch Terminal on Mac OS and use spark-submit to run the code for **Step 4**:

```
(base) Songyus-MacBook-Pro:~ Daddy$ spark-submit /Users/Daddy/Desktop/HW0/wordcount.py /Users/Daddy/Desktop/HW0/wiki.txt /Users/Daddy/Desktop/HW0/wordcount
```

This is what I submitted to the Terminal, and the line after `$` is what to type in Terminal. The python script for **Step 4** is saved in wordcount.py.

Launch Terminal on Mac OS and use spark-submit to run the code for **Step 5**:

```
(base) Songyus-MacBook-Pro:~ Daddy$ spark-submit /Users/Daddy/Desktop/HW0/bigram_model.py /Users/Daddy/Desktop/HW0/wiki.txt /Users/Daddy/Desktop/HW0/bigram_count /Users/Daddy/Desktop/HW0/bigram_model
```

This is what I submitted to the Terminal, and the line after `$` is what to type in Terminal. The python script for **Step 5** is saved in bigram_model.py.

### Output files

> **Step 4**:

> > Folder `wordcount`. The actual wordcount result is in `part-00000` inside the folder.

> **Step 5**:

> > Folder `bigram_count` for bigram count. The actual result of the count for all bigram words is in `part-00000` inside the folder.

> > Folder `bigram_model` for conditional bigram distribution. The actual result is in `part-00000` inside the folder.

### How to interpret the output for Step 5

**Bigram count**

The output for bigram count is a list of the bigrams and their corresponding count in `wiki.txt`.

For each line, it's of the form:

((first word of the bigram, second word of the bigram), count of the bigram)
{: .alert .alert-info .text-center}

Here is an example:

(('organization', 'of'), 208)
{: .alert .alert-info .text-center}

The bigram is `'organization of'`, with the first word being `'organization'` and the second word being `'of'`, and that bigram exists in this document for `208` times.

**Conditional bigram distribution**

The output for conditional bigram frequency is a list of the bigrams and their corresponding conditional frequency distributions in `wiki.txt`.

For each line, it's of the form:

((first word of the bigram, second word of the bigram), conditional bigram distribution)
{: .alert .alert-info .text-center}

The conditional bigram distribution is the count of the bigram divided by the count of the first word in this bigram.

Here is an example:

(('three', 'one'), 0.08789033503241452)
{: .alert .alert-info .text-center}

The bigram is `'three one'`, with the first word being `'three'` and the second word being `'one'`, and that if a word `'three'` occurs then there is a 8.78903% chance that the next word is `'one'`.


