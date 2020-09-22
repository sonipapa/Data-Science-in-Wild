# Construct bigram model with conditional probabilities
# create a Spark context
import sys
 
from pyspark import SparkContext, SparkConf
 
conf = SparkConf()
sc = SparkContext(conf=conf)

# Read data from text file and split each line into words
words = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))
	
# Now count the occurrence of each word
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)


# Read data from text file and split into words and form bigram tuples
bigrams = sc.textFile(sys.argv[1]).map(lambda line: line.split(" ")) \
		.flatMap(lambda x: ((x[i],x[i+1]) for i in range(0,len(x)-1)))

# Now count the occurrence of each bigram
bigramCounts = bigrams.map(lambda x: (x, 1)).reduceByKey(lambda a,b:a +b)

# save the bigram count output to another text file
bigramCounts.coalesce(1, shuffle=True).saveAsTextFile(sys.argv[2])


# Let the starting word of each bigram be the key
bigramMatch = bigramCounts.map(lambda x: (x[0][0], x))

# join each bigram with the count of its starting word
bigramJoin = bigramMatch.join(wordCounts)

# Find the conditional probability for each bigram
bigramProb = bigramJoin.map(lambda x: (x[1][0][0], x[1][0][1]/x[1][1]))

# save the conditional bigram probability output to another text file
bigramProb.coalesce(1, shuffle=True).saveAsTextFile(sys.argv[3])
sc.stop()