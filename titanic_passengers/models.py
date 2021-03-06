from django.db import models

# Create your models here.
class TitanicPassenger(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )

    CHERBOURG = 'C'
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'
    PORT_CHOICES = (
        (CHERBOURG, 'Cherbourg'),
        (QUEENSTOWN, 'Queenstown'),
        (SOUTHAMPTON, 'Southampton'),
    )

    name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    survived = models.BooleanField()
    age = models.FloatField(null=True)
    fare = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)

    def __str__(self):
        return self.name
