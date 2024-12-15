from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# database related work 

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts/')
    likes = models.ManyToManyField(User,related_name='liked_post',blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"post is creadet on {self.created_at}"
    
class Like(models.Model):
    user = models.ForeignKey(User,related_name='Like',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='Like',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.post.caption} on {self.created_at}"

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    caption = models.TextField()

    def __str__(self):
        return f"{self.user.username}:{self.caption}" if self.user else "Comment without user"

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
        
