"""SimpleApp.py"""
from pyspark.sql import SparkSession

spark = SparkSession.builder.remote("sc://localhost").appName("SimpleApp").getOrCreate()

df = spark.range(1000)

df.show()

#df.write.mode("overwrite").parquet("./example")
df.write.mode("overwrite").csv("csv-data")

spark.stop()
