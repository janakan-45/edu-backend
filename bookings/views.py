from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import Booking

@csrf_exempt
def create_booking(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Create booking record
            booking = Booking.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                phone_number=data.get('phone_number'),
                destination=data.get('destination'),
                start_date=data.get('start_date'),
                office=data.get('office'),
                counselling_mode=data.get('counselling_mode')
            )

            # Send confirmation email
            subject = 'Consultation Request Received - EduGlobe'
            message = f"""
Dear {booking.first_name},

Thank you for your interest in studying in {booking.destination}. We have received your request for a free consultation.

One of our expert counsellors from our {booking.office} office will be in touch with you shortly to assist you with your study abroad journey.

Your Details:
Name: {booking.first_name} {booking.last_name}
Mobile: {booking.phone_number}
Destination: {booking.destination}
Preferred Start: {booking.start_date}
Mode: {booking.counselling_mode}

Best regards,
The EduGlobe Team
            """
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [booking.email],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            return JsonResponse({'message': 'Booking created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
