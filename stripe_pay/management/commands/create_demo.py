from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from cartapp.models import Item


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(
                username='admin',
                password='admin',
                is_active=True,
                is_superuser=True
            )
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')

        if Item.objects.count() == 0:
            item = Item.objects.create(
                name='Demo item',
                description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.',
                price=10000,
            )
            item.save()
        else:
            print('Item can only be initialized if no Items exist')
