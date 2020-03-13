from django.shortcuts import render
import numpy as np
import pickle
from .forms import *

path = 'regressor/models/pickle_model.pkl'
# Create your views here.


def Predict(request):
    form = InputArray(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        with open(path,'rb') as model_pk1:
            model = pickle.load(model_pk1)
            int1 = form.cleaned_data["int1"]
            int2 = form.cleaned_data["int2"]
            int3 = form.cleaned_data["int3"]
            int4 = form.cleaned_data["int4"]
            int5 = form.cleaned_data["int5"]
            array = np.array([[int1,int2,int3,int4,int5]])
            print(array)
            print( model.predict(array))
            context = {
                'value':model.predict(array)
            }
    else:
        context["form"] = InputArray(request.POST or None)

    return render(request,'predict.html',context)

