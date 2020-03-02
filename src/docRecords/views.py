from django.shortcuts import render
from django import forms
from docRecords.models import NewEntry
from docRecords.forms import NewEntryForm
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,DeleteView, CreateView, UpdateView)


class EntryListView(ListView):
    model = NewEntry
    template_name = 'docEntry/entryList.html'

class EntryCreateView(CreateView):
    model = NewEntry
    form_class = NewEntryForm
    template_name = 'docEntry/createEntry.html'
    success_url = reverse_lazy('docRecords:list-entry')

class EntryDetailView(DetailView):
    model = NewEntry
    template_name = 'docEntry/entrydetail.html'
    slug_field = 'slug'

class EntryUpdateView(UpdateView):
    model = NewEntry
    form_class = NewEntryForm
    template_name = 'docEntry/entryupdate.html'
    slug_field = 'slug'
    success_url = reverse_lazy('docRecords:entry-detail')

class EntryDeleteView(DeleteView):
    model = NewEntry
    form_class = NewEntryForm
    template_name = 'docEntry/entrydelete.html'
    slug_field = 'slug'
    success_url = reverse_lazy('docRecords:list-entry')