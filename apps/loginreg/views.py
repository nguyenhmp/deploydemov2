# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(req):
	return render(req, "loginreg/index.html")
def login(req):
	result = User.objects.validate(req.POST) # tuple consisting of (true/false, errors[if any])
	if result[0]:
		user = User.objects.filter(email=req.POST["email"])
		if len(user) > 0:
			user = user[0]
			if bcrypt.checkpw(req.POST["password"].encode(), user.password.encode()):
				req.session["user_id"] = user.id
				messages.error(req, "Your in but my app doesnt do anything yet")
			else:
				messages.error(req, "password does not match")
		else:
			messages.error(req, "email does not exist")
		return redirect("/loginreg")
	else:
		errors = result[1]
		for error in errors:
			messages.error(req, error)
		return redirect('/loginreg')
def register(req):
	result = User.objects.validate(req.POST) # tuple consisting of (true/false, errors[if any])
	if result[0]:
		hashed_pw = bcrypt.hashpw(req.POST["password"].encode(), bcrypt.gensalt())
		User.objects.create(email=req.POST["email"], password=hashed_pw)
		messages.error(req, "Register successsful")
		return redirect("/loginreg")
	else:
		errors = result[1]
		for error in errors:
			messages.error(req, error)
		return redirect('/loginreg')
		#pass to view
