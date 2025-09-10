from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import LibraryBook
from .serializers import LibraryBookSerializer, LibraryBookCreateSerializer
from .forms import LibraryBookForm
from datetime import datetime, timedelta


# REST API Views
class LibraryBookViewSet(viewsets.ModelViewSet):
    queryset = LibraryBook.objects.all()
    serializer_class = LibraryBookSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return LibraryBookCreateSerializer
        return LibraryBookSerializer
    
    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        """Check out a book"""
        book = self.get_object()
        if book.is_checked_out:
            return Response(
                {'error': 'Book is already checked out'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Set due date to 14 days from now
        book.is_checked_out = True
        book.due_date = datetime.now() + timedelta(days=14)
        book.save()
        
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        """Return a book"""
        book = self.get_object()
        if not book.is_checked_out:
            return Response(
                {'error': 'Book is not checked out'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        book.is_checked_out = False
        book.due_date = None
        book.save()
        
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available books (not checked out)"""
        available_books = LibraryBook.objects.filter(is_checked_out=False)
        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def checked_out(self, request):
        """Get all checked out books"""
        checked_out_books = LibraryBook.objects.filter(is_checked_out=True)
        serializer = self.get_serializer(checked_out_books, many=True)
        return Response(serializer.data)


# Web Views
def book_list(request):
    """Display all books"""
    books = LibraryBook.objects.all()
    return render(request, 'student/book_list.html', {'books': books})


def book_detail(request, pk):
    """Display book details"""
    book = get_object_or_404(LibraryBook, pk=pk)
    return render(request, 'student/book_detail.html', {'book': book})


def book_create(request):
    """Create a new book"""
    if request.method == 'POST':
        form = LibraryBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book_list')
    else:
        form = LibraryBookForm()
    return render(request, 'student/book_form.html', {'form': form, 'title': 'Create Book'})


def book_update(request, pk):
    """Update a book"""
    book = get_object_or_404(LibraryBook, pk=pk)
    if request.method == 'POST':
        form = LibraryBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = LibraryBookForm(instance=book)
    return render(request, 'student/book_form.html', {'form': form, 'title': 'Update Book'})


def book_delete(request, pk):
    """Delete a book"""
    book = get_object_or_404(LibraryBook, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'student/book_confirm_delete.html', {'book': book})


def book_checkout(request, pk):
    """Check out a book"""
    book = get_object_or_404(LibraryBook, pk=pk)
    if book.is_checked_out:
        messages.error(request, 'Book is already checked out!')
    else:
        book.is_checked_out = True
        book.due_date = datetime.now() + timedelta(days=14)
        book.save()
        messages.success(request, f'Book checked out successfully! Due date: {book.due_date.strftime("%Y-%m-%d")}')
    return redirect('book_detail', pk=book.pk)


def book_return(request, pk):
    """Return a book"""
    book = get_object_or_404(LibraryBook, pk=pk)
    if not book.is_checked_out:
        messages.error(request, 'Book is not checked out!')
    else:
        book.is_checked_out = False
        book.due_date = None
        book.save()
        messages.success(request, 'Book returned successfully!')
    return redirect('book_detail', pk=book.pk)
