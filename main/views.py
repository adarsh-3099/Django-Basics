from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%s"  % t.name)
    else:
        form  = CreateNewList()

    return render(response, 'main/create.html', {"form":form})

def index(response, name):
    ls = ToDoList.objects.get(name=name)
    #items = ls.item_set.get(id=1)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            ls.item_set.create(text=txt, complete=False)


    return render(response, 'main/list.html', {"ls":ls})

def view(request):
	l = ToDoList.objects.all()
	return render(request, "main/view.html", {"lists":l})