from django.shortcuts import render, get_object_or_404, redirect
from .models import Map
from .models import POI
from .forms import POIForm



def maps_list(request):
    maps = Map.objects.order_by('name')
    return render(request, 'mapmaker/maps.html', {'maps': maps})


def map_editor(request, pk):
    poi = POI.objects.order_by('name')
    map = get_object_or_404(Map, pk=pk)
    return render(request, 'mapmaker/editor.html', {'map': map, 'pois': poi})


def POI_new(request):
    if request.method == "POST":
        form = POIForm(request.POST)
        if form.is_valid():
            poi = form.save(commit=False)
            poi.save()
            return redirect('map_editor', pk=1)
    else:
        form = POIForm()
    return render(request, 'mapmaker/POI.html', {'form': form})


def POI_edit(request, pk):
    poi = get_object_or_404(POI, pk=pk)
    if request.method == "POST":
        form = POIForm(request.POST, instance=poi)
        if form.is_valid():
            poi = form.save(commit=False)
            poi.save()
            return redirect('map_editor', pk=1)
    else:
        form = POIForm(instance=poi)
    return render(request, 'mapmaker/POI.html', {'form': form})