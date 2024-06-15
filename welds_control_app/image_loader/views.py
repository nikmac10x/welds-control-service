from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Image
from .forms import ImageUploadForm


def image_uploader(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Image(image_file=request.FILES['image_file'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('image_uploader'))
    else:
        form = ImageUploadForm()  # A empty, unbound form

    # Load documents for the list page
    images = Image.objects.all()

    # Render list page with the documents and the form
    return render(request, 'image_uploader.html', {'images': images, 'form': form})
