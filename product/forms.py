from django import forms
from product.models import Review

class ProductForm(forms.Form):
    title= forms.CharField(max_length=50)
    content= forms.CharField(widget=forms.Textarea)
    image= forms.ImageField(required=False)

    def clean_title(self):
        title = self.cleaned_data['title']
        if "lala" in title.lower():
            raise forms.ValidationError("NO")
        return title

class CategoryForm(forms.Form):
    name= forms.CharField(max_length=50)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

