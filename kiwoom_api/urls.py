from django.urls import path, include
#from .views import show_first, game_start, login, game_attack
from . import views

app_name = 'kiwoom_api'

urlpatterns = [
    path('', view=views.login, name='login'),
    # path('start/', game_start, name='game_start'),
    # path('login/', login, name='login'),
    # path('attack/', view=views.game_attack, name='game_attack'),
    # path('list/', views.game_list, name='game_list'),
    # path('<int:pk>/delete/', views.game_delete, name='game_delete'),
    # path('<int:pk>', views.game_detail, name='game_detail'),
    # path('game/rank/', view=views.game_rank, name='game_rank'),
    # path('<int:pk>/counter/', view=views.counter_start, name='counter_start'),
]
