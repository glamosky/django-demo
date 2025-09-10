from django import forms
from .models import LibraryBook


class LibraryBookForm(forms.ModelForm):
    class Meta:
        model = LibraryBook
        fields = ['title', 'author', 'isbn', 'is_checked_out', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '13-digit ISBN'}),
            'is_checked_out': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
    
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if isbn and (not isbn.isdigit() or len(isbn) != 13):
            raise forms.ValidationError("ISBN must be exactly 13 digits")
        return isbn
    
    def clean(self):
        cleaned_data = super().clean()
        is_checked_out = cleaned_data.get('is_checked_out')
        due_date = cleaned_data.get('due_date')
        
        if is_checked_out and not due_date:
            raise forms.ValidationError("Due date is required when book is checked out")
        if not is_checked_out and due_date:
            raise forms.ValidationError("Due date should not be set when book is not checked out")
        
        return cleaned_data
