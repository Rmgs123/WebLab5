from django.urls import path
from .views import (
    create_lobby_view, join_lobby_view, select_game_view, start_view, dissolve_view,
    sudoku_start, sudoku_check,
    japanese_crossword_start, japanese_crossword_check,
    rps_move_view, rps_state_view, get_rps_result, lobby_state_view, generate_lobby_code # новые эндпоинты
)

urlpatterns = [
    path('sudoku/start/', sudoku_start, name='sudoku_start'),
    path('sudoku/check/', sudoku_check, name='sudoku_check'),
    path('japaneseCrossword/start/', japanese_crossword_start, name='japanese_crossword_start'),
    path('japaneseCrossword/check/', japanese_crossword_check, name='japanese_crossword_check'),

    path('create', create_lobby_view, name='create_lobby'),
    path('join', join_lobby_view, name='join_lobby'),
    path('selectGame', select_game_view, name='select_game'),
    path('start', start_view, name='start_game'),
    path('dissolve', dissolve_view, name='dissolve_game'),

    # эндпоинты для RPS (двух игроков)
    path('rps/move', rps_move_view, name='rps_move'),
    path('rps/state', rps_state_view, name='rps_state'),
    path('state', rps_state_view, name='lobby_state'),
]