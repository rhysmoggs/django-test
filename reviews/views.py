from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.

@login_required
def add_review(request, product_id):
    """ Allows a user to add a review """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(User, username=request.user)

    if request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.review_author = user
            review.save()
            messages.success(request, 'Thank You! Your review \
                has been added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oops, something went wrong! \
                Please try adding your review again.')

    context = {
        'form': form,
    }

    return render(request, context)

# def product_detail(request, product_id):
#     """ A view to show individual product details """

#     product = get_object_or_404(Product, pk=product_id)

#     context = {
#         'product': product,
#     }

#     return render(request, 'products/product_detail.html', context)


# @login_required
# def add_product(request):
#     """ Add a product to the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, 'Successfully added product!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to add product. Please ensure the form is valid.')
#     else:
#         form = ProductForm()

#     template = 'products/add_product.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)