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


def add_to_wishlist(request, product_id):
    """Adds product to user wishlist"""

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    redirect_url = request.POST.get('redirect_url')

    if Wishlist.objects.filter(product=product, user=user).exists():
        print(Wishlist.objects.filter(product=product, user=user).exists())
        messages.info(request, f'{product.name} already in your wishlist.')
    # elif wishlist:
    #     Wishlist.objects.create(
    #         user=user,
    #         product=product
    #     )
    else:
        wishlist, created = Wishlist.objects.get_or_create(user=user, product=product)
        # wishlist = Wishlist.objects.filter(user=user)
        wishlist.save()
        messages.success(request, f'{product.name} added to your wishlist.')

    # return redirect(redirect_url)
    return redirect(reverse('product_detail', args=[product.id]))


def remove_from_wishlist(request, product_id):
    """Remove product from user wishlist"""

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    wishlist = Wishlist.objects.filter(user=user, product=product)

    wishlist.delete()
    messages.error(request, f'{product.name} deleted from your wishlist.')

    return redirect(reverse('wishlist'))