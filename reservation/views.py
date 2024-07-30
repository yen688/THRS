from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'reservation/index.html')

def rule(request):
    return render(request, 'reservation/rule.html')

def confirmForm(request):
    return render(request, 'reservation/confirmForm.html')

def confirm(request):
    if request.method == 'POST':
        customer = request.POST.get('customer')
        phone = request.POST.get('phone')
    return render(request, 'reservation/index.html')
