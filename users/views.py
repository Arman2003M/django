from django.shortcuts import render
from .models import Users
from .forms import UsersForm
def index (request):
    user = Users.objects.all()
    form = UsersForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=UsersForm()
    
    return render(request,"users/index.html", {"user":user,"form":form})
    


