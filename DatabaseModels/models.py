from django.db import models

# Create your models here.
class user(models.Model):
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    role=models.CharField(max_length=45)

    class Meta:
        db_table="user"


