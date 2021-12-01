from django.shortcuts import render

def index(request):
    """The home page for Boardy"""
    return render(request, 'board_games/index.html')
