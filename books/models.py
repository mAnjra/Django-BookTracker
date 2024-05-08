from django.db import models
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

    class Meta:
        '''This class holds extra information to help with model management'''
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return f"{self.book_title}"