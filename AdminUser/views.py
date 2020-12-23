from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
