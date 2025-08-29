from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from cadastros.models import TipoUsuario

class UsuarioCadastroForm(UserCreationForm):
    nome = forms.CharField(required=True, max_length=255)
    endereco = forms.CharField(required=True, max_length=50, label="Endereço")
    cpf = forms.CharField(required=True, max_length=14, label="CPF")
    telefone = forms.CharField(required=True, max_length=20, label="Telefone")
    tipo_usuario = forms.ChoiceField(
        choices=TipoUsuario.choices,
        label="Tipo de usuário",
        required=False
    )
    email = forms.EmailField(required=True, help_text="Informe um email válido.")

    def __init__(self, *args, user_is_admin=False, **kwargs):
        super().__init__(*args, **kwargs)
        # Se o usuário não for admin, remove o campo tipo_usuario do formulário
        if not user_is_admin:
            del self.fields['tipo_usuario']

    class Meta:
        model = User
        fields = ['nome', 'endereco', 'telefone', 'cpf', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        # Se tipo_usuario não estiver presente (usuário não admin), define como Cliente
        if 'tipo_usuario' not in cleaned_data or not cleaned_data['tipo_usuario']:
            cleaned_data['tipo_usuario'] = TipoUsuario.CLIENTE
        return cleaned_data