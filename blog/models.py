from django.db import models
from django.utils import timezone
from django.conf import settings
# from django.urls import
#from django.urls import reverse


# Create your models here.


CHOICE = (('publish','publish'),
          ('Draft','Draft')

)

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE,related_name='blog_posts')
    header_image = models.ImageField(upload_to='media')
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    published = models.BooleanField(default=False)



    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-post_date']

    def __str__(self):
        #return super().__str__()(self):
        return self.title    


#    def get_absolute_url(self):
 #       return reverse("post", kwargs={"pk": self.pk})
        



class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']

    def __str__(self):
        return self.author