from django.shortcuts import render

# Create your views here.
def indexCursos(request):
    return render(request,'cursos.html')