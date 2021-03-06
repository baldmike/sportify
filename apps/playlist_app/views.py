# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import *

# Create your views here.
def addPlaylist(request):

    return render(request, 'playlist_app/addPlaylist.html')

def createPlaylist(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        playlist_name = request.POST['playlist_name']
        Playlist.objects.create(playlist_name=playlist_name, user_id=user_id)

    return redirect('music_app:index')
    
def viewPlaylist(request, playlist_id):
    context={
        'playlist': Playlist.objects.get(id=playlist_id),
        'additions': Addition.objects.filter(playlist_id=playlist_id)
    }
    return render(request, 'playlist_app/viewPlaylist.html', context)

def addToPlaylist(request, song_id, playlist_id):
    
    playlist= Playlist.objects.get(id=playlist_id)
    song= Song.objects.get(id=song_id)
    Addition.objects.create(playlist=playlist, song=song)
    
    return redirect(reverse('playlist_app:viewPlaylist', kwargs={ 'playlist_id':playlist_id}))


def deletePlaylist(request, playlist_id):
    
    Playlist.objects.delete(playlist_id=playlist_id)

    return redirect(reverse('playlist_app:viewPlaylist', kwargs={ 'playlist_id':playlist_id}))

