from django import template
from django.utils import timezone
from bookings.models import Booking
from django.db.models import Count
from django.db.models.functions import TruncDay
import json
from datetime import timedelta

register = template.Library()

@register.simple_tag
def get_unread_notifications():
    # Assuming bookings created in the last 24 hours are "new" notifications
    # In a real app, you might have a 'read' status field.
    last_24_hours = timezone.now() - timedelta(days=1)
    return Booking.objects.filter(created_at__gte=last_24_hours).order_by('-created_at')

@register.simple_tag
def get_booking_stats():
    # Get bookings for the last 7 days for the graph
    end_date = timezone.now()
    start_date = end_date - timedelta(days=6)  # 7 days including today
    
    # Initialize dictionary with 0 counts for the last 7 days
    stats_dict = {}
    for i in range(7):
        day = (start_date + timedelta(days=i)).date()
        stats_dict[day] = 0

    # Fetch actual data
    data = Booking.objects.filter(created_at__date__range=(start_date.date(), end_date.date())) \
        .annotate(date=TruncDay('created_at')) \
        .values('date') \
        .annotate(count=Count('id')) \
        .order_by('date')
        
    # Update stats with actual counts
    for entry in data:
        # TruncDay returns datetime, convert to date
        day_date = entry['date'].date()
        if day_date in stats_dict:
            stats_dict[day_date] = entry['count']
            
    # Prepare lists for Chart.js
    labels = []
    counts = []
    for date_key, count in stats_dict.items():
        labels.append(date_key.strftime('%d %b')) # Format: 06 Feb
        counts.append(count)
        
    return json.dumps({
        'labels': labels,
        'data': counts
    }, default=str)

@register.simple_tag
def get_total_bookings_count():
    return Booking.objects.count()

@register.simple_tag
def get_recent_activity():
    return Booking.objects.order_by('-created_at')[:5]
