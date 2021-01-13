from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class SignUp(FormView):
   template_name = 'registration/signup.html'
   form_class = UserCreationForm
   success_url = reverse_lazy('home')

   def form_valid(self, form):
      if self.request.recaptcha_is_valid:
         form.save()
         username = self.request.POST['username']
         password = self.request.POST['password1']
         user = authenticate(username=username, password=password)
         login(self.request, user)
         return super(SignUp, self).form_valid(form)
      return render(self.request, self.template_name, self.get_context_data())