from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.username if not self.is_anonymous else "Anonymous"

class Story(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Profile, related_name='stories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    story = models.ForeignKey(Story, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {"Anonymous" if self.author.is_anonymous else self.author.username} on {self.story.title}'