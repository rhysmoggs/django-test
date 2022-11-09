from django import forms
from .models import Review


# class ReviewForm(forms.ModelForm):
#     """ ReviewForm to allow users to add reviews """
#     class Meta:
#         model = Review
#         fields = ('review_title', 'review_text', 'review_rating')

#     def __init__(self, *args, **kwargs):
#         super(ReviewForm, self).__init__(*args, **kwargs)
#         self.fields['review_text'].label = "Review"


class ReviewForm(forms.ModelForm):
    """ ReviewForm to allow users to add reviews """
    class Meta:
        model = Review
        fields = ['review_title', 'review_text', 'review_rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'ya ya ya',
            'review_text': 'la la Code',
            'review_rating': 'numbers',
        }
        labels = {
            'review_title': 'label title test',
            'review_text': 'review text label test',
            'review_rating': 'label test rating',
        }

        # for field in self.fields:
        #     self.fields[field].label = labels[field] + "yaya"
        # self.fields['review_text'].label = "Write your Review:"
        self.fields['review_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = labels[field] + "__tester"
