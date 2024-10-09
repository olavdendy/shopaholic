from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["nama_produk", "deskripsi", "harga"]

    def clean_nama_produk(self):
        nama_produk = self.cleaned_data["nama_produk"]
        return strip_tags(nama_produk)

    def clean_deskripsi(self):
        deskripsi = self.cleaned_data["deskripsi"]
        return strip_tags(deskripsi)