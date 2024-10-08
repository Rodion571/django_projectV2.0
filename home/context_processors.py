from lib2to3.fixes.fix_input import context

from .models import FooterItem

def footer_items(request):
    context = {}
    follow_us_items = []

    items = FooterItem.objects.all()

    for item in items:
        if item.item_title == 'Address':
            context['address'] = item
        elif item.item_title == 'Reservations':
            context['reservations'] = item
        elif item.item_title == 'Opening Hours':
            context['opening_hours'] = item
        elif item.item_title == 'Follow Us' and item.item_slug != 'social_media':
            follow_us_items.append(item)

    context['follow_us'] = follow_us_items

    return {
        'footer_items': context
    }