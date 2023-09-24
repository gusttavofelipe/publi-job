<p>PubliJob é uma plataforma inovadora que simplifica a busca e candidatura a oportunidades de emprego.</p>
</p>O objetivo é conectar talentos a empresas em crescimento, tornando o processo de recrutamento mais eficiente.</p>

<img src="readme/index.png">
<!-- <img src="readme/vacancy_detail.png">
<img src="readme/register.png">
<img src="readme/login.png">
<img src="readme/profile.png"> -->

### Preparar ambiente

Para executar o projeto, foi utilizado pyenv na versão 3.11.0 do python para o ambiente virtual.

Ao optar por usar pyenv, após a instalação, execute:
```bash
pyenv virtualenv 3.11.0 publi
pyenv activate publi
```

### Banco de dados

Abra seu terminal e acesse o MySQL:
```bash
mysql -u seu_usuario -p
```
Digite sua senha quando solicitado.

<br>
Crie um novo banco de dados para o projeto:

```bash
CREATE DATABASE publijob;
```
<br>
Saia do terminal

```bash
exit
```
<br>

No arquivo settings.py do projeto, em `DATABASES`, substitua as informações de conexão do banco de dados:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'publijob',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',  # ou o endereço do seu servidor
        'PORT': 'porta_escolhida', # deixe em branco para usar a padrão
    }
}
```

<br>
Execute os seguintes comandos para aplicar as migrações ao banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Execução

```bash
python manage.py runserver
```
Visite http://localhost:8000/ ou endereço do seu servidor em seu navegador para verificar se o site está funcionando corretamente.