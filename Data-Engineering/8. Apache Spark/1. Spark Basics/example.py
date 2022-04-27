import sys
import pyspark
from pyspark import SparkConf
 
if __name__ == "__main__":
 
    # create Spark context with Spark configuration
    conf = SparkConf().setAppName("Word Count - Python").setMaster('local[*]')
    session = pyspark.sql.SparkSession.builder.config(conf=conf).getOrCreate()

    # read in text file and split each document into words
    rddDistributedFile = session.sparkContext.textFile("lorem.txt")
    rddDistributedFile = rddDistributedFile.cache()
    # count the occurrence of each word
    print(rddDistributedFile.flatMap(lambda text: text.split()).countByValue())