from django.shortcuts import render

from .models import ClientDetail
from .forms import ClientDetailForm
def home(request):
    if request.method == "POST":
        form = ClientDetailForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'home.html',{})
    else:
        return render(request,'home.html',{})