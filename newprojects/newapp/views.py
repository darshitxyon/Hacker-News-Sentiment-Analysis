from django.db.models import Q
from django.shortcuts import render
import requests
from aylienapiclient import textapi
from django.views.generic import TemplateView, ListView

# Create your views here.
from newapp.models import News


class HomePageView(TemplateView):
    template_name = 'newapp/home.html'


class SearchResultsView(ListView):
    model = News
    template_name = 'newapp/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = News.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


# def article_overview(request):
#     search_term = ''
#
#     if 'search' in request.GET:
#         search_term = request.GET['search']
#         articles = News.objects.all().filter(feeder__icontains=search_term)
#
#     return render(request, 'newapp/search_results.html', {'object_list': articles, 'search_term': search_term})


def home(request):
    result1 = {}
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    request.session['topdata'] = response.json()
    result = request.session['topdata'][0:25]
    client = textapi.Client("88f165f7", "7a3f743c0e8a7ccc1f881f5d5c6ca245")
    count = 25
    for story in result:
        response1 = requests.get('https://hacker-news.firebaseio.com/v0/item/%s.json' % story)
        print(response1.json())
        request.session['topdata'] = response1.json()
        sentiment = client.Sentiment({'text': request.session['topdata']['title']})
        request.session['topdata']['polarity'] = sentiment['polarity']

        news_instance = News(by=request.session['topdata']['by'],
                             title=request.session['topdata']['title'],
                             points=request.session['topdata']['score'],
                             #comments=request.session['topdata']['descendants'],
                             sentiment=request.session['topdata']['polarity'])
        news_instance.save()
        result1[story] = request.session['topdata']
        count = count - 1
        if count < 0:
            break
    return render(request, 'newapp/home.html', {'result': result, 'result1': result1})
    # })
