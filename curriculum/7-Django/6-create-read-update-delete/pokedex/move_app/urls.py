from django.urls import path
from .views import All_moves, A_move

urlpatterns = [
    path("", All_moves.as_view(), name="all_moves"),
    path("<str:name>/", A_move.as_view(), name="a_move"),
]
