from __future__ import print_function

import sys

from operator import add
from pyspark.sql import SparkSession

inpath = "wasbs://<YOUR_CONTAINER_NAME>@<YOUR_STORAGE_ACCOUNT>.blob.core.windows.net/<INPUT_DIRECTORY>/"
spark = SparkSession.builder.appName("AzureDatabricksWordCount").getOrCreate()

lines = spark.read.text(inpath).rdd.map(lambda r: r[0])

counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)

output = counts.collect()

for (word, count) in output:

    print("%s: %i" % (word, count))



#spark.stop()