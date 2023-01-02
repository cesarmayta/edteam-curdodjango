from django.shortcuts import render

# Create your views here.
def index(request):
    listaArticulos = [
        {
            "titulo":"Mover, copiar y renombrar directorios en Linux",
            "imagen":"https://ed.team/_next/image?url=https%3A%2F%2Fedteam-media.s3.amazonaws.com%2Fblogs%2Foriginal%2F511e1605-3a2a-46ba-a211-ff5d33d6028f.png&w=1920&q=75",
            "autor":"Alvaro Felipe Chávez"
        },
        {
            "titulo":"La ruta para ser programador frontend (Guía completa)",
            "imagen":"https://edteam-media.s3.amazonaws.com/blogs/original/316f4593-d55e-4f67-a15c-f9d91c233ad7.jpg",
            "autor":"Yimmerlys Lopez"
        },
        {
            "titulo":"La ruta para ser programador backend (Guía completa)",
            "imagen":"https://edteam-media.s3.amazonaws.com/blogs/original/a0a6ef1a-855e-4822-a6f5-c72df88927e4.jpg",
            "autor":"Alvaro Felipe Chávez"
        },
    ]
    
    context = {
        "articulos":listaArticulos
    }
    
    return render(request,'blog/index.html',context)
    
    