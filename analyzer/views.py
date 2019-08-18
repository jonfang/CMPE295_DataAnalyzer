from django.http import HttpResponse
from pyspark.sql import SparkSession
from django.shortcuts import render
from datetime import datetime

from core.chartfactory import createBarChart
from core.dataprocessor import DataProcessor


def home(request):
    keys = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    values = [10,8,6,4,2,1]
    image_base64 = createBarChart(keys, values, 'Usage', 'Programming language usages')
    return render(
        request,
        'analyzer/main.html',
        {
            'name': "Jon",
            'date': datetime.now(),
            'image_base64':image_base64,
        }
    )

def report1(request):
    keys = []
    values = []
    DataProcessor.getInstance().loadAndProcess(keys, values)
    image_base64 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category')
    return render(
        request,
        'analyzer/main.html',
        {
            'name': "Jon",
            'date': datetime.now(),
            'image_base64':image_base64,
        }
    )

def report2(request):
        keys = []
        values = []
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=2)
        config = {'rotation':90}
        image_base64 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category', configs=config)
        return render(
            request,
            'analyzer/main.html',
            {
                'name': "Jon",
                'date': datetime.now(),
                'image_base64':image_base64,
            }
        )

def report3(request):
        keys = []
        values = []
        DataProcessor.getInstance().loadAndProcess(keys, values)
        image_base64 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category')
        keys.clear()
        values.clear()
        DataProcessor.getInstance().loadAndProcess(keys, values, report_type=2)
        config = {'rotation':90}
        image_base64_1 = createBarChart(keys, values, 'App Count', 'Google Play App Store Count By Category', configs=config)
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