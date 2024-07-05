from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField() 
    phonenumber = models.IntegerField()
    description = models.TextField()

    def __str__(self) :
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length = 40)
    description = models.TextField()
    techstack = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'project' , blank = True , null = True)
    timestamp = models.DateTimeField(auto_now_add=True , blank = True)

    
    def __str__(self) :
        return self.title