from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    totalcount = fulltext.split()
    

    wordcountdictionary = {}
    for word in totalcount:
        if word in wordcountdictionary:
            #increase the count
            wordcountdictionary[word] += 1
        else:
            wordcountdictionary[word] = 1
    
    sorted_words = sorted(wordcountdictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'noofwords':len(totalcount),'totalcount':fulltext,'repeatedwordcount':sorted_words })


def about(request):
    return render(request,'about.html')