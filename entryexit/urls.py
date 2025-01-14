
from django.contrib import admin
from django.urls import include, path
from enter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.library, name='library'),
    path('/', views.library, name='library'),
    path('home', views.library, name='library'),
    path('home/', views.library, name='library'),
    path('records_today', views.records_today, name='records_today'),
    path('records_today/', views.records_today, name='records_today'),
    path('library', views.library, name='library'),
    path('library/', views.library, name='library'),
    path('records', views.records, name='records'),
    path('records/', views.records, name='records'),
    path('allrecords', views.allrecords, name='allrecords'),
    path('allrecords/', views.allrecords, name='allrecords'),
    path('recordsbystatus', views.recordsbystatus, name='recordsbystatus'),
    path('recordsbystatus/', views.recordsbystatus, name='recordsbystatus'),
    path('export', views.export, name='export'),
    path('export/', views.export, name='export'),
    path('exportbydate', views.exportbydate, name='exportbydate'),
    path('exportbydate/', views.exportbydate, name='exportbydate'),
    path('recordsbymonth', views.recordsbymonth, name='recordsbymonth'),
    path('recordsbymonth/', views.recordsbymonth, name='recordsbymonth'),
    path('exportbymonth', views.exportbymonth, name='exportbymonth'),
    path('exportbymonth/', views.exportbymonth, name='exportbymonth'),
    path('shifts', views.shifts, name='shifts'),
    path('shifts/', views.shifts, name='shifts'),
    path('statistics', views.statistics, name='statistics'),
    path('statistics/', views.statistics, name='statistics'),
    path('get_reader_data', views.get_reader_data),
]
