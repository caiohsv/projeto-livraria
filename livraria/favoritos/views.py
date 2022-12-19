from django.shortcuts import render, get_object_or_404, redirect
from .models import Favoritos2
from livrariaapp.models import Livros
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required
def addfav(request, livros_id):
    livro =  Livros.objects.get(id=livros_id)
    try:
        fav = Favoritos2.objects.get(user=request.user)
    except Favoritos2.DoesNotExist:
        fav = Favoritos2.objects.create(user=request.user)
    try:
        if livro in fav.livros.all():
            fav.save()
        else:
            fav.livros.add(livro)
            fav.save()
    except Livros.DoesNotExist:
        print('livro nao adicionado')
    return redirect('/')



    