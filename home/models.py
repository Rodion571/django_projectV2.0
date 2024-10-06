from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible =True).order_by('sort')
        for dish in dishes:
            yield dish

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.IntegerField()
    unit = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='dishes', blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=50)
    sort = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='events', blank=True, null=True)
    date_and_time = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChefCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Chef(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='chefs', blank=True, null=True)
    chef_category = models.ForeignKey(ChefCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery', blank=True, null=True)
    position = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    item_title = models.CharField(max_length=50)
    item_description = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_title

class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?3?\d{9,15}', message="Phone number must be entered in the format: '+3999999999'")
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name