from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from ranklist.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from ranklist.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import os

# Create your views here.

class HomeView(TemplateView):

    template_name = 'ranklist/home.html'

class RanklistDetailView(DetailView):

    model = College

    template_name = 'ranklist/college.html'

    def get_context_data(self, **kwargs):

         context = super(RanklistDetailView, self).get_context_data(**kwargs)
         college = College.objects.get(short_name = self.kwargs['pk'])
         context['college'] = college
         if college.results:


             labs = Student.objects.filter(col = college).order_by('-labs')[:20]
             quests = Student.objects.filter(col = college).order_by('stamp').order_by('-quests')[:20]
             quests = list(quests)
             for i in range(len(quests)):
                 for j in range(len(quests)-1):
                     if(quests[j].stamp > quests[j+1].stamp and quests[j].quests == quests[j+1].quests):
                         quest = quests[j]
                         quests[j] = quests[j+1]
                         quests[j+1] = quest


             i=1
             j=1
             lab = labs[0].labs
             quest = quests[0].quests
             for stud1, stud2 in zip(labs, quests):
                 if stud1.labs != lab:
                     lab = stud1.labs
                     i+=1
                 if stud2.quests != quest:
                     quest = stud2.quests
                     j+=1

                 stud1.position_labs = i
                 stud2.position = j
                 stud1.save()
                 stud2.save()

             context['labs']=labs
             context['quests']=quests

         return context


class CollegeFormView(CreateView):

    template_name = 'ranklist/college_form.html'
    success_url = reverse_lazy('list')
    form_class = CollegeForm
    model = College

    def form_valid(self, form):

        form.instance.save()
        data = pd.read_csv(form.instance.csv)
        #college = College.objects.get_or_create(short_name = form.instance.short_name)
        for i in range(len(data)):
            obj = Student.objects.create(col = form.instance, name = data['Name'][i], url = data['URL'][i], quests = 0, labs = 0)
            print(obj)
        scheduler = BackgroundScheduler()
        scheduler.add_job(form.instance.get_results, 'interval', minutes=5)
        scheduler.start()
        print("New job started")

        return super().form_valid(form)

class CollegeListView(ListView):

    model = College
    template_name = 'ranklist/college_list.html'

    def get_context_data(self, **kwargs):

         context = super(CollegeListView, self).get_context_data(**kwargs)
         context['colleges'] = College.objects.order_by('-short_name')
         return context
