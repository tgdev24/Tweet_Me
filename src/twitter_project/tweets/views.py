# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from .models import Tweet
from .forms import TweetModelForm

class TweetCreateView(CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_tweet.html'
	success_url = '/tweet/create/'

	def form_valid(self, form):
		if(self.request.user.is_authenticated()):
			form.instance.user = self.request.user
			return super(TweetCreateView, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
			return self.form_invalid(form)

class TweetDetailView(DetailView):
	template_name = "tweets/detail_view.html"
	queryset = Tweet.objects.all()
	# def get_object(self):
	# 	pk=self.kwargs.get("pk")
	# 	obj=get_object_or_404(Tweet, pk=pk)
	# 	return Tweet.objects.get(id=1)

class TweetListView(ListView):
	template_name = "tweets/list_view.html"
	queryset = Tweet.objects.all()

# Create your views here.
# def tweet_detail(request, id=1):
# 	obj = Tweet.objects.get(id=id)
# 	context ={
# 		"object": obj
# 	}
# 	return render(request, "tweets/detail_view.html", context)

# def tweet_list(request):
# 	queryset = Tweet.objects.all()
# 	for obj in queryset:
# 		print(obj.content)
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, "tweets/list_view.html", context)