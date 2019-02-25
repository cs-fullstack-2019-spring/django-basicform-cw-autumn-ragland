from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account


# render index html
def index(request):
    allAccounts = Account.objects.all()
    context = {
        'allAccounts': allAccounts
    }
    return render(request, 'accountApp/index.html', context)


# display personalized h1 tag
def displayName(request):
    print(request.POST)
    return HttpResponse("<h1>Welcome to " + request.POST['personName'] + "'s Page</h1>")


# add five dollars to  each account checking account (called in html)
def addFive(request, accountID):
    individualAccount = get_object_or_404(Account, pk=accountID)
    individualAccount.checking += 5
    individualAccount.save()
    return redirect('index')
