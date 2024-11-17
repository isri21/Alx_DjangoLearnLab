from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=150)
    author = forms.CharField(max_length=500)
    publication_year = forms.IntegerField()