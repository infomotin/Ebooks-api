from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
# Ebooks DB Class

class Ebook(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.title} {self.author}"


# Reviews Class BD

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    review_author = models.CharField(max_length=8, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.rating)
