from django.db import models

# Create your models here.
class Post(models.Model):
    title = description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=200) # Theoretically this would be a foreign key to a user model
    published = models.DateField(auto_now_add=True)
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

    def __str__(self):
        return self.title + " - " + self.author
        
    # Returns post's content or its first 200 characters if it has more
    @property
    def postPreview(self):
        try:
            preview = self.content[0:200] + "..."
        except:
            preview = self.content
        return preview
    
    @property
    def netVotes(self):
        return self.upvotes - self.downvotes

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=200) # See Post author
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')