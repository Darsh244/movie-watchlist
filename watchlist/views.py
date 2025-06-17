from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from .models import Movie, Watchlist, WatchlistItem
from .forms import WatchlistItemForm
import requests

def home(request):
    return render(request, 'watchlist/home.html')

def search_movies_tmdb(query):
    api_key = settings.TMDB_API_KEY
    url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': api_key,
        'query': query,
        'include_adult': False,
        'language': 'en-US',
        'page': 1,
    }
    response = requests.get(url, params=params)
    data = response.json()
    movies = []
    for item in data.get('results', []):
        movies.append({
            'title': item['title'],
            'year': item.get('release_date', '')[:4],
            'poster': f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get('poster_path') else '',
            'tmdb_id': item['id']
        })
    return movies

def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = search_movies_tmdb(query)
    return render(request, 'watchlist/search.html', {'results': results})


def fetch_tmdb_movie(tmdb_id):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    return {
        'tmdb_id': data['id'],
        'title': data['title'],
        'release_year': data.get('release_date', '')[:4],
        'poster': f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data.get('poster_path') else '',
    }



@login_required
def add_to_watchlist(request, tmdb_id):
    movie_data = fetch_tmdb_movie(tmdb_id)
    if not movie_data:
        return redirect('search')

    movie, created = Movie.objects.get_or_create(
        tmdb_id=movie_data['tmdb_id'],
        defaults={
            'title': movie_data['title'],
            'release_year': movie_data['release_year'],
            'poster': movie_data['poster'],
        }
    )

    watchlist, _ = Watchlist.objects.get_or_create(user=request.user)
    watchlist.movies.add(movie)
    return redirect('mywatchlist')

@login_required
def my_watchlist(request):
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    items = WatchlistItem.objects.filter(watchlist=watchlist).select_related('movie')

    if request.method == 'POST':
        for item_id, position in enumerate(request.POST.getlist('order[]')):
            WatchlistItem.objects.filter(id=position, watchlist=watchlist).update(position=item_id)
        return JsonResponse({'status': 'ok'})

    return render(request, 'watchlist/watchlist.html', {'items': items})


@login_required
def update_watchlist_item(request, pk):
    item = get_object_or_404(WatchlistItem, pk=pk, watchlist__user=request.user)
    if request.method == 'POST':
        form = WatchlistItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('mywatchlist')
    else:
        form = WatchlistItemForm(instance=item)
    return render(request, 'watchlist/edit_item.html', {'form': form, 'item': item})

@login_required
def delete_watchlist_item(request, pk):
    item = get_object_or_404(WatchlistItem, pk=pk, watchlist__user=request.user)
    item.delete()
    return redirect('mywatchlist')