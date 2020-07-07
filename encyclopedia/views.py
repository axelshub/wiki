from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, TITLE):
    return render(request, "encyclopedia/entry.html", {
        "entry page": util.get_entry(TITLE)
    })



