from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def addition(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        context = {
            'answer':answer, 
        }
        return render(request, 'addition.html', context)
    
    return render(request, 'addition.html')

def subtraction(request):
    return render(request, 'subtraction.html')
    
def multiplication(request):
    return render(request, 'multiplication.html')
    
def division(request):
    return render(request, 'division.html')