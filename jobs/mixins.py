from django.shortcuts import get_object_or_404
from .models import Jobs
class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user

            if not self.obj.status == 'i':
                self.obj.status = 'i'
                
            if self.obj.is_expire == True:
               self.obj.status = 'b'    
        return super().form_valid(form)

class AuthorAccessMixin():
    def dispatch(self, request,pk, *args, **kwargs):
        job = get_object_or_404(Jobs, pk=pk)
        if job.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('یافت نشد')