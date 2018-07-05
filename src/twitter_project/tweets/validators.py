from django.core.exceptions import ValidationError

def validate_content(value):
	content = value
	if content == "damn":
		raise ValidationError("Content cannot be profanity. Just Write a NICE Tweet")
	return value