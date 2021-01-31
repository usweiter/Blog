from django.shortcuts import render
from django.contrib.postgres.search import TrigramSimilarity
from .forms import FormSearch
from post.models import ModelPost

def search(request):
    form_search = FormSearch()
    query = None
    results = []

    if 'query' in request.GET:
        form_search = FormSearch(request.GET)

        if form_search.is_valid():
            query = form_search.cleaned_data['query']

            results = ModelPost.issued.annotate(
                similarity=TrigramSimilarity('title', query)+TrigramSimilarity('text', query))\
            .filter(similarity__gt=0.2).order_by('-similarity')

    return render(request, 'search/search.html', {
        'form_search':form_search,
        'query':query,
        'results':results,
        })