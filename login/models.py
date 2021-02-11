from django.db import models

# Create your models here.


class video(models.Model):
    name= models.CharField(max_length=500)
    class_name= models.CharField(max_length=500, null=True)
    subject= models.CharField(max_length=500, null=True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")



    



    

    