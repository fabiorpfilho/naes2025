from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .views import CadastroUsuarioView

from django.urls import reverse_lazy

urlpatterns = [
    
    path("login/", LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={"titulo": "Autenticação"}), name="login"),
    
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path("alterar-senha/", PasswordChangeView.as_view(
        template_name='usuarios/login.html',
        extra_context={"titulo": "Alterar minha senha",
        "success_url": reverse_lazy("index")}), 
        name="alterar-senha" , 
),


    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),

]