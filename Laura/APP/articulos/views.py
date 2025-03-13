from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia

def crear_noticia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        resumen = request.POST.get('resumen')
        detalle = request.POST.get('detalle')
        foto = request.FILES.get('foto')
        publicada = request.POST.get('publicada') == 'on'

        noticia = Noticia(
            titulo=titulo,
            resumen=resumen,
            detalle=detalle,
            foto=foto,
            publicada=publicada
        )
        noticia.save()
        return redirect('lista_noticias')  # Redirige a la lista de noticias

    return render(request, 'noticias/crear_noticias.html')



def lista_noticias(request):
    noticias = Noticia.objects.filter(publicada=True).order_by('-fecha_publicacion')
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id, publicada=True)
    return render(request, 'noticias/detalle_noticia.html', {'noticia': noticia})
