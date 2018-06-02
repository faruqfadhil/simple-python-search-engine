import pandas
from django.shortcuts import render
from .forms import SearchForm
from .SearchEngine import SearchEngine

def searchform(request):
    #if form is submitted
    if request.method == 'POST':
        #will handle the request later
        form = SearchForm(request.POST)
 
        #checking the form is valid or not 
        if form.is_valid():
            #if valid rendering new view with values
            #the form values contains in cleaned_data dictionary
            
            df = pandas.read_csv("/media/faruq/FARUQ/PENS/semester6/datamining/program/django/ClassFormExample/newsletter/newsfeed.csv")
            model = SearchEngine()
            model.fit(df)
            res = model.search(form.cleaned_data['query'])
            return render(request, 'searchform.html', {
            'query': res,
            'result':True,
            'form':form,
            })

            # print(form.cleaned_data['query'])
 
    else:
        #creating a new form
        form = SearchForm()
        #returning form 
        return render(request, 'searchform.html', {
            'form':form,
            'result':False,
            })