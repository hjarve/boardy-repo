from django.shortcuts import redirect, render
from .models import BoardGame, Loan
from .forms import BoardGameForm, LoanForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """The home page for Boardy"""
    games = BoardGame.objects.all().order_by('name')
    first_5 = games[:5]
    context = {'first_5': first_5}
    return render(request, 'board_games/index.html', context)

def all_games(request):
    """Show all board games"""
    # Board games sorted by their names
    games = BoardGame.objects.order_by('name')
    context = {'games': games}
    return render(request, 'board_games/all_games.html', context)

@login_required
def user_page(request):
    # User's own page; shows user's board games and the board games the user has borrowed
    users_board_games = BoardGame.objects.filter(owner=request.user).order_by('name')
    users_loans = Loan.objects.filter(borrower = request.user).order_by('-date_added')
    context = {'users_board_games': users_board_games, 'users_loans': users_loans}
    return render(request, 'board_games/user_page.html', context)

@login_required
def board_game(request, board_game_id):
    """Show the details of a specific board game and who has borrowed it."""
    board_game = BoardGame.objects.get(id=board_game_id)
    loans = board_game.loan_set.order_by('-date_added')
    context = {'board_game': board_game, 'loans': loans}
    return render(request, 'board_games/board_game.html', context)

@login_required
def new_board_game(request):
    """Add a new board game"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BoardGameForm()
    else:
        # POST data submitted; process data.
        form = BoardGameForm(data = request.POST)
        if form.is_valid():
            new_board_game = form.save(commit=False)
            new_board_game.owner = request.user
            new_board_game.save()
            return redirect('board_games:user_page')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'board_games/new_board_game.html', context)

@login_required
def edit_board_game(request, board_game_id):
    """Edit a board game."""
    board_game = BoardGame.objects.get(id = board_game_id)
    # Make sure the board game belongs to the current user.
    if board_game.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current data.
        form = BoardGameForm(instance=board_game)
    else:
        # POST data submitted; process data.
        form = BoardGameForm(instance=board_game, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:user_page')

    context = {'board_game': board_game, 'form': form}
    return render(request, 'board_games/edit_board_game.html', context)

@login_required
def borrow_game(request, board_game_id):
    """Place a new loan on a game"""
    board_game = BoardGame.objects.get(id = board_game_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = LoanForm()
    else:
        # POST data submitted; process data.
        form = LoanForm(data = request.POST)
        if form.is_valid():
            borrow_game = form.save(commit=False)
            borrow_game.board_game = board_game
            borrow_game.borrower = request.user
            borrow_game.owner = board_game.owner
            borrow_game.save()
            return redirect('board_games:user_page')

    #Display a blank or invalid form.
    context = {'board_game': board_game,'form': form}
    return render(request, 'board_games/borrow_game.html', context)

@login_required
def edit_loan(request, loan_id):
    """Edit a loan (return the game)."""
    loan = Loan.objects.get(id = loan_id)
    # Make sure the loan belongs to the current borrower.
    if loan.borrower != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current data.
        form = LoanForm(instance=loan)
    else:
        # POST data submitted; process data.
        form = LoanForm(instance=loan, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:user_page')

    context = {'loan': loan, 'form': form}
    return render(request, 'board_games/edit_loan.html', context)