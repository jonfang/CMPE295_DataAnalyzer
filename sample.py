import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import sum as _sum
from functools import reduce

#Basic sample
# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,1]
# # plt.figure(figsize=(20,10))
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
# plt.show()

#Basic spark sample
# spark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()
# df = spark.read.csv(path="DataSources/google-play-store-apps/googleplaystore.csv", header="true")
# rows = df.groupBy("Category").count().collect()
# keys = []
# values = []
# for r in rows:
#     if(r[1]>400):
#         keys.append(r[0])
#         values.append(r[1])
# y_pos = np.arange(len(keys))

# plt.bar(y_pos, values, align='center', alpha=0.5)
# plt.xticks(y_pos, keys)
# plt.ylabel('App Count')
# plt.title('Google Play App Store Count By Category')

# plt.show()

#Spark sample top ranking apps
# spark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()
# df = spark.read.csv(path="DataSources/google-play-store-apps/googleplaystore.csv", header="true")
# df.sort(df.Installs.desc()).show()
# df.show()
# print(df.count())

# Spark india trade
keys = []
values = []
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
df = spark.read.csv(path="DataSources/india-trade-data/2018-2010_import.csv", header="true")
df = df.select(df.country, df.value.cast('float').alias('value')).where(df.value.isNotNull())
df = df.groupBy("country").agg(_sum("value").alias("sum_val"))
df = df.select(df.country, df.sum_val.cast('int').alias('total')).orderBy('total', ascending=False)
rows = df.limit(10).collect()
for r in rows:
        keys.append(r[0])
        values.append(r[1])
explode = []
for i in range(len(values)):
    explode.append(0)
explode[0] = 0.1  # only "explode" the largest slide
fig1, ax1 = plt.subplots()
ax1.pie(values, explode=explode, labels=keys, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#Spark oakland crime rate
# keys = []
# values = []
# spark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()
# df2011 = spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2011.csv", header="true").select('Incident Type Description')
# df2012 = spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2012.csv", header="true").select('Incident Type Description')
# df2013 = spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2013.csv", header="true").select('Incident Type Description')
# df2014 = spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2014.csv", header="true").select('Incident Type Description')
# df2015 = spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2015.csv", header="true").select('Incident Type Description')
# df2016 = spark.read.csv(path="DataSources/oakland-crime-statistics-2011-to-2016/records-for-2016.csv", header="true").select('Incident Type Description')
# df = reduce(DataFrame.unionAll, [df2011, df2012, df2013, df2014, df2015, df2016])
# rows = df.groupBy("Incident Type Description").count().orderBy('count', ascending=False).limit(10).collect()
# for r in rows:
#         keys.append(r[0])
#         values.append(r[1])
# explode = []
# for i in range(len(values)):
#     explode.append(0)
# explode[0] = 0.1  # only "explode" the largest slide
# fig1, ax1 = plt.subplots()
# ax1.pie(values, explode=explode, labels=keys, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# sizes.sort(reverse=True)
# explode = (0.1, 0.0, 0, 0)  # only "explode" the largest slide

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()