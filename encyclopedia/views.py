from django import forms
from django.shortcuts import render
from . import util
import markdown2
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

class NewPageForm(forms.Form):
    title = forms.CharField(label='Title')
    textarea = forms.CharField(label='Text', widget=forms.Textarea)

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def entry(request, title):
    output = util.get_entry(title)
    if output == None:
        return render(request, 'encyclopedia/error.html')
    else:
        entry = markdown2.markdown(output)
        return render(request, 'encyclopedia/entry.html', {
            'entry': entry, # "key that HTML has access to": value that the variable takes on
            'title': title
        })
    
def search(request):
    query = request.GET['q'].lower()
    entries = util.list_entries()
    matches = []

    # Check match
    for title in entries:
        if title.lower() == query:
            return entry(request, title)

    # Check substring
    for title in entries:
        if query in title.lower():
            matches.append(title)
        
    return render(request, 'encyclopedia/search.html', {
        'matches': matches
    })


def create(request):
    show_error = False
    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data['title']
            content = form.cleaned_data['textarea']
            entries = util.list_entries()
            for title in entries:
                if not title.lower() == new_title.lower():
                    util.save_entry(new_title, content)
                    return entry(request, new_title)
                else:
                    show_error = True       
              
    return render(request, 'encyclopedia/create.html', {
    'form': NewPageForm(),
    'error': show_error
    })

def edit(request):
    title = request.POST.get('title')
    content = util.get_entry(title)
    if request.method == 'POST':
        form = NewPageForm(initial={'title': title, 'textarea': content})
        if form.is_valid():
            new_content = form.cleaned_data['textarea']
            util.save_entry(title, new_content)
            return entry(request, title)
            
    return render(request, 'encyclopedia/edit.html', {
        'form': form,
        'entry': entry,
        'title': title
    })
    