from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(
        max_length=13,
        unique=True,
        validators=[RegexValidator( # stackoverflow will diss the crap out of you but give the best answers
            regex=r'^\d{13}$',
            message='ISBN must be exactly 13 digits'
        )]
    )
    is_checked_out = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']