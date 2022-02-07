from django.db import models

# Create your models here.
class WelModel(models.Model):
    title = models.CharField(max_length=50)
    number = models.IntegerField()
    # decision category choices
    KITCHEN = 'KT'
    BATH = 'BT'
    ROOM = 'RM'
    COOK = 'CO'
    AMENITY = 'AM'
    OTHER = 'OT'
    CATEGORY_CHOICES = [
        (KITCHEN, 'Kitchen'),
        (BATH, 'Bath'),
        (ROOM, 'Room'),
        (COOK, 'Cook'),
        (AMENITY, 'Amenity'),
        (OTHER, 'Other')
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=KITCHEN,
    )
    
    def __str__(self) -> str:
        return self.title.__str__()