from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product
from profiles.models import UserProfile


# @login_required
# def get_wishlist(request):
#     """Lists the users wishlist products"""

#     user = get_object_or_404(UserProfile, user=request.user)
#     wishlist = Wishlist.objects.filter(user=user)

#     template = 'wishlist/wishlist.html'
#     context = {
#         'wishlist': wishlist,
#     }

#     return render(request, template, context)


@login_required
def get_wishlist(request):
    """Lists the users wishlist products"""
    # wishlist = None
    # try:
    #     wishlist = Wishlist.objects.get(user=request.user.userprofile)
    # except Wishlist.DoesNotExist:
    #     pass

    user = get_object_or_404(UserProfile, user=request.user)
    print(user)
    wishlist = Wishlist.objects.filter(user=user)
    print(wishlist)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """Adds product to user wishlist"""
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    redirect_url = request.POST.get('redirect_url')

    wish, _ = Wishlist.objects.get_or_create(user=user)

    wish.products.add(product)
    messages.info(request, f'{product.name} was added to your wishlist')

    return redirect(reverse('product_detail', args=[product.id]))


# @login_required
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

#     if created is True:
#         messages.success(request, f'{product.name} added to your wishlist.')
#     else:
#         messages.info(request, f'{product.name} already in your wishlist.')

#     redirect_url = request.POST.get('redirect_url')

#     return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, product_id):
    """Remove product from user wishlist"""
    wish = Wishlist.objects.get(user=request.user.userprofile)
    product = get_object_or_404(Product, pk=product_id)

    # Remove wish from the wishlist
    wish.products.remove(product)
    messages.info(request, f'{product.name} was removed from your wishlist')

    return redirect(reverse('wishlist'))


# @login_required
# def remove_from_wishlist(request, product_id):
#     """Remove product from user wishlist"""

#     product = get_object_or_404(Product, pk=product_id)
#     user = get_object_or_404(UserProfile, user=request.user)

#     wishlist = Wishlist.objects.filter(user=user, product=product)

#     wishlist.delete()
#     messages.info(request, f'{product.name} deleted from your wishlist.')

#     return redirect(reverse('wishlist'))
