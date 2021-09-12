# agent 계정이 url로 127.0.0.1:8000/agents를 입력해도 못 들어가도록
# custom한 LoginRequiredMixin을 만들꺼

from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrganizerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organizer."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            #권한이 없으면 lead-list 페이지로 감
            return redirect("leads:lead-list")
        return super().dispatch(request, *args, **kwargs)
