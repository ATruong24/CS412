# voter_analytics/views.py
# Description: Handles views to list, filter and show details
# Date: Fall 2026

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Voter
from django.db.models import Count
from django.db.models.functions import ExtractYear
import plotly
import plotly.graph_objs as go
import time
import random

ELECTIONS = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']

class VoterListView(ListView):
    '''View to display filterable list of voters'''

    template_name = 'voter_analytics/voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        '''Return the Voters that match whichever filters were submitted.'''

        voters = super().get_queryset().order_by('last_name', 'first_name')
        get = self.request.GET

        party = get.get('party')
        if party:
            voters = voters.filter(party_affiliation=party)

        min_dob = get.get('min_dob')
        if min_dob:
            voters = voters.filter(date_of_birth__year__gte=int(min_dob))

        max_dob = get.get('max_dob')
        if max_dob:
            voters = voters.filter(date_of_birth__year__lte=int(max_dob))

        voter_score = get.get('voter_score')
        if voter_score:
            voters = voters.filter(voter_score=int(voter_score))

        for election in ELECTIONS:
            if election in get:
                voters = voters.filter(**{election: True})

        return voters

    def get_context_data(self, **kwargs):
        '''Add the forms choices'''

        context = super().get_context_data(**kwargs)

        context['parties'] = (Voter.objects.values_list('party_affiliation', flat=True).distinct().order_by('party_affiliation'))
        context['years'] = [str(d.year) for d in Voter.objects.dates('date_of_birth', 'year')]
        context['scores'] = [str(s) for s in range(0, 6)]
        context['elections'] = ELECTIONS
        context['selected'] = self.request.GET
        params = self.request.GET.copy()
        params.pop('page', None)
        context['filter_params'] = params.urlencode()

        return context


class VoterDetailView(DetailView):
    '''Show all fields of one voter'''

    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'v'

class GraphsListView(VoterListView):
    '''View to show graphs of voter data'''

    template_name = 'voter_analytics/graphs.html'
    paginate_by = None   

    def get_context_data(self, **kwargs):
        '''Build plotly graphs of the filtered voters'''

        context = super().get_context_data(**kwargs)
        voters = self.object_list
        total = voters.count()

        # Bar chart: istribution of voters by year of birth
        by_year = (voters.annotate(year=ExtractYear('date_of_birth'))
                         .values('year')
                         .annotate(count=Count('id'))
                         .order_by('year'))
        x = [row['year'] for row in by_year]
        y = [row['count'] for row in by_year]
        fig = go.Bar(x=x, y=y)
        title_text = f'Voter distribution by year of birth (n={total})'
        context['graph_div_birth_year'] = plotly.offline.plot(
            {'data': [fig], 'layout_title_text': title_text},
            auto_open=False, output_type='div')

        # Pie chart: distribution of voters by party affiliation
        by_party = (voters.values('party_affiliation')
                          .annotate(count=Count('id'))
                          .order_by('party_affiliation'))
        x = [row['party_affiliation'] for row in by_party]
        y = [row['count'] for row in by_party]
        fig = go.Pie(labels=x, values=y)
        title_text = f'Voter distribution by party affiliation (n={total})'
        context['graph_div_party'] = plotly.offline.plot(
            {'data': [fig], 'layout_title_text': title_text},
            auto_open=False, output_type='div')

        # Bar chart: how many voters participated in each election
        x = ELECTIONS
        y = [voters.filter(**{election: True}).count() for election in ELECTIONS]
        fig = go.Bar(x=x, y=y)
        title_text = f'Vote count by election (n={total})'
        context['graph_div_elections'] = plotly.offline.plot(
            {'data': [fig], 'layout_title_text': title_text},
            auto_open=False, output_type='div')

        return context