class FormUserMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            form.save()

        return super().form_valid(form)
