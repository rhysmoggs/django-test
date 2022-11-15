from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product
from profiles.models import UserProfile


@login_required
def get_wishlist(request):
    """Lists the users wishlist products"""

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user=user)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


# def add_to_wishlist(request, product_id):
#     """Adds product to user wishlist"""

#     product = get_object_or_404(Product, pk=product_id)
#     print(product)

#     user = get_object_or_404(UserProfile, user=request.user)
#     print(user)

#     obj, created = Wishlist.objects.get_or_create(
#         product=product,
#         user=user
#     )
#     print(obj, created)
#     print(obj)
#     print(created)

#     redirect_url = request.POST.get('redirect_url')

#     return redirect(reverse('product_detail', args=[product.id]))


def add_to_wishlist(request, product_id):
    """Adds product to user wishlist"""

    product = get_object_or_404(Product, pk=product_id)
    print(product)

    user = get_object_or_404(UserProfile, user=request.user)
    print(user)

    #rename obj to wishlist. check if necessary to use created?
    #works well, just need to figure out a way to add all to one list. create wishlist list here
    #or in Wishlist model.py?
    obj, created = Wishlist.objects.get_or_create(
        product=product,
        user=user
    )
    print(obj, created)
    print(obj)
    print(created)

    if created is True:
        messages.success(request, f'{product.name} added to your wishlist.')
    else:
        messages.info(request, f'{product.name} already in your wishlist.')

    redirect_url = request.POST.get('redirect_url')

    return redirect(reverse('product_detail', args=[product.id]))


def remove_from_wishlist(request, product_id):
    """Remove product from user wishlist"""

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    wishlist = Wishlist.objects.filter(user=user, product=product)

    wishlist.delete()
    messages.error(request, f'{product.name} deleted from your wishlist.')

    return redirect(reverse('wishlist'))
