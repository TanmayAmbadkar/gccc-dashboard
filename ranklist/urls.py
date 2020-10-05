from django.urls import path
from ranklist.views import *
from django.conf.urls import include

urlpatterns = [

    path('<int:pk>', RanklistDetailView.as_view(), name = 'college'),
    path('', HomeView.as_view(), name = 'home'),
    path('forms', CollegeFormView.as_view(), name = 'form'),
    path('colleges', CollegeListView.as_view(), name = 'list'),
    




]
