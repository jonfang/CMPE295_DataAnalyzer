from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import sum as _sum
from functools import reduce
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
        if(report_type==1):
            df = self.spark.read.csv(path="DataSources/google-play-store-apps/googleplaystore.csv", header="true")
            rows = df.groupBy("Category").count().collect()
            for r in rows:
                if(r[1]>400):
                    keys.append(r[0])
                    values.append(r[1])
        elif(report_type==2):
            df = self.spark.read.csv(path="DataSources/google-play-store-apps/googleplaystore.csv", header="true")
            rows = df.groupBy("Category").count().collect()
            for r in rows:
                if(r[1]>100 and r[1]<300):
                    keys.append(r[0])
                    values.append(r[1])
        elif(report_type==4):
            df2011 = self.spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2011.csv", header="true").select('Incident Type Description')
            df2012 = self.spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2012.csv", header="true").select('Incident Type Description')
            df2013 = self.spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2013.csv", header="true").select('Incident Type Description')
            df2014 = self.spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2014.csv", header="true").select('Incident Type Description')
            df2015 = self.spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2015.csv", header="true").select('Incident Type Description')
            df2016 = self.spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2016.csv", header="true").select('Incident Type Description')
            df = reduce(DataFrame.unionAll, [df2011, df2012, df2013, df2014, df2015, df2016])
            rows = df.groupBy("Incident Type Description").count().orderBy('count', ascending=False).limit(10).collect()
            for r in rows:
                    keys.append(r[0])
                    values.append(r[1])
        elif(report_type==5):
            df = self.spark.read.csv(path="DataSources/india-trade-data/2018-2010_import.csv", header="true")
            df = df.select(df.country, df.value.cast('float').alias('value')).where(df.value.isNotNull())
            df = df.groupBy("country").agg(_sum("value").alias("sum_val"))
            df = df.select(df.country, df.sum_val.cast('int').alias('total')).orderBy('total', ascending=False)
            rows = df.limit(10).collect()
            for r in rows:
                    keys.append(r[0])
                    values.append(r[1])
        elif(report_type==6):
            df = self.spark.read.csv(path="DataSources/india-trade-data/2018-2010_export.csv", header="true")
            df = df.select(df.country, df.value.cast('float').alias('value')).where(df.value.isNotNull())
            df = df.groupBy("country").agg(_sum("value").alias("sum_val"))
            df = df.select(df.country, df.sum_val.cast('int').alias('total')).orderBy('total', ascending=False)
            rows = df.limit(10).collect()
            for r in rows:
                    keys.append(r[0])
                    values.append(r[1])