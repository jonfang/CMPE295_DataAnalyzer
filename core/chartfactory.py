import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from io import BytesIO
import base64

def createBarChart(keys, values, y_label, title, configs = {}):
    y_pos = np.arange(len(keys))
    plt.clf()
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, keys)
    plt.ylabel(y_label)
    plt.title(title)
    if('rotation' in configs):
        plt.xticks(rotation=configs['rotation'])
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()
    return image_base64

def createPieChart(keys, values, title, configs = {}):
    plt.clf()
    explode = []
    for i in range(len(values)):
        explode.append(0)
    explode[0] = 0.1  # only "explode" the largest slide
    plt.pie(values, explode=explode, labels=keys, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    if('rotation' in configs):
        plt.xticks(rotation=configs['rotation'])
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()
    return image_base64