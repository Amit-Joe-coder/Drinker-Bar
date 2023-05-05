from django.shortcuts import render,redirect
from mainapp.models import rate
from mainapp.forms import entry_form



# Create your views here.
def index_view(request):
    return render(request,'index.html')




def table_view(request):
    data=rate.objects.all()
    return render(request,'info.html',{'table':data})



def form_view(request):
    form=entry_form()
    if request.method=='POST':
        form=entry_form(request.POST)
        if form.is_valid():
            form.save()
            return table_view(request)
    return render(request,'form.html',{'form':form})



def update_view(request,id):
    model=rate.objects.get(id=id)
    form=entry_form(instance=model)
    if request.method =="POST":
        form=entry_form(request.POST,instance=model)
        if form.is_valid():
            form.save()
            return redirect('/info')
    return render(request,'update.html',{'form':form})

def delete_view(request,id):
    item=rate.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect("/info")
    return render(request,'delete.html',{'item':item})
