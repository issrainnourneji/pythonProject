from django.db import models
from users.models import *
from django.core.exceptions import ValidationError
import datetime
from django.core.validators import MinValueValidator
# Create your models here.
def titleValidator(value):
    if not value[0].isupper():
        raise ValidationError(
            "title must contain capital letters"
        )
def dateValidator(value):
    if not value >= datetime.date.today():
        raise ValidationError(
            "date must be in futur"
        )
class Event(models.Model):
    CATEGORY_CHOICES = (
        ('Music', 'Music'),
        ('Cinema', 'Cinema'),
        ('Sport', 'Sport'),
    )

    title = models.CharField(max_length=255, null=True, validators=[titleValidator])
    description = models.TextField()
    eventImage = models.ImageField(upload_to='images/', blank=True)

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=8)
    state = models.BooleanField(default=False)
    nbrParticipants = models.IntegerField(default=0, validators=[MinValueValidator(0, message ='must be positiv') ])
    eventDate = models.DateField(validators=[dateValidator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    organizer = models.ForeignKey(Person, on_delete=models.CASCADE)

    participate = models.ManyToManyField(
        Person,
        related_name="Participation",
        through='Participation'
    )
    def _str_(self):
        return self.title

class Participation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event , on_delete=models.CASCADE)
    datePart = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('person','event')

