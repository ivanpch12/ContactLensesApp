from django import forms
from django.core.exceptions import ValidationError

from reviews.models import Review


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise ValidationError("Rating must be between 1 and 5")
        return rating



class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')


class ReviewDeleteForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance