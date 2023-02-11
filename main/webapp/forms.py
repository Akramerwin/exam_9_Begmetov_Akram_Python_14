from django import forms
from django.contrib.auth import get_user_model
from django.forms import widgets
from webapp.models import Adds, Comments
from django.core.validators import BaseValidator, ValidationError
from django.utils.deconstruct import deconstructible

class AddsForm(forms.ModelForm):
    class Meta:
        model = Adds
        fields = ['title', 'description_adds', 'category', 'price']


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['description_review', 'rating']


# class ModeratorReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['description_review', 'rating', 'is_moderated']