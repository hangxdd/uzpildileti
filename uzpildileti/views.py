from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def indexView(request):
    return render(request, 'main/index.html')

def favouriteView(request):
    return render(request, 'main/favourite.html')

def aboutView(request):
    return render(request, 'main/about.html')

def stationView(request):
    return render(request, 'main/station.html')

def loginView(request):
    return render(request, 'registration/login.html')

def registerView(request):
       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')
       else:
           form = UserCreationForm()
       return render(request, 'registration/register.html', {'form': form})
