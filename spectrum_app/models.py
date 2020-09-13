from django.db import models

PHOTO_TYPES = (
    ('Commercial','Commercial'),
    ('Kids','Kids'),
    ('Portrait','Portrait'),
)
SHOOT_TYPES = (
    ('Wedding','Wedding'),
    ('Portrait','Portrait'),
    ('Other events','Other events')
)
class AllPhoto(models.Model):
    photo_name = models.CharField(max_length=50)
    photo_type = models.CharField(choices=PHOTO_TYPES,max_length=10)
    main_photo = models.ImageField(upload_to="images/")
    c_man = models.CharField(max_length=30)

    def __str__(self):
        return self.photo_name+" "+self.photo_type+" "+self.c_man

class Photo(models.Model):
    main = models.ForeignKey(AllPhoto,on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.main.photo_name

class SliderPhoto(models.Model):
    img = models.ImageField(upload_to="images/")


class WeddingCouple(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    place = models.CharField(max_length=50)
    photographer = models.CharField(max_length=100)
    review = models.CharField(max_length=500, blank=True,null=True)
    main_photo = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.name

class WeddingPhoto(models.Model):
    couple = models.ForeignKey(WeddingCouple,on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.couple.name




class Book(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    date = models.DateField()
    shoot_type = models.CharField(max_length=20)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.name+" "+self.place