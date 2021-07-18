from django.shortcuts import render,redirect
from django.contrib import messages
import datetime as dt
from .models import Projects,Profile
from django.http  import Http404
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm,UploadForm,Registration,ProfileForm,AuthenticationForm
from django.contrib.auth import login, authenticate 
 

# Create your views here.

def register(request):
    if request.method == 'POST':
     form = Registration(request.POST)
     if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login.html')
    else:
      form = Registration()
    return render(request,'registration/registration_form.html',{"form":form})

def login_request(request):
    	if request.method == "POST":
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'registration/login.html', context={"login_form":form})

def index(request):
  date = dt.date.today()
  projects = Projects.objects.all()
  return render(request, 'all-awards/index.html', {"date":date, "projects":projects} )

def project(request, id):
    
    try:
        project = Projects.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()    
    
    return render(request, "all-awards/project.html", {"project":project})
  
@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('index')

    else:
        form = UploadForm()
    return render(request, 'all-awards/upload_project.html', {"form":form})

@login_required(login_url='/accounts/login')
def search(request):
    projects = Projects.objects.all()
    parameter = request.GET.get("project")
    result = Projects.objects.filter(project_name__icontains=parameter)
    print(result)
    return render(request, 'all-awards/search.html', locals())

def new_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
       
        if form.is_valid():
            profile = form.save(commit=False)  
            profile.user = current_user
            profile.save()
            
    return render(request, 'profile.html', {"form": form, "profile": profile})
