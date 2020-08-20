from django.http import HttpResponse
from django.shortcuts import render

# here are the functions that send you to the url you've specified


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return render(request, 'count.html', {'fulltext':fulltext,
                    'count':len(word_list), 'word_dict':word_dict.items()})

