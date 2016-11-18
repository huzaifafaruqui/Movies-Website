from django import forms
import re
from django.contrib.auth.models import User
from .models import Movie,Comment
class RegistrationForm(forms.Form):
	name=forms.CharField(label=u'Name',max_length=30)
	username = forms.CharField(label=u'Username', max_length=30)
	email = forms.EmailField(label=u'Email')
	password1 = forms.CharField(
	label=u'Password',
	widget=forms.PasswordInput()
	)
	password2 = forms.CharField(
	label=u'Password (Again)',
	widget=forms.PasswordInput()
	)
	
	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
		if password1 == password2:
			return password2
		raise forms.ValidationError('Passwords do not match.')
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken.')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('rating', 'text',)


class SearchForm(forms.ModelForm):
	genres = forms.MultipleChoiceField(choices=Movie.genres,widget=forms.CheckboxSelectMultiple,label="Genres:")
	#rating=forms.MultipleChoiceField(choices=Comment.RATINGS,widget=forms.CheckboxSelectMultiple,label="rating:")
	
	minr=forms.IntegerField()
	class Meta:
		model=Movie
		
		exclude=['image','duration']

class SearchForm2(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['rating']		
