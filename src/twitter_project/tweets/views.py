# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from django.urls import reverse_lazy
from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

#can also use LoginRequiredMixin 
# class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
# need to set login_url = 'url_for_login'
class TweetCreateView(FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_tweet.html'
	# success_url = '/tweet/create/'
	# def form_valid(self, form):
	# 	if(self.request.user.is_authenticated()):
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView, self).form_valid(form)
	# 	else:
	# 		form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
	# 		return self.form_invalid(form)

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	# success_url = reverse_lazy("tweet:detail")
	template_name = 'tweets/update_tweet.html'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	success_url = reverse_lazy('tweet:list')
	template_name = "tweets/delete_tweet.html"


class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()
	template_name = "tweets/detail_view.html"
	# def get_object(self):
	# 	pk=self.kwargs.get("pk")
	# 	obj=get_object_or_404(Tweet, pk=pk)
	# 	return Tweet.objects.get(id=1)

class TweetListView(ListView):
	# queryset = Tweet.objects.all()
	template_name = "tweets/list_view.html"
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			#make sure to have 2 underscores
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query))
		return qs

	# how we knew that variables are object_list and object
	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context

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