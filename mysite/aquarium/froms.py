from .models import FishReview
from django import forms


class FishReviewForm(forms.ModelForm):
    class Meta:
        model = FishReview
        fields = ['content']