from pyspark.sql import SparkSession
import os

# https://stackoverflow.com/questions/50963444/failed-to-find-data-source-com-mongodb-spark-sql-defaultsource

def get_spark_session():
    return SparkSession.builder.appName("visualizer") \
        .config("spark.mongodb.read.connection.uri", "mongodb://127.0.0.1:27017/") \
        .config("spark.mongodb.write.connection.uri", "mongodb://127.0.0.1:27017/") \
        .config("spark.mongodb.input.uri", "mongodb://127.0.0.1:27017/") \
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1:27017/") \
        .config('spark.driver.extraClassPath', os.path.join(os.path.abspath(os.path.dirname(__file__)), '../drivers/*')) \
        .getOrCreate()

