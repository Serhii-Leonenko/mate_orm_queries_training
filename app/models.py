from django.contrib.gis.measure import MeasureBase
from django.db import models


class AbstractNameModel(models.Model):
    """Abstract model for simple models"""
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class Author(AbstractNameModel):
    pass


class Genre(AbstractNameModel):
    pass

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    published_date = models.DateField()

    class  Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

class Member(AbstractNameModel):
    joined_date = models.DateField()

class Rental(models.Model):
    """Model represents book rental by the Member"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rentals")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="rentals")
    rented_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "member"],
                name="unique_rental",
            )
        ]

    def __str__(self):
        return f"{self.book.title} rented by {self.member.name}"
