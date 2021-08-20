from django import forms

from .models import AddNewCode, Cards

class AddCode(forms.ModelForm):
    """AddCode definition."""
    class Meta:
        model = Cards
        fields = '__all__'
        exclude = ('code','owner','slug','language_type','image')


class EditCode(forms.ModelForm):
    """ edit the code """
    class Meta:
        model = Cards
        fields = ['description','code_blog']
