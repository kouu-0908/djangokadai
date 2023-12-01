from django.forms import ModelForm
from .models import PhotoPost,Category
 
class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category','title','comment','image1','subtitle']
 
class KategoriTuika(ModelForm):
    class Meta:
        model = Category
        fields = ['title']