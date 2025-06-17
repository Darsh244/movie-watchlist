from django import forms
from .models import WatchlistItem

class WatchlistItemForm(forms.ModelForm):
    class Meta:
        model = WatchlistItem
        fields = ['rating', 'notes', 'watched']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Add your notes...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
    