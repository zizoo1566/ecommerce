from django.shortcuts import render,redirect
from .models import Destination


def home(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})


def services(request):
    return render(request, 'services.html')


def control(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.POST['img']
        desc = request.POST['desc']
        price = int(request.POST['price'])
        offer = bool(request.POST['offer'])

        post = Destination.objects.create(name=name, img=img, desc=desc, price=price, offer=offer)
        post.save()
        print('Dest Created')
        return redirect('/')
    else:
        return render(request, 'add_Destination.html')
