from django.contrib.auth.models import User
from django.db.models import CharField, TextField, Model, ForeignKey, CASCADE, \
    FloatField, ImageField, TextChoices
from django.forms import EmailField


#
# class Category(Model):
#     name = CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(Model):
#     name = CharField(max_length=100)
#     price = IntegerField()
#     count = PositiveIntegerField(default=0)
#     description = TextField()
#     category = ForeignKey('apps.Category', CASCADE, related_name='products')
#
#
#     def __str__(self):
#         return self.name
#

class Galaxy(Model):
    title = CharField(max_length=100)

    def __str__(self):
        return self.title


class Planet(Model):
    title = CharField(max_length=100)
    diameter = FloatField(help_text='only km')
    distance = FloatField()
    description = TextField()
    icon1 = CharField(max_length=7)
    icon2 = CharField(max_length=7)
    galaxy = ForeignKey('apps.Galaxy', CASCADE, related_name='planets')

    def __str__(self):
        return self.title

class Group(Model):
    title = CharField(max_length=100)

    def __str__(self):
        return self.title

class Star(Model):
    title = CharField(max_length=100)
    description = TextField()
    group = ForeignKey('apps.Group', CASCADE, related_name='stars')

    def __str__(self):
        return self.title


class Gallery(Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

class Exploration(Model):
    title = CharField(max_length=100)

    def __str__(self):
        return self.title




class About(Model):
    title = CharField(max_length=100)
    description = TextField()
    about = ForeignKey('apps.Exploration', CASCADE, related_name='about')

    def __str__(self):
        return self.title


class Holes_Matter(Model):
    title = CharField(max_length=100)
    description = TextField()

    def __str__(self):
        return self.title


class Register(Model):
    class Interests(TextChoices):
        PLANETS = "planets", "Planets & Solar System"
        GALAXIES = "galaxies", "Galaxies & Stars"
        BLACK_HOLES = "black-holes", "Black Holes & Physics"
        EXPLORATION = "exploration", "Space Exploration"
        ALL = "all", "All Topics"

    name = CharField(max_length=100)
    email = EmailField(max_length=100)
    interest = CharField(max_length=20, choices=Interests.choices)
    message = TextField()




