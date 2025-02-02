from django.shortcuts import render, HttpResponse


def show_fuel_form(request):
    ALCOHOL_PRICE = 3.15
    GASOLINE_PRICE = 4.05

    ALCOHOL_CAR_CONSUMPTION = 10.5
    GASOLINE_CAR_CONSUMPTION = 12.5

    default_data = {
        'alcohol_price': ALCOHOL_PRICE,
        'gasoline_price': GASOLINE_PRICE,
        'alcohol_car_consumption': ALCOHOL_CAR_CONSUMPTION,
        'gasoline_car_consumption': GASOLINE_CAR_CONSUMPTION,
    }

    if request.method == "POST":
        data = request.POST
        
        # Request values
        car = data.get('car', 'Invalid Car')
        fuelvalue = float(data.get('value', 0))
        currentkm = float(data.get('currentkm', 0))
        fueltype = data.get('fueltype', 'GAS')

        # Calculated values
        fuelquantity = 0
        possiblekm = 0
        totalkm = 0

        if fueltype == 'GAS':
            fuelquantity = fuelvalue / GASOLINE_PRICE
            possiblekm = round(fuelquantity * GASOLINE_CAR_CONSUMPTION, 2)
        elif fueltype == 'ALC':
            fuelquantity = fuelvalue / ALCOHOL_PRICE
            possiblekm = round(fuelquantity * ALCOHOL_CAR_CONSUMPTION, 2)

        totalkm = currentkm + possiblekm

        default_data.update({
            'success': True,
            'car': car,
            'possiblekm': possiblekm,
            'value': fuelvalue,
            'totalkm': totalkm
        })

    return render(request, 'fuel-form.html', default_data)
