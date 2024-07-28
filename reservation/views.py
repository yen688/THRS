from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'reservation/index.html')

def rule(request):
    return render(request, 'reservation/rule.html')
