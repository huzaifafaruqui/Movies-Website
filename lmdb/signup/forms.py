from django import forms


from .models import users


class PostForm(forms.ModelForm):
    class Meta:
    	password = forms.CharField(widget=forms.PasswordInput)
        model = users
        fields = [
            "user_name",
	        "full_name",
	        "email_id",
	        "password"
            
        ]