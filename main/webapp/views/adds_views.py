from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from webapp.forms import AddsForm
from webapp.models import Adds, Comments
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class AddsList(ListView):
    template_name = 'adds/index.html'
    model = Adds
    context_object_name = 'adds'
    paginate_by = 3
    ordering = ['-date_of_publication']

    def get_queryset(self):
        return self.model.objects.filter(status='Published')
class AddsCreate(CreateView):
    template_name = 'adds/adds_create.html'
    model = Adds
    form_class = AddsForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:detail_adds', kwargs={'pk': self.object.pk})

class AddsUpdate(UpdateView):
    template_name = 'adds/adds_update.html'
    form_class = AddsForm
    model = Adds
    context_object_name = 'adds'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('webapp:detail_adds', kwargs={'pk': self.object.pk})

class AddsDelete(DeleteView):
    template_name = 'adds/adds_delete.html'
    model = Adds
    success_url = reverse_lazy('webapp:index')
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = 'On_deleted'
        self.object.save()
        return HttpResponseRedirect(success_url)

class AddsView(DetailView):
    template_name = 'adds/detail.html'
    model = Adds

