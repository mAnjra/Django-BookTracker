from django.db import models
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
class Books(models.Model):
    book_title = models.CharField(max_length=255)
    book_genre = models.CharField(max_length=255)
    #created_at = models.DateField(_('Date'), default=datetime.date.today)
    created_at = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    completed_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('library', 'Library'),('reading','Currently Reading'),('completed',"Completed")
    ], default='library')

    def clean(self):
        if self.completed_date and not self.start_date:
            raise ValidationError("Cannot mark a book as completed wihtout a start date")
        
        if self.completed_date and self.start_date:
            if self.completed_date < self.start_date:
                raise ValidationError("Completed date cannot be before start date")
    
    def save(self, *args, **kwargs):
        """Override save method to full clean that matches the validation set out in the clean method"""
        self.full_clean()
        super().save(*args, **kwargs)     

    class Meta:
        '''This class holds extra information to help with model management'''
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return f"{self.book_title}"