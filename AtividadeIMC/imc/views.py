from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        height = float(request.POST.get('height', 0))
        weight = float(request.POST.get('weight', 0))
        
        body_mass_index = round(weight / (height ** 2), 2)

        return render(request, 'index.html', {"result": body_mass_index})

    return render(request, 'index.html')