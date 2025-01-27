from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return self.caption


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email_address = models.EmailField()
    
    
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    def __str__(self):
        return self.fullname()

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", height_field=None, width_field=None, max_length=None,null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True) #search engine friendly url
    #db_index  creates a index makes querying and filtering more effective
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL ,null=True)
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    
