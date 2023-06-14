# m5-backend-kenzie-social

## Documentação
[documentação](https://kenzie-social-yu5v.onrender.com/api/docs/swagger/)

## Tutorial Inicial:

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Entrar no seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Instale as dependências:
```bash
    pip install -r requirements.txt
```

# Workspace Insominia:
[texto do link](URL do link)

### Pronto agora é só usar as rotas😎
<br>
<br>

# Rotas:
```url
Base Url: 
https://social-kenzie.onrender.com/api/
```
<br>

# User
## POST:

- ### Cadastro:
Criar um novo usuário:
```bash
#Url:
users/
```
<br>

Body:
```javascript
{
    "username": "diego",
    "email": "diego@mail.com",
    "first_name": "Diego",
    "last_name": "Guilherme",
    "password": "1234"
}   
```
<br>

- ### Login:
Logar numa conta existente:

```bash
#url:
users/login
```
<br>

Body:
```javascript
{
    "username": "diego",
    "password": "1234"
}
```
<br>

## GET:
- ### Listar todos os usuário:
```bash
#url:
users/
```

- ### Capturar dados de um usuário:
```bash
#url:
users/<int:pk>/
```
<br>

## PATCH:
- ### Atualizar Dados de um Usuário:
```bash
#url: 
users/<int:pk>/
```
<br>

Body:
```javascript
{
    "username": "diega",
    "email": "diega@mail.com",
    "first_name": "Diega",
    "last_name": "Guilherma",
    "password": "123456"
}
```
<br>

## DELETE

- ### Deletar Usuário:
```bash
#url:
users/<int:pk>/
```

<br>
<br>

# Friendships:
## GET:

- ### Todas as amizades do usuário:
```bash
    #Url:
    friendships/
```
<br>

- ### Todos os convites recebidos:
```bash
    #Url:
    friendships/received/
```
<br>

- ### Todos os convites enviados:

```bash
    #Url:
    friendships/requested/
```
<br>

## POST:

- ### Fazer uma solicitação de amizade

Enviar um convite para outro usuário, passando o id do outro usuário no end point 

```bash
    #Url: pk: id do usuário pedido
    friendships/<int:pk>/
```
<br>

## PATCH:

- ### Aceitar um pedido:

Para aceitar um pedido enviado, terá que passar o id do outro usuário como end point

```bash
    # url:
    friendships/<int:pk>/
```
<br>

## DELETE:

- ### Rejeitar um pedido:
Para rejeitar um pedido enviado, terá que passar o id do outro usuário como end point

```bash
    # url:
    friendships/<int:pk>/
```
<br>
<br>

# POSTS
## GET:
- ### Listar todos os posts:
```bash
    #url:
    posts/
```

- ### Listar um post:
```bash
    # url:
    posts/<int:pk>/
```

- ### Listar post buscando pela timeline:
```bash
    # url
    posts/timeline/
```
<br>

## POST:
- ### Criar um post:
```bash
    # url:
    posts/
```
<br>

Body:
```javascript
{
	"title": "iron-man 3",
	"description": "o melhor filme da marvel",
	"private": false
}
```

## PATCH:
- ### Atulizar post:
```bash
    # url:
    posts/<int:pk>/
```
<br>

Body:
```javascript
{
	"title": "homem aranha",
	"description": "qualquer filme aí",
	"private": true
}
```
<br>

## DELETE:
- ### Deletar post:
```bash
    # url:
    posts/<int:pk>/
```
<br>
<br>


# Followers:
## GET:
- ### Listar seguidores:
```bash
    # url:
    followers/my-followers/
```

- ### Listar pessoas seguidas por você:
```bash
    # url:
    followers/i-follow/
```
<br>

## POST:
- ### Seguir usuário:
```bash
    # url:
    followers/<int:pk>/
```
<br>

## DELETE:
- ### Deixar de seguir usuário:
```bash
    # url:
    followers/<int:pk>/
```
