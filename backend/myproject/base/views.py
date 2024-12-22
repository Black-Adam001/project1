from django.shortcuts import render
from django.http import HttpResponse
from . models import Room , Topic
from .forms import RoomForm
# Create your views here.
# rooms = [
# 	{'id' : 1 , 'name' : 'Welcome To GIS learning!'},
# 	{'id' : 2 , 'name' : 'Accouting II Lovers'},
# 	{'id' : 3 , 'name' : 'Java coders in Zanzibar'},
# 	{'id' : 4 , 'name' : 'Database Masters in SUZA'},
# 	{'id' : 5 , 'name' : 'All About Information System'},

# ]


def home (request):
	q = request.GET.get('q')
	# rooms = Room.objects.all()
	rooms = Room.objects.filter(topic__name=q)
	topics = Topic.objects.all()
	context = {'room' : room , 'topics' : topics}

	return render (request , 'base/home.html', context)

def room (request, pk):
	room = Room.objects.get(id=pk)
	# room = None
	# for i in rooms:
	# 	if i ['id'] == int(pk):
	# 		room = i
	context = {'room' : room}
	return render (request , 'base/room.html', context)

def create_room (request):
	form = RoomForm()
	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
			form = RoomForm()
			# return redirect ('home')

	context = {'form' : form}
	return render (request , 'base/room_form.html',context)

def updateRoom (request , pk):
	room = Room.objects.get(id = pk)
	form = RoomForm(instance = room)
	if request.method == 'POST':
		form = RoomForm(request.POST, instance=room)
		if form.is_valid():
			form.save()
			form = RoomForm()
	context ={'form' : form}
	return render (request , 'base/room_form.html' , context)

def DeleteRoom(request , pk):
	room = Room.objects.get(id = pk)
	if request.method == 'POST':
		room.delete()
	return render (request , 'base/delete.html' ,{'obj' : room})



