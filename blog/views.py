from django.shortcuts import render

# Create your views here.
from django.template import  Context
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
def index(request):    #创建一个 index的视图函数
    return HttpResponse("HELLO WORD")

def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question %s "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s."%question_id)

def current_datetime(request):
    now = datetime.datetime.now()

    return render_to_response('qianduan.html',{'current_date':now})