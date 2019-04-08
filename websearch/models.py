from django import forms
from djongo import models

class Page(models.Model):
    link = models.CharField(max_length=20000)
    most_relevant_info = models.TextField()
    extra_info = models.TextField(max_length=20000)

    class Meta:
        abstract = True


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = (
            'link',
            'most_relevant_info',
            'extra_info',
        )

class Search(models.Model):
    original_input = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    result = models.ArrayModelField(
        model_container = Page,
        model_form_class = PageForm
    )


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = (
            'original_input',
            'keywords',
        )