from django import forms


from .models import userlogin


class PostForm(forms.ModelForm):
    class Meta:
    	password = forms.CharField(widget=forms.PasswordInput)
        model = userlogin
        fields = [
            "user_name",
	        "password"
            
        ]