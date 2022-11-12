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
        fields = ['review_text', 'review_rating']

    def __init__(self, *args, **kwargs):
        """ Add labels and required attribute if needed """
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_text': 'la la Code',
        }
        labels = {
            'review_text': 'Product Review',
            'review_rating': 'Rating',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
            # if self.fields[field].required is not True:
            #     placeholder = placeholders[field]
            # else:
            #     placeholder = " "

        # for field in self.fields:
        #     self.fields[field].label = labels[field] + "yaya"
        # self.fields['review_text'].label = "Write your Review:"

        # self.fields['review_text'].widget.attrs['autofocus'] = True

        # for field in self.fields:
        #     if self.fields[field].required:
        #         placeholder = f'{placeholders[field]} *'
        #     else:
        #         placeholder = placeholders[field]
        #     self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
        #     self.fields[field].label = labels[field] + " "

        # for field in self.fields:
        #     if field != 'review_rating':
        #         if self.fields[field].required:
        #             placeholder = f'{placeholders[field]} *'
        #         else:
        #             placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
        #     self.fields[field].label = labels[field] + " "
