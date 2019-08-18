from pyspark.sql import SparkSession
import logging

class DataProcessor:
    __instance = None
    @staticmethod
    def getInstance():
        if(DataProcessor.__instance == None):
            DataProcessor()
        return DataProcessor.__instance
    def __init__(self):
        if(DataProcessor.__instance != None):
            raise Exception("This class is a singleton!")
        else:
            self.spark = SparkSession \
            .builder \
            .appName("Python Spark SQL basic example") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
            DataProcessor.__instance = self
            logging.info("Spark session for Data Processor has started.")
    def loadAndProcess(self, keys, values, report_type=1):
        df = self.spark.read.csv(path="DataSources/google-play-store-apps/googleplaystore.csv", header="true")
        rows = df.groupBy("Category").count().collect()
        if(report_type==1):
            for r in rows:
                if(r[1]>400):
                    keys.append(r[0])
                    values.append(r[1])
        else:
            for r in rows:
                if(r[1]>100 and r[1]<300):
                    keys.append(r[0])
                    values.append(r[1])