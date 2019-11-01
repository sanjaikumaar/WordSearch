from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from operator import itemgetter
import os
import pandas

def index(request):
	return render(request, 'search/search.html') 

def search(request):
	result=[]
	letters = request.GET.get('search')
	path = os.getcwd()
	df = pandas.read_csv(path+"\\word_search.tsv",header=None, names=['word','rank'], sep='\t')
	df1=df['word'].str.startswith(str(letters),na=False)
	bs = df[df1]
	sl = bs.sort_values('rank',ascending=False)
	fl = sl['word']
	result.extend(list(fl.head(25)))
	if len(result)<25:
		count = 25 - int(len(result))
		df2 = df[df['word'].str.contains(str(letters),na=False)]
		sf = df2.sort_values('rank',ascending=False)
		sf1 = (sf['word'].head(int(count)))
		result.extend(list(sf1))
	unique_list=list(set(result))
	sorted_list=sorted(unique_list,key=len)
	returnvals={'result':sorted_list}
	return HttpResponse(json.dumps(returnvals), content_type='application/json')