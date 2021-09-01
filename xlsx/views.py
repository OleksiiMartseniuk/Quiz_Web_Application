from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View
from .forms import XlsxModelForm
from .models import Xlsx
from .utils import AddQuizMixin
from django.contrib import messages


class UploadFileView(PermissionRequiredMixin, AddQuizMixin, View):
    permission_required = ('xlsx.view_xlsx', 'xlsx.add_xlsx')

    def get(self, request):
        form = XlsxModelForm(request.POST or None, request.FILES or None)
        return render(request, 'xlsx/upload.html', {'form': form})

    def post(self, request):
        form = XlsxModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.author = request.user
            form_obj.save()
            form_obj = XlsxModelForm()
            obj = Xlsx.objects.get(activated=False, author=request.user)
            error = self.add_quiz(obj)
            if error:
                messages.add_message(request, messages.INFO, 'Adding successfully')
            else:
                messages.add_message(request, messages.ERROR, 'Incorrectly filled file!')
        return render(request, 'xlsx/upload.html', {'form': form_obj})

