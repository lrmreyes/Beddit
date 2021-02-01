from django.db import models
from django.utils.timezone import localdate

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    content = models.TextField(blank=True)
    author = models.CharField(max_length=200) # Theoretically this would be a foreign key to a user model
    published = models.DateField(default=localdate)
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

    def __str__(self):
        return self.title + " - " + self.author
            
    @property
    def netVotes(self):
        return self.upvotes - self.downvotes

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=200) # See Post author
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.content + " - " + self.author