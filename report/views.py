from django.shortcuts import render
import json
# from django.shortcuts import render
from .forms import DateTimeForm
from django.shortcuts import render, redirect
from .forms import DateTimeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def city_list(request):
    with open('report/kanini.json') as file:
        cities_data = json.load(file)
    return render(request, 'report/city_list.html', {'cities': cities_data})


# @login_required
# def datetimepicker_view(request):
#     if request.method == 'POST':
#         form = DateTimeForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#
#             # Print form data for debug
#             form.save()  # Save the form data to the model
#             return redirect('city_list')  # Redirect to the
#     else:
#         form = DateTimeForm()
#     return render(request, 'report/city_list.html', {'form': form})


def datetime_view(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        print(f"Date 1: {date1}")
        print(f"Date 2: {date2}")

    return render(request, 'report/city_list.html')
