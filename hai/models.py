from django.db import models

#  model for prudect.
class producte(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=(LIVE,'live'),(DELETE,'delete')
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='Images')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


