from django.shortcuts import render, HttpResponse, redirect
from .forms import RSVPForm

from django.shortcuts import render, redirect

def home_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            will_attend = form.cleaned_data['will_attend']

            # Remove the guest's name from the GuestName model
            guest_name = form.cleaned_data['name']
            guest_name.delete()

            if will_attend == "True":
                form.save()
                return redirect('yes_response_page')
            else:
                return redirect('no_response_page')
    else:
        form = RSVPForm()

    return render(request, 'index.html', {'form': form})





def yes_response_view(request):
    return render(request, 'yes_response.html')

def no_response_view(request):
    return render(request, 'no_response.html')
