from django.shortcuts import redirect, render
from .models import BoardGame
from .forms import BoardGameForm

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

def new_board_game(request):
    """Add a new board game"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BoardGameForm()
    else:
        # POST data submitted; process data.
        form = BoardGameForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:user_page')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'board_games/new_board_game.html', context)
