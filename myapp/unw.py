def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				#messages.info(request, f"You are now logged in as {username}.")
				return HttpResponse('sucess')
    
			else:
				#messages.error(request,"Invalid username or password.")
				return HttpResponse('error')
		else:
			#messages.error(request,"Invalid username or password.")
			return HttpResponse('erroe')
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})  


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			#messages.success(request, "Registration successful." )
			return HttpResponse('sucess')
			#return redirect(home)
		    #messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def register_request(request):
    v=NewUserForm()
    if(request.method=="POST"):
        v=NewUserForm(request.POST)
        if(v.is_valid()):
            v.save()
            return redirect(mainsite)
    return render(request,"register.html",{"ror":v})



	 print(cust)
                    return render(request,"index.html",{"ror":cust ,"jek":haa}) 