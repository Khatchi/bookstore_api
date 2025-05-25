from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    
class PriceHistory(models.Model):
    book = models.ForeignKey(Book, related_name='price_history', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.price}"
