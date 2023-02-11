from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from webapp.forms import CommentsForm
from webapp.models import Comments, Adds
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class CommentsCreate(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentsForm


    def form_valid(self, form):
        adds = get_object_or_404(Adds, pk=self.kwargs.get('pk'))
        author = self.request.user
        form.instance.author = author
        form.instance.adds = adds
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:detail_adds', kwargs={'pk': self.object.adds.pk})

class DeleteComments(PermissionRequiredMixin, DeleteView):
    model = Comments

    def has_permission(self):
        return self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:detail_adds', kwargs={'pk': self.object.adds.pk})



