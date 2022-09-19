import stripe
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView

from cartapp.models import Item
from stripe_pay.settings import STRIPE_API_KEY


class ItemList(ListView):
    model = Item
    context_object_name = 'items'   # ваше собственное имя переменной контекста в шаблоне
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'cartapp/item_list.html'


class ItemDetail(DetailView):
    model = Item
    template_name = 'cartapp/item_detail.html'



def buy(request, pk):
    stripe.api_key = STRIPE_API_KEY
    item = Item.objects.get(id=pk)

    session = stripe.checkout.Session.create(
        cancel_url=request.build_absolute_uri(reverse('item', args=[pk])),
        success_url=request.build_absolute_uri(reverse('item', args=[pk])),
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.format_price(),
            },
            'quantity': 1,
        }],
        mode="payment",
    )
    return redirect(session.url, code=303)



