from django.db import models
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Home(models.Model):
    Sno = models.AutoField(primary_key=True)
    image = models.TextField(max_length=100)
    line_1 = models.TextField()
    line_2 = models.TextField()
    line_3 = models.TextField()
    


    def _str_(self) -> str:
        return "Posted by "+ self.image + " - " + self.subject


