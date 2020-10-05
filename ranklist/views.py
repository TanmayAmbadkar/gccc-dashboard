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
import pandas as pd


# Create your views here.

class HomeView(TemplateView):

    template_name = 'ranklist/home.html'

class RanklistDetailView(DetailView):

    model = College

    template_name = 'ranklist/college.html'

    def get_context_data(self, **kwargs):

         context = super(RanklistDetailView, self).get_context_data(**kwargs)
         college = College.objects.get(pk = self.kwargs['pk'])
         data = pd.read_csv(college.results)
         context['college'] = college
         labs, quests = get_results(data, college)

         context['labs']=labs
         context['quests']=quests

         return context

def get_results(data, college):

    labs = data.sort_values(by = ['labs'], ascending=False)[:5]
    quests = data.sort_values(by = ['quests'], ascending=False)[:5]
    i = 1
    lab = []
    for name, labs in zip(labs['Name'], labs['labs']):

        obj, created = LabsPosition.objects.get_or_create(college = college,
                                                 name = name,
                                                 labs = labs,
                                                 position = i)
        i+=1
        lab.append(obj)

    quest = []
    i=1
    for name, quests in zip(quests['Name'], quests['quests']):

        obj, created = QuestPosition.objects.get_or_create(college = college,
                                                 name = name,
                                                 quests = quests,
                                                 position = i)
        i+=1
        quest.append(obj)

    return lab, quest




class CollegeFormView(CreateView):

    template_name = 'ranklist/college_form.html'
    success_url = reverse_lazy('list')
    form_class = CollegeForm
    model = College

class CollegeListView(ListView):

    model = College
    template_name = 'ranklist/college_list.html'

    def get_context_data(self, **kwargs):

         context = super(CollegeListView, self).get_context_data(**kwargs)
         context['colleges'] = College.objects.order_by('-short_name')
         return context
