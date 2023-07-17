import os

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from authors.models import Profile
from recipes.models import Recipe
from utils.pagination import make_pagination

PER_PAGE = int(os.environ.get('PER_PAGE', 3))


class ProfileView(TemplateView):
    template_name = 'authors/pages/profile.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            Recipe.objects.filter(
                author=ctx.get('id'),
                is_published=True,
            ).order_by('-id'),
            PER_PAGE
        )
        ctx.update(
            {'recipes': page_obj, 'pagination_range': pagination_range}
        )
        return ctx

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        profile_id = context.get('id')
        profile = get_object_or_404(
            Profile.objects.filter(
                pk=profile_id,
            ).select_related('author'),
            pk=profile_id
        )
        return self.render_to_response({
            **context,
            'profile': profile,
        })
