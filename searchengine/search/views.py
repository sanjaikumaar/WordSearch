from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from operator import itemgetter
import os
import pandas

def index(request):
	return render(request, 'search/search.html') 

def search(request):

	letters = request.POST.get('search')
	path = os.getcwd()
	df = pandas.read_csv(path+"\\word_search.tsv",header=None, names=['word','rank'], sep='\t')
	df1 = df[df['word'].str.contains(str(letters),na=False)]
	sf = df1.sort_values('rank',ascending=False)
	sf1 = (sf['word'].head(25))
	sl = list(sf1)
	returnvals={'result':sl}
	return HttpResponse(json.dumps(returnvals), content_type='application/json')