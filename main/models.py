from django.db import models
import uuid

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    nama_produk = models.CharField(max_length=255)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    
    