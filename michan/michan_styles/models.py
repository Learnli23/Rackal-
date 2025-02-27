from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 
# Create your models here.
 
class Comodities(models.Model):
    
    CATEGORY = [
        ('New', 'New'),
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Accessories', 'Accessories'),
        ('Collections', 'Collections'),
        ('Store', 'Store'),
        ('Bags & Leather Goods', 'Bags & Leather Goods'),
       
    ]

    STATUS = [
        
        ('available', 'available'),
        ('out', 'out'),
    ]

    category = models.CharField(max_length=40, choices=CATEGORY)
    status = models.CharField(max_length=40, choices=STATUS)
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='content/',blank=True)
    image_2 = models.FileField(upload_to='content/',blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField(max_length=10000)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class vidoes(models.Model):
    title = models.CharField(max_length=200)
    video_1=models.FileField(upload_to='content/',blank=True)
    vdeo_2 = models.FileField(upload_to='content/',blank=True)
    def __str__(self):
        return self.title
    
from ckeditor.fields import RichTextField

# Create your models here.
#*****MODEELS TO HANDLe BLOGGS*******
   
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_title = models.CharField(max_length=200)
    blog_title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    video = models.FileField(upload_to='blog_videos', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='blog_dislikes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
     
    def __str__(self):
       return  f"{self. blog_title + '  ' + 'by'+ '  ' + str(self. author) }"

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()    

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.blog_title}'        