# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse, response

from .models import Manufacturer, Product


def product_list(request):
    """return product list in jsonformat"""

    products = Product.objects.all()
    # data = {'products': list(products.values("pk", "name"))}

    # retreve manufacturers objects data as dictionary then convert list then
    # save as dictionary in data variable
    data = {'products': list(products.values())}
    response = JsonResponse(data)

    return response


def product_detail(reauest, id):
    """Return JsonResponse about product detail"""

    try:
        product = Product.objects.get(pk=id)
        data = {
            'product':
            {
                'name': product.name,
                'manufacturer': product.manufacturer.name,
                'description': product.description,
                'photo': product.photo.url,
                'price': product.price,
                'shipping_cost': product.shipping_cost,
                'quantitiy': product.quantitiy
            }
        }
        # Convert aour Dictionary data to Jasonresponse format
        response = JsonResponse(data)

    except Product.DoesNotExist:
        response = JsonResponse(
            {
                'error': {
                    'code': 404,
                    'message': 'Product Does not exist'
                }
            },
            status=404
        )
    return response


def manufacturer_list(request):
    """return list of active manufacturer in jsonresponse"""

    manufacturers = Manufacturer.objects.filter(active=True)

    # retreve manufacturers objects data as dictionary then convert list then
    # save as dictionary in data variable
    data = {
        'manufacturers': list(manufacturers.values())
    }

    return JsonResponse(data)


def manufacturer_detail(request, id):
    """Return detail of specific manufacturer in JsonResponse"""

    try:
        manufacturer = Manufacturer.objects.get(pk=id)
        data = {
            'manufacturer': {
                'name': manufacturer.name,
                'location': manufacturer.location,
                'active': manufacturer.active,
                'products': list(manufacturer.porducts.all().values())
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'manufacturer does not exist'
            }
        }, status=404)

    return response
