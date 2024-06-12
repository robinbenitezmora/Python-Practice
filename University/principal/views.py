from base.base_admin_permissions import BaseAdminUsersAdSe

# ---- Disciplines ---- #
class DisciplineNewView(BaseAdminUsersAdSe, CreateView):
    model = Discipline
    template_name = 'principal/discipline_new.html'
    form_class = DisciplineForm
    success_url = reverse_lazy('disciplines_new')
    success_message = 'New course successfully registered'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['disciplines'] = Discipline.objects.all()

        return context  

class DisciplineUpdateView(BaseAdminUsersAdSe, UpdateView):
    model = Discipline
    template_name = 'principal/discipline_update.html'
    form_class = DisciplineForm
    success_url = reverse_lazy('disciplines')
    success_message = 'Course successfully updated'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['disciplines'] = Discipline.objects.all()

        return context

class DisciplineListView(BaseAdminUsersAdSe, ListView):
    model = Discipline
    template_name = 'principal/discipline_list.html'
    context_object_name = 'disciplines'
    ordering = ['discipline_name', 'discipline_teacher']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['disciplines'] = Discipline.objects.all()

        return context
