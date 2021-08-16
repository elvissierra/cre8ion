from django.db import models

#user = models.ForeignKey(
#User, on_delete=models.CASCADE, null=True, blank=True)

class Prints (models.Model):
    filename = models.CharField(max_length=50, default='')
    creator = models.CharField(max_length=50, default= '')
    created= models.DateTimeField(auto_now_add= True)
    stl = models.FileField(upload_to= "stls")
    cover = models.ImageField(upload_to= "covers")
    

    def __str__(self):
        return self.filename

    


