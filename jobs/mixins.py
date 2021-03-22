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
        return super().form_valid(form)

class RevicerMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            self.obj = form.save(commit=False)
            self.obj.revicer = object.author
        # else:
        #     self.obj = form.save(commit=False)
        #     self.obj.author = self.request.user

        #     if not self.obj.status == 'i':
        #         self.obj.status = 'i'
        return super().form_valid(form)
