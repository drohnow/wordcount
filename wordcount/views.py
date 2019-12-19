from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    #return HttpResponse('<h1>testing Django</h1>')
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)

    wordlist = fulltext.split()
    print(wordlist)
    print(len(wordlist))

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1

        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)


    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
