from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View

from webapp.forms import AddsForm, CommentsForm
from webapp.models import Adds, Comments
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied



class AddsList(ListView):
    template_name = 'adds/index.html'
    model = Adds
    context_object_name = 'adds'
    paginate_by = 6
    ordering = ['-date_of_publication']

    def get_queryset(self):
        return self.model.objects.filter(status='Published')
class AddsCreate(LoginRequiredMixin, CreateView):
    template_name = 'adds/adds_create.html'
    model = Adds
    form_class = AddsForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:detail_adds', kwargs={'pk': self.object.pk})

class AddsUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'adds/adds_update.html'
    form_class = AddsForm
    model = Adds
    context_object_name = 'adds'

    def has_permission(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.object.status == 'Rejected':
            raise PermissionDenied()
        form.instance.status = 'On_moderated'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:detail_adds', kwargs={'pk': self.object.pk})

class AddsDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'adds/adds_delete.html'
    model = Adds
    success_url = reverse_lazy('webapp:index')

    def has_permission(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = 'On_deleted'
        self.object.save()
        return HttpResponseRedirect(success_url)

class AddsView(DetailView):
    template_name = 'adds/detail.html'
    model = Adds

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.all()

        # if not self.request.user.has_perm('webapp.view_not_moderated_review'):
        #     reviews = reviews.filter(is_moderated=True)

        context['form'] = CommentsForm
        context['comments'] = comments.order_by('-created_at')
        return context

class ListNoModerAdds(PermissionRequiredMixin, ListView):
    model = Adds
    template_name = 'comments/not_moder.html'
    context_object_name = 'adds'
    permission_required = 'webapp.view_not_moderated_adds'


    def has_permission(self):
        return super().has_permission()

    def get_queryset(self):
        return super().get_queryset().filter(status='On_moderated')

class CheckModer(View):
    def get(self, request, *args, **kwargs):
        add = get_object_or_404(Adds, pk=self.kwargs.get('pk'))
        add.status = 'Published'
        add.save()
        response = JsonResponse({'status': add.status})
        return response

class CheckCancelModer(View):
    def get(self, request, *args, **kwargs):
        add = get_object_or_404(Adds, pk=self.kwargs.get('pk'))
        add.status = 'Rejected'
        add.save()
        response = JsonResponse({'status': add.status})
        return response
