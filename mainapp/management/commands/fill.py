import json

from django.core.management import BaseCommand


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстурв с категориями
        pass

    @staticmethod
    def json_read_products():
        with open('fixtures/product_data.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        return products
