from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=250)
    
    
    def __str__(self) -> str:
        return self.title
    
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_username')
    title=models.CharField(max_length=250)
    description=models.TextField()
    due_date=models.DateTimeField()
    status=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='task_category')
    dlt=models.IntegerField(default=0)  

    def description_10words(self):
        return self.description[:10]
    
    def __str__(self) -> str:
        return self.title
    

    
class Tag(models.Model):
    name=models.CharField(max_length=250)
    task=models.ManyToManyField(Task)
    
    def __str__(self) -> str:
        return self.name
    

#  The Task: A model with title, description, due date, and status fields.
# • The Category: A model with a one-to-many relationship to Task.
# • The Tag: A model with a many-to-many relationship to Task.
