from django import forms
from .models import Userper, cart, datas, person,datarow
from .models import person1

class details(forms.ModelForm):
    class Meta:
        model=person
        fields="__all__"

    
class nexta(forms.ModelForm):
    class Meta:
        model=person1
        fields="__all__"

class replay(forms.ModelForm):
    class Meta:
        model=datas
        fields="__all__"
    
class relay(forms.ModelForm):
    class Meta:
        model=datarow
        fields="__all__"
    
class helpp(forms.Form):
    email=forms.EmailField()
    subject=forms.CharField(max_length=60)
    msg=forms.CharField(max_length=300)

class login(forms.Form):
    username=forms.CharField()
    password=forms.CharField(max_length=60)

class newuser(forms.ModelForm):
	class Meta:
		model = Userper
		fields = "__all__"
    
class cartt(forms.ModelForm):
	class Meta:
		model = cart
		fields = "__all__"

