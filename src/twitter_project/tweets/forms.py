from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = [
			#"user",
			"content"
		]
		# exclude = ['user']
		def clean_content(self, *args, **kwargs):
			content = self.cleaned_data.get("content")
			if content=="":
				raise forms.ValidationError("Cannot be empty")
			return content