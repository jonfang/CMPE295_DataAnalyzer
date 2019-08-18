import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession


objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
# plt.figure(figsize=(20,10))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()

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