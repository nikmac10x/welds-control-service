from django import forms


class ImageUploadForm(forms.Form):
    image_file = forms.ImageField(
        label='Select a image',
        help_text='max. 42 megabytes'
    )
