from django.test import TestCase
from .forms import ReviewForm


# Create your tests here.


class TestReviewForm(TestCase):

    def test_item_name_is_required(self):
        form = ReviewForm({'review_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_title', form.errors.keys())
        self.assertEqual(form.errors['review_title'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ReviewForm({'review_title': 'Test Review Title'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ['review_title', 'review_text', 'review_rating'])
        # self.assertEqual(form.Meta.fields, (('review_title')))
