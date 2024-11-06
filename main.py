# TEST QUERIES HERE
import init_django_orm # noqa

from app.models import Member,  Rental, Book, Genre


def query():
    # ToDo write your queries in the result
    result = Member.objects.filter(rentals__book__genres__name="Science Fiction").exclude(rentals__book__genres__name="Fantasy")


    return result

if __name__ == "__main__":
    print(query())