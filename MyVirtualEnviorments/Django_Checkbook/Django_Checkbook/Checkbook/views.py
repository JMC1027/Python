from django.shortcuts import render

def home(request):
    return render(request, 'checkbook/index.html')

def create_account(request):
    return render(request, 'checkbook/CreateNewAccount.html')

def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')

def transaction(request):
    return render(request, 'checkbook/AddTransaction.html')
