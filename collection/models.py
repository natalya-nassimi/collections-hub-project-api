from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        to='users.User',
        related_name='profile',
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'Profile for {self.user.username}'
    
class Collection(models.Model):
    user = models.ForeignKey(
        to='users.User',
        related_name='collections',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.user.username}'
    
class Item(models.Model):

    ITEM_TYPE_CHOICES = [
        ('recipe', 'Recipe'),
        ('book', 'Book'),
        ('music', 'Music'),
        ('movie', 'Movie'),
        ('travel', 'Travel'),
        ('workout', 'Workout'),
        ('restaurant', 'Restaurant'),
        ('product', 'Product'),
        ('event', 'Event'),
        ('game', 'Game'),
    ]

    collection = models.ForeignKey(
        to=Collection,
        related_name='items',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    image = models.URLField(blank=True)
    link = models.URLField(blank=True)
    details = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} [{self.item_type}]'