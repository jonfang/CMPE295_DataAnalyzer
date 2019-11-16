from django.http import HttpResponse
from pyspark.sql import SparkSession
from django.shortcuts import render
from datetime import datetime

from core.chartfactory import createBarChart, createPieChart
from core.dataprocessor import DataProcessor


def home(request):
    """
    sample python report
    """
    keys = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    values = [10,8,6,4,2,1]
    image_base64 = createBarChart(keys, values, 'Usage', 'Programming language usages')
    return render(
        request,
        'analyzer/layout.html',
        # {
        #     'name': "Jon",
        #     'date': datetime.now(),
        #     'image_base64':image_base64,
        # }
    )
#google play app report 1
def report1(request):
    keys = []
    values = []
    DataProcessor.getInstance().loadAndProcess(keys, values, report_type=1)
    image_base64 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category > 400')
    return render(
        request,
        'analyzer/main.html',
        {
            'name': "Jon",
            'date': datetime.now(),
            'image_base64':image_base64,
        }
    )
#google play app report 2
def report2(request):
        keys = []
        values = []
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=2)
        config = {'rotation':90}
        image_base64 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category < 400', configs=config)
        return render(
            request,
            'analyzer/main.html',
            {
                'name': "Jon",
                'date': datetime.now(),
                'image_base64':image_base64,
            }
        )
#google play app report 3
def report3(request):
        keys = []
        values = []
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=1)
        image_base64 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category > 400 ')
        keys.clear()
        values.clear()
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=2)
        config = {'rotation':90}
        image_base64_1 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category < 400', configs=config)
        return render(
            request,
            'analyzer/main1.html',
            {
                'name': "Jon",
                'date': datetime.now(),
                'image_base64':image_base64,
                'image_base64_1':image_base64_1,
            }
        )

def report4(request):
        keys = []
        values = []
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=4)
        image_base64 = createPieChart(keys, values, 'Oakland Crime Rate 2011-2016')
        keys.clear()
        values.clear()
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=4)
        config = {'rotation':90}
        image_base64_1 = createBarChart(keys, values, 'Count', 'Oakland Crime Rate 2011-2016', configs=config)
        return render(
            request,
            'analyzer/main1.html',
            {
                'name': "Jon",
                'date': datetime.now(),
                'image_base64':image_base64,
                'image_base64_1':image_base64_1,
            }
        )

def report5(request):
        keys = []
        values = []
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=5)
        image_base64 = createPieChart(keys, values, 'India trade import 2010-2018')
        keys.clear()
        values.clear()
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=5)
        config = {'rotation':90}
        image_base64_1 = createBarChart(keys, values, 'Total(millions $USD)', 'India trade import 2010-2018', configs=config)
        return render(
            request,
            'analyzer/main1.html',
            {
                'name': "Jon",
                'date': datetime.now(),
                'image_base64':image_base64,
                'image_base64_1':image_base64_1,
            }
        )
def report6(request):
        keys = []
        values = []
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=6)
        image_base64 = createPieChart(keys, values, 'India trade export 2010-2018')
        keys.clear()
        values.clear()
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=6)
        config = {'rotation':90}
        image_base64_1 = createBarChart(keys, values, 'Total(millions $USD)', 'India trade export 2010-2018', configs=config)
        return render(
            request,
            'analyzer/main1.html',
            {
                'name': "Jon",
                'date': datetime.now(),
                'image_base64':image_base64,
                'image_base64_1':image_base64_1,
            }
        )