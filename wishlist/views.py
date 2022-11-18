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


# works for wishlist-works-m2m.html
# @login_required
# def get_wishlist(request):
#     """Lists the users wishlist products"""
#     wishlists = Wishlist.objects.all()

#     for wishlist in wishlists:
#         print(wishlist.products.all())

#     template = 'wishlist/wishlist.html'
#     context = {
#         'wishlist': wishlist,
#     }

#     return render(request, template, context)


@login_required
def get_wishlist(request):
    """Lists the users wishlist products"""

    # wishlists = Wishlist.objects.all()
    # print(wishlists)
    # e = Wishlist.objects.get(id=68)
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)
    user_wishlist = get_object_or_404(Wishlist, user=user)
    print(user_wishlist)
    # wishlist = Wishlist.objects.filter(user=user)
    # print(wishlist)
    # print(wishlist.all())
    # print(wishlist.count())

    # user_wishlist = wishlist.filter(user=user)
    # print(user_wishlist)
    # print(user_wishlist.all())

    # only need these 3 lines
    # wishlists = Wishlist.objects.get()
    # print(wishlists)
    wishlist = user_wishlist.products.all()
    print(user_wishlist.products.all())

    # print(e.products.count())
    # print(e.products.filter(name="Arizona Original Bootcut Jeans"))

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


# this works but no check on duplicates
# @login_required
# def add_to_wishlist(request, product_id):
#     """Adds product to user wishlist"""
#     product = get_object_or_404(Product, pk=product_id)
#     user = get_object_or_404(UserProfile, user=request.user)
#     redirect_url = request.POST.get('redirect_url')

#     wish, _ = Wishlist.objects.get_or_create(user=user)

#     wish.products.add(product)
#     messages.info(request, f'{product.name} was added to your wishlist')

#     return redirect(reverse('product_detail', args=[product.id]))


@login_required
def add_to_wishlist(request, product_id):
    """Adds product to user wishlist"""

    # get current product
    product = get_object_or_404(Product, pk=product_id)
    print(product)

    # get current user
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)

    # get user wishlist otherwise create wishlist
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    print(wishlist)
    print(created)

    # check if product exists in user wishlist
    check_duplicate = bool(Wishlist.objects.filter(products=product))
    print(check_duplicate)

    # if product exists in user wishlist, inform user, otherwise, add to user wishlist
    if check_duplicate:
        messages.info(request, f'{product.name} already in your wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} added to your wishlist.')

    # # get user wishlist
    # get_wishlist = Wishlist.objects.get(user=user)
    # print(get_wishlist)

    # # get products in user wishlist
    # print(get_wishlist.products.all())

    # # check if product is in wishlist
    # check_wishlist = get_wishlist.products.filter(name=product)
    # print(check_wishlist)

    # if product in check_wishlist:
    #     messages.info(request, f'{product.name} already in your wishlist.')
    # else:
    #     get_wishlist.products.add(product)
    #     messages.success(request, f'{product.name} added to your wishlist.')

    return redirect(reverse('product_detail', args=[product.id]))


# def add_to_wishlist(request, product_id):
#     """Adds product to user wishlist"""

#     # get current product
#     product = get_object_or_404(Product, pk=product_id)
#     print(product)

#     # get current user
#     user = get_object_or_404(UserProfile, user=request.user)
#     print(user)

#     # get user wishlist
#     get_wishlist = Wishlist.objects.get(user=user)
#     print(get_wishlist)

#     # get products in user wishlist
#     print(get_wishlist.products.all())

#     # check if product is in wishlist
#     check_wishlist = get_wishlist.products.filter(name=product)
#     print(check_wishlist)

#     if product in check_wishlist:
#         messages.info(request, f'{product.name} already in your wishlist.')
#     else:
#         get_wishlist.products.add(product)
#         messages.success(request, f'{product.name} added to your wishlist.')

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
