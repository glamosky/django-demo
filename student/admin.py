from django.contrib import admin
from .models import Student, Teacher, LibraryBook

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name']
    search_fields = ['first_name', 'last_name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name']
    search_fields = ['first_name', 'last_name']

@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'is_checked_out', 'due_date', 'created_at']
    list_filter = ['is_checked_out', 'created_at']
    search_fields = ['title', 'author', 'isbn']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'isbn')
        }),
        ('Status', {
            'fields': ('is_checked_out', 'due_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
