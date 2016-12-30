from django.shortcuts import render

def maps_list(request):
    return render(request, 'mapmaker/maps.html', {})