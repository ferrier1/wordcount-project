from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def test(request):
    return HttpResponse("TEST")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    dict_count = {}
    for word in wordlist:
        if word.isalpha():
            if word in dict_count:
                dict_count[word] += 1
            else:
                dict_count[word] = 1
    sorted_word_list = sorted(dict_count.items(), key=operator.itemgetter(1),
    reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext,
     'sorted_word_list': sorted_word_list, 'word_count': len(wordlist)})


def about(request):
    return render(request, 'about.html')
