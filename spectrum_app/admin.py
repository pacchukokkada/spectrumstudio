from django.contrib import admin
from .models import *


    
class PhotoAdmin(admin.StackedInline):
    model = Photo

class AllPhotoAdmin(admin.StackedInline):
    model = AllPhoto

@admin.register(AllPhoto)
class AllPhotoAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
       model = AllPhoto
       
@admin.register(SliderPhoto)
class SliderPhotoAdmin(admin.ModelAdmin):
    pass

class WeddingPhotoAdmin(admin.StackedInline):
    model = WeddingPhoto

class WeddingCoupleAdmin(admin.StackedInline):
    model = WeddingCouple

@admin.register(WeddingCouple)
class WeddingCoupleAdmin(admin.ModelAdmin):
    inlines = [WeddingPhotoAdmin]

    class Meta:
       model = WeddingCouple

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass