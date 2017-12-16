from django import forms

from .models import Serveriplist



class ServerIplistForm(forms.ModelForm):
    class Meta:
        model = Serveriplist
        fields = [
            'Iplist'
        ]