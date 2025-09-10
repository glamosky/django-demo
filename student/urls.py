from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create router for REST API
router = DefaultRouter()
router.register(r'books', views.LibraryBookViewSet)

# URL patterns for web interface
urlpatterns = [
    # Web URLs
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/update/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('book/<int:pk>/checkout/', views.book_checkout, name='book_checkout'),
    path('book/<int:pk>/return/', views.book_return, name='book_return'),
    
    # API URLs
    path('api/', include(router.urls)),
]
