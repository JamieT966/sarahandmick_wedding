from django.shortcuts import render, HttpResponse, redirect
from .forms import RSVPForm

def home_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or wherever you want
    else:
        form = RSVPForm()

    return render(request, 'home.html', {'form': form})