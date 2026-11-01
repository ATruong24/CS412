# voter_analytics/views.py
# Description: Handles views to list, filter and show details
# Date: Fall 2026

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Voter
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