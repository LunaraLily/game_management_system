from django.db import models

# Create your models here.
class GameInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    platform = models.CharField(max_length=20)
    company = models.CharField(max_length=20)

    class Meta:
        db_table = 'game_info'
