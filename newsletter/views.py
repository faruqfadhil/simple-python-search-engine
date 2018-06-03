import pandas
from django.shortcuts import render
from .forms import SearchForm
from .SearchEngine import SearchEngine

def searchform(request):
    global df 
    global model
    #if form is submitted
    if 'query' in request.GET:
        #will handle the request later
        form = SearchForm(request.GET)
 
        #checking the form is valid or not 
        if form.is_valid():
            #if valid rendering new view with values
            #the form values contains in cleaned_data dictionary
            res = model.search(request.GET['query'],page=int(request.GET['page']))
            return render(request, 'searchform.html', {
            'query': res,
            'result':True,
            'form':form,
            'q':request.GET['query'],
            'p':int(request.GET['page']),
            'range': range(10),
            
            })

            # print(form.cleaned_data['query'])
 
    else:
        # data set
        df = pandas.read_csv("/media/faruq/FARUQ/PENS/semester6/datamining/program/django/ClassFormExample/newsletter/newsfeed.csv")
        model = SearchEngine()
        model.fit(df)
        #creating a new form
        form = SearchForm()
        #returning form 
        return render(request, 'searchform.html', {
            'form':form,
            'result':False,
            })