"""Defines URL patterns for board_games."""

from django.urls import path
from . import views

app_name = 'board_games'
urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    # Page that shows all board games.
    path('all_games/', views.all_games, name='all_games'),
    # Detail page for a specific board game and for borrowing a board game
    path('all_games/<int:board_game_id>/', views.board_game, name='board_game'),
    # Page for adding a new board game
    path('new_board_game/', views.new_board_game, name='new_board_game'),
    # Page for edting a board game
    path('edit_board_game/<int:board_game_id>/', views.edit_board_game, name='edit_board_game'),
    # User's own page, shows users board games
    path('user_page/', views.user_page, name = 'user_page'),
]