from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def example(response):
    return HttpResponse("hello world!!")


def example2(response, question_id):
    return HttpResponse("ok!")
