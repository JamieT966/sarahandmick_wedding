from django.shortcuts import render, redirect
from .forms import RSVPForm

def home_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            # Assuming the form's save method returns the instance
            # If not, you should adjust to get the saved instance
            instance = form.save()

            # Check if any guest is attending
            guests_attending = any([
                instance.will_attend_1,
                instance.will_attend_2,
                instance.will_attend_3,
                instance.will_attend_4,
                instance.will_attend_5
            ])

            if guests_attending:
                return redirect('yes_response_page')  # update with your actual view/route
            else:
                return redirect('no_response_page')  # update with your actual view/route

        else:
            # If the form is not valid, render the form again with errors
            return render(request, 'index.html', {'form': form})

    else:
        form = RSVPForm()

    return render(request, 'index.html', {'form': form})

def yes_response_view(request):
    return render(request, 'yes_response.html')

def no_response_view(request):
    return render(request, 'no_response.html')
