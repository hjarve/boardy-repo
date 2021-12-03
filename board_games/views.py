from django.shortcuts import render
from .models import BoardGame

def index(request):
    """The home page for Boardy"""
    return render(request, 'board_games/index.html')

def board_games(request):
    """Show all board games"""
    # Board games sorted by their names
    board_games = BoardGame.objects.order_by('name')
    context = {'board_games': board_games}
    return render(request, 'board_games/board_games.html', context)

def board_game(request, board_game_id):
    """Show the details of a specific board game and who has borrowed it."""
    board_game = BoardGame.objects.get(id = board_game_id)
    loans = board_game.loan_set.order_by('-date_added')
    context = {'board_game': board_game, 'loans': loans}
    return render(request, 'board_games/board_game.html', context)
