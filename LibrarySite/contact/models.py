from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=140)
    Timestamp = models.CharField(max_length=100)
    message = models.TextField()


    def _str_(self) -> str:
        return "Posted by "+ self.name + " - " + self.subject
