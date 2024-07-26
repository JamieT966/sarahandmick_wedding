from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RSVPForm

def home_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            instance = form.save()

            # Check if any guest is attending
            guests_attending = any([
                instance.will_attend_1,
                instance.will_attend_2,
                instance.will_attend_3,
                instance.will_attend_4,
                instance.will_attend_5
            ])

            subject = "RSVP Confirmation"
            # Initialize the message content
            message_parts = []

            def get_dietary_info(dietary_requirements, other_dietary_input):
                # Collect dietary requirements
                dietary_info = ', '.join(d.name for d in dietary_requirements.all()).strip()
                # If dietary_info and other_dietary_input are empty, use 'None'
                if not dietary_info and not other_dietary_input:
                    return "None"
                elif dietary_info and other_dietary_input:
                    return f"{dietary_info}, {other_dietary_input}"
                elif dietary_info:
                    return dietary_info
                else:
                    return other_dietary_input

            # Guest 1
            if instance.will_attend_1:
                message_parts.append(
                    f"Guest Name: {instance.name_1}\n"
                    f"Coming to the Wedding: {'Yes'}\n"
                    f"Dietary Requirements: {get_dietary_info(instance.dietary_requirements_1, instance.other_dietary_input_1)}\n"
                    f"Attending Day 2: {instance.attending_day2_1}\n"
                )
            elif instance.name_1:
                message_parts.append(
                    f"Guest Name: {instance.name_1}\n"
                    f"Coming to the Wedding: {'No'}\n"
                )

            # Guest 2
            if instance.will_attend_2:
                message_parts.append(
                    f"\nGuest Name: {instance.name_2}\n"
                    f"Coming to the Wedding: {'Yes'}\n"
                    f"Dietary Requirements: {get_dietary_info(instance.dietary_requirements_2, instance.other_dietary_input_2)}\n"
                    f"Attending Day 2: {instance.attending_day2_2}\n"
                )
            elif instance.name_2:
                message_parts.append(
                    f"\nGuest Name: {instance.name_2}\n"
                    f"Coming to the Wedding: {'No'}\n"
                )
            
            # Guest 3
            if instance.will_attend_3:
                message_parts.append(
                    f"\nGuest Name: {instance.name_3}\n"
                    f"Coming to the Wedding: {'Yes'}\n"
                    f"Dietary Requirements: {get_dietary_info(instance.dietary_requirements_3, instance.other_dietary_input_3)}\n"
                    f"Attending Day 2: {instance.attending_day2_3}\n"
                )
            elif instance.name_3:
                message_parts.append(
                    f"\nGuest Name: {instance.name_3}\n"
                    f"Coming to the Wedding: {'No'}\n"
                )
            
            # Guest 4
            if instance.will_attend_4:
                message_parts.append(
                    f"\nGuest Name: {instance.name_4}\n"
                    f"Coming to the Wedding: {'Yes'}\n"
                    f"Dietary Requirements: {get_dietary_info(instance.dietary_requirements_4, instance.other_dietary_input_4)}\n"
                    f"Attending Day 2: {instance.attending_day2_4}\n"
                )
            elif instance.name_4:
                message_parts.append(
                    f"\nGuest Name: {instance.name_4}\n"
                    f"Coming to the Wedding: {'No'}\n"
                )
            
            # Guest 5
            if instance.will_attend_5:
                message_parts.append(
                    f"\nGuest Name: {instance.name_5}\n"
                    f"Coming to the Wedding: {'Yes'}\n"
                    f"Dietary Requirements: {get_dietary_info(instance.dietary_requirements_5, instance.other_dietary_input_5)}\n"
                    f"Attending Day 2: {instance.attending_day2_5}\n"
                )
            elif instance.name_5:
                message_parts.append(
                    f"\nGuest Name: {instance.name_5}\n"
                    f"Coming to the Wedding: {'No'}\n"
                )
            
            # Music Requests
            message_parts.append(f"\nMusic Requests: {instance.music_requests}\n")

            # Join all parts into a single message
            message = "\n".join(message_parts)
            # Send notification email
            try:
                send_mail(
                    subject,
                    message,
                    'no-reply@mcgettricklynders.com',
                    ['jamietarpey@gmail.com'],
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            if guests_attending:
                return redirect('yes_response_page')
            else:
                return redirect('no_response_page')

        else:
            return render(request, 'index.html', {'form': form})

    else:
        form = RSVPForm()

    return render(request, 'index.html', {'form': form})

def yes_response_view(request):
    return render(request, 'yes_response.html')

def no_response_view(request):
    return render(request, 'no_response.html')
