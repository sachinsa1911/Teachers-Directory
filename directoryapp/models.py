from django.db import models

# Create your models here.


class LoginTable(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'LoginTable'


class TeacherModel(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Profilepicture = models.ImageField(upload_to='profilepic/')
    EmailAddress = models.CharField(unique=True, max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    RoomNumber = models.CharField(max_length=100)
    Subjectstaught = models.TextField(max_length=1000)

    class Meta:
        db_table = 'Teachers'
