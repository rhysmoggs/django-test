from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.contrib.auth.models import User

# Create your views here.

@login_required
def add_review(request, product_id):
    """ A view to allow users to create product reviews """
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm

    if request.method == 'POST':
        # Filters reviews based on session user
        previous_review = Review.objects.filter(
            author=request.user, product=product,
        ).exists()
        if previous_review:
            # If previous review error message displayed
            messages.error(request,
                           f'You have already left a comment'
                           f'for {product.name}')
        else:
            # if no previous review 
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.review_author = User.objects.get(
                    username=request.user.username)
                review.product = product
                review.save()
                messages.success(request, 'Successfully added review!')
                return redirect(reverse(
                    'product_detail', kwargs={"product_id": product.id}))
            else:
                messages.error(request,
                               'Failed to add review.'
                               'Please ensure the form is valid')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)
