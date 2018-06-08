#  coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [  #表示一个视图函数的通用前缀
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
    url(r'^time/$',views.current_datetime,name='current_datetime'),
]