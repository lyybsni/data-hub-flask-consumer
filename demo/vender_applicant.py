import datetime
import threading
import time

import schedule
from pyspark.sql.dataframe import DataFrame

from demo.spark_configurer import get_spark_session

counts = [0]
count_diff = []
count_diff_txn = []


# call the defined API in data-hub service, pulling the data
def update_cron():
    schedule.every(10).seconds.do(update_count)

    worker_thread = threading.Thread(target=worker_main)
    worker_thread.start()


def worker_main():
    while True:
        schedule.run_pending()
        time.sleep(1)


def get_count_diff():
    return count_diff


def get_count_txn():
    return count_diff_txn


def update_count():
    count_new = update_from_data_hub().count()
    count_diff.append(count_new - counts[-1])
    counts.append(count_new)
    count_diff_txn.append(datetime.datetime.now())
    print(count_new, count_diff, counts)


def update_from_data_hub() -> DataFrame:
    session = get_spark_session()
    return session.getActiveSession() \
        .read \
        .format("com.mongodb.spark.sql.DefaultSource") \
        .option("database", "datahub") \
        .option("collection", "applications") \
        .load()
    # print(streaming_data_frame.show())
    # data_stream_writer = streaming_data_frame.write \
    # .trigger(continuous="1 second").format("memory") \
    # .option("checkpointLocation", "/tmp/checkpointDir") \
    # .outputMode("append")


class ApplicantVisualizer:
    def __init__(self, labels, data):
        self.labels = labels
        self.data = data

    def get_labels(self):
        return self.labels

    def get_data(self):
        return self.data

    def set_labels(self, labels):
        self.labels = labels

    def set_data(self, data):
        self.data = data
