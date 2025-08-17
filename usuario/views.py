from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from cadastros.models import Usuario
from .forms import UsuarioCadastroForm
import traceback

# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Registro de usuários'}


    def form_valid(self, form):
        
        # Pega os dados do form, antes de criar o objeto
        nome = form.cleaned_data['nome']
        endereco = form.cleaned_data['endereco']
        cpf = form.cleaned_data['cpf']
        telefone = form.cleaned_data['telefone']
        tipo = form.cleaned_data['tipo_usuario']

        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        
        # Usa um try para não correr o risco de cadastrar o usuário
        # e acontecer um erro durante o cadastro de Aluno ou Servidor
        # e o User ficar sem relação "travando" o uso daqueles dados
        try:
            usuario = Usuario.objects.create(
                nome=nome,
                endereco=endereco,
                telefone=telefone,
                cpf=cpf,
                tipo=tipo,
                usuario=self.object  # self.object é o User criado pelo form
            )
            # Busca ou cria um grupo com esse nome
            if tipo == "Cliente":
                # Se for Cliente, cria o grupo Cliente
                grupo, criado = Group.objects.get_or_create(name='Cliente')
                # Acessa o objeto criado e adiciona o usuário no grupo acima
                self.object.groups.add(grupo)

            elif tipo == "Administrador":
                # Se for Servidor, cria o grupo Servidor
                grupo, criado = Group.objects.get_or_create(name='Administrador')
                # Acessa o objeto criado e adiciona o usuário no grupo acima
                self.object.groups.add(grupo)

        # Caso de algum problema na criação de Aluno ou Servidor
        except Exception as e:
            # Exclui o User para não ficar órfão
            self.object.delete()
            # Loga o erro completo no terminal
            print("Erro ao criar usuário relacionado:", str(e))
            traceback.print_exc()
            # Adiciona erro no form
            form.add_error("", f"Houve um problema: {str(e)}")
            return self.form_invalid(form)

        # Retorna a URL de sucesso
        return url
