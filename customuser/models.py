from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # pass
    ROLE = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=30, choices=ROLE, default="User")

    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True)
            
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    method = models.TextField()
    thumbnail = models.ImageField(default="https://images.pexels.com/photos/326058/pexels-photo-326058.jpeg", null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    # updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created', ]


class Review(models.Model):
    comment_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)
    review = models.CharField(max_length=100, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review

    class Meta:
        ordering = ['date_created', ]


class Contact(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    desc = models.TextField(null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created', ]


