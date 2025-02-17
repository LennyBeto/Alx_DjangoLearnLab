from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

   class UserProfile(models.Model):
       ROLE_CHOICES = [
           ('Admin', 'Admin'),
           ('Librarian', 'Librarian'),
           ('Member', 'Member'),
       ]
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       role = models.CharField(max_length=10, choices=ROLE_CHOICES)

   @receiver(post_save, sender=User)
   def create_user_profile(sender, instance, created, **kwargs):
       if created:
           UserProfile.objects.create(user=instance)

   @receiver(post_save, sender=User)
   def save_user_profile(sender, instance, **kwargs):
       instance.userprofile.save()
          
   class Author(models.Model):
       return self.name = models.CharField(max_length=100)

   class Book(models.Model):
       title = models.CharField(max_length=200)
       author = models.ForeignKey(Author, on_delete=models.CASCADE)

   class Library(models.Model):
       name = models.CharField(max_length=100)
       books = models.ManyToManyField(Book)

   class Librarian(models.Model):
       name = models.CharField(max_length=100)
       library = models.OneToOneField(Library, on_delete=models.CASCADE)


    class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    # Add other fields as necessary

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

