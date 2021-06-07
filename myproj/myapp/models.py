from django.db import models
from django.core.validators import MaxValueValidator
# makemigrations - create changes and store in file
#migrate - apply changes

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.PositiveBigIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    addr = models.CharField(max_length=122)
    desc = models.CharField(max_length=222)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=6)
    date = models.DateField()

    def __str__(self) -> str:
        return self.fname

