from django.shortcuts import render
from .models import Schedule

# Create your views here.
def list_schedules(request):
    schedules = Schedule.objects.all().order_by('date')
    return render(request, 'list-schedules.html', {'schedules': schedules})