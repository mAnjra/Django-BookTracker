from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_title','book_genre','start_date']
        widgets = {'start_date': forms.DateInput(attrs={'type':'date'})}