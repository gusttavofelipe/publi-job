 <!-- Instalar pyenv:
    mac
    linux

criar ambiente virtual:
    pyenv virtualenv 3.12 publijob
    pyenv activate publijob -->

# Ambiente virtual
Este projeto ultiliza a versão **3.12** do python, ultilize [pyenv](https://gist.github.com/trongnghia203/9cc8157acb1a9faad2de95c3175aa875) para instalar a respectiva versão

#### Após a instalação do Python execute:
```shell
pyenv virtualenv 3.12 publijob
```
Para criar o ambiente virtual

```shell
pyenv virtualenv 3.12 publijob
```
Para atvar o ambiente virtual

# Instalar dependencias
#### Certifique-se de que seu ambiente virtual esteja ativo e execute:
```shell
make dependencies
```

# Banco de dados
Crie um arquivo .env e insira as credenciais de local.env

#### Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/ubuntu/) e [docker-compose](https://docs.docker.com/compose/install/linux/) instalados e execute:
```shell
docker-compose up -d
```

# Executar projeto
#### Após as etapas anteriores serem bem sucedidas execute:
Para executar as migrações no banco de dados
```shell
make migrations
```
Subir o site
```shell
make runserver
```
