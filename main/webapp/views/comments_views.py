from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from webapp.forms import CommentsForm
from webapp.models import Comments, Adds
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class CommentsCreate(CreateView):
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

class DeleteComments(DeleteView):
    model = Comments

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:detail_adds', kwargs={'pk': self.object.adds.pk})


# class DeleteReviewDeleteView):
#     template_name = 'co'
#     model = Comments
#     permission_required = 'webapp.delete_review'
#
#     def get_success_url(self):
#         return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})

# class ListNoModeratedReviewView(PermissionRequiredMixin, ListView):
#     model = Review
#     template_name = 'Review_html/not_moder.html'
#     context_object_name = 'reviews'
#     permission_required = 'webapp.view_not_moderated_review'
#
#     def get_queryset(self):
#         return super().get_queryset().filter(is_moderated=False)