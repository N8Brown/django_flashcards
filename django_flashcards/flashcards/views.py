from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def addition(request):
    from random import randint
    num1 = randint(0,10)
    num2 = randint(0,10)

    if request.method == 'POST':
        question_num1 = int(request.POST['question_num1'])
        question_num2 = int(request.POST['question_num2'])
        answer = (request.POST['answer'])
        correct_answer = question_num1 + question_num2

        context = {
            'answer':answer,
            'correct_answer': correct_answer,
            }
        return render(request, 'addition.html', context)

    context = {
        'num1': num1,
        'num2': num2, 
    }

    return render(request, 'addition.html', context)

def subtraction(request):
    return render(request, 'subtraction.html')
    
def multiplication(request):
    return render(request, 'multiplication.html')
    
def division(request):
    return render(request, 'division.html')