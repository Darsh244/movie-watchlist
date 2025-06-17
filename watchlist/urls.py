from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_view, name='search'),
    path('watchlist/', views.my_watchlist, name='mywatchlist'),
    path('add/<int:tmdb_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/edit/<int:pk>/', views.update_watchlist_item, name='edit_watchlist_item'),
    path('watchlist/delete/<int:pk>/', views.delete_watchlist_item, name='delete_watchlist_item'),
]
