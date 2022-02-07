from django.shortcuts import render

from welapp.models import WelModel
from django.views.generic.edit import CreateView

# Create your views here.

def welfunc(request):
    kitchen_list = WelModel.objects.filter(category="KT")
    bath_list = WelModel.objects.filter(category="BT")
    room_list = WelModel.objects.filter(category="RM")
    cook_list = WelModel.objects.filter(category="CO")
    amenity_list = WelModel.objects.filter(category="AM")
    other_list = WelModel.objects.filter(category="OT")    
    return render(request, 'list.html', {'kitchen_list': kitchen_list,\
        'bath_list':bath_list,'room_list': room_list,\
            'cook_list':cook_list, 'amenity_list':amenity_list, \
                'other_list':other_list})
    
class createList(CreateView):
    template_name = 'create.html'
    model = WelModel