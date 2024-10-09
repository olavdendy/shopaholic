from django.db import models
import uuid
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    nama_produk = models.CharField(max_length=255) #tadinya mood
    deskripsi = models.TextField() #tadinya feelings
    harga = models.IntegerField() #tadinya mood_intensity
    
    