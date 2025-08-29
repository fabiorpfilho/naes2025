from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from cadastros.models import Usuario
from .forms import UsuarioCadastroForm
import traceback

class CadastroUsuarioView(CreateView):
    form_class = UsuarioCadastroForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Verifica se o usuário está autenticado e é administrador
        user_is_admin = self.request.user.is_authenticated and self.request.user.groups.filter(name='Administrador').exists()
        kwargs['user_is_admin'] = user_is_admin
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de usuários'
        return context

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        endereco = form.cleaned_data['endereco']
        cpf = form.cleaned_data['cpf']
        telefone = form.cleaned_data['telefone']
        tipo = form.cleaned_data['tipo_usuario']

        url = super().form_valid(form)

        try:
            usuario = Usuario.objects.create(
                nome=nome,
                endereco=endereco,
                telefone=telefone,
                cpf=cpf,
                tipo=tipo,
                usuario=self.object
            )
            grupo, criado = Group.objects.get_or_create(name=tipo)
            self.object.groups.add(grupo)

        except Exception as e:
            self.object.delete()
            print("Erro ao criar usuário relacionado:", str(e))
            traceback.print_exc()
            form.add_error("", f"Houve um problema: {str(e)}")
            return self.form_invalid(form)

        return url