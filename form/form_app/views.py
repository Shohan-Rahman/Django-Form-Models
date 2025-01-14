from django.shortcuts import render
from . forms import contactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    # return render(request, 'about.html')
    if request.method == 'POST':
        name = request.POST.get('userName')
        email = request.POST.get('email')
        return render(request, 'about.html', {'name' : name, 'email' : email})
    else:
        return render(request, 'about.html')

def submit(request):
    return render(request, 'form.html')

def contact(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'contact.html', {'form' : form})