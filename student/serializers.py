from rest_framework import serializers
from .models import LibraryBook


class LibraryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBook
        fields = ['id', 'title', 'author', 'isbn', 'is_checked_out', 'due_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_isbn(self, value):
        """Validate that ISBN is exactly 13 digits"""
        if not value.isdigit() or len(value) != 13:
            raise serializers.ValidationError("ISBN must be exactly 13 digits")
        return value
    
    def validate(self, data):
        """Validate that due_date is only set when book is checked out"""
        if data.get('is_checked_out') and not data.get('due_date'):
            raise serializers.ValidationError("Due date is required when book is checked out")
        if not data.get('is_checked_out') and data.get('due_date'):
            raise serializers.ValidationError("Due date should not be set when book is not checked out")
        return data


class LibraryBookCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new books (without due_date initially)"""
    class Meta:
        model = LibraryBook
        fields = ['title', 'author', 'isbn']
    
    def validate_isbn(self, value):
        """Validate that ISBN is exactly 13 digits"""
        if not value.isdigit() or len(value) != 13:
            raise serializers.ValidationError("ISBN must be exactly 13 digits")
        return value
