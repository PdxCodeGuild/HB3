from django.db import models


# Create your models here.
class ZipcodeModel(models.Model):
    zip_code = models.CharField(max_length=5)
    def __str__(self):
        return self.zip_code
    
# class FishModel(models.Model):

#     fishname = models.CharField(max_length=100)
#     fishdescription = models.TextField()
    
#     fish_zip_codes = models.ManyToManyField(ZipcodeModel)

#     def __str__(self):
#         return self.name
    
#     # fishlocation = fish['Location']
#     # fishhabitat = fish['Habitat']
#     # fishphoto = fish['Species Illustration Photo']
    
#     # fishcalories = fish['Calories']
#     # fishcarbohydrates = fish['Carbohydrate']
#     # fishcholesterol = fish['Cholesterol']
#     # fishfat = fish['Fat, Total']
#     # fishfiber = fish['Fiber, Total Dietary']
#     # fishprotein = fish['Protein']
#     # fishSfat = fish['Saturated Fatty Acids, Total']
#     # fishsodium = fish['Sodium']
#     # fishtaste = fish['Taste']
#     # fishtexture = fish['Texture']
#     # fishhealth = fish['Health Benefits']
    
#     # fishfarming = fish['Farming Methods']
#     # fishenvironment = fish['Environmental Effects']
#     # fishrate = fish['Fishing Rate']
    
#     # fishlocation = models.ManyToManyRel(ZipcodeModel)


# models.py




class SpeciesData(models.Model):
    zip_code = models.CharField(max_length=10)
    species_list = models.JSONField()

    def __str__(self):
        return self.zip_code
    
class FishSpeciesModel(models.Model):
    fish_name = models.CharField(max_length=100)
    fish_zip = models.ManyToManyField(ZipcodeModel)
    fish_habitat = models.TextField(default=0)
    
    fishcalories = models.FloatField(default=0)
    fishcarbohydrates = models.FloatField(default=0)
    fishcholesterol = models.FloatField(default=0)
    fishfat = models.FloatField(default=0)
    fishfiber = models.FloatField(default=0)
    fishprotein = models.FloatField(default=0)
    fishSfat = models.FloatField(default=0)
    fishsodium = models.FloatField(default=0)
    
    fishtaste = models.TextField(default=0)
    fishtexture = models.TextField(default=0)
    fishhealth = models.TextField(default=0)
    
    fishfarming = models.TextField(default=0)
    fishenvironment = models.TextField(default=0)
    fishrate = models.TextField(default=0)
    
    fishphoto = models.ImageField(upload_to="data/", default=0)

    
    def __str__(self):
        return self.fish_name


#############################################################

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    