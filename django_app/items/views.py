from django.shortcuts import render, redirect
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

def index(request):
    items = Item.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items:index')
    else:
        form = ItemForm()
    return render(request, 'items/index.html', {'items': items, 'form': form})

def homepage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        if name:
            Item.objects.create(name=name, description=description)
    items = Item.objects.all()
    return render(request, 'items/homepage.html', {'items': items})