from .models import FishReview, Profilis
from django import forms
from django.contrib.auth.models import User


class FishReviewForm(forms.ModelForm):
    class Meta:
        model = FishReview
        fields = ['content']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']


class DateInput(forms.DateInput):
    input_type = "date"
