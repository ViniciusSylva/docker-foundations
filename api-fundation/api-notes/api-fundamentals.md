# 🌐 REST e APIs

## 📌 REST

**REST** significa **Representational State Transfer**.

O protocolo **HTTP**, que é onde a internet "roda", é um design **stateless** (sem estado).

Isso significa que ele **não guarda dados**.

É como se, sempre que você fosse cumprimentar seus amigos, vocês precisassem se apresentar novamente, pois nenhum de vocês guarda dados.

Quando você cria o login em um site, esse login é salvo através de um **cookie** ou através de um banco de dados no seu navegador. Caso contrário, toda vez que você abrisse o site, precisaria fazer login novamente.

O REST coloca toda a responsabilidade de **lembrar os dados no cliente**, como seu navegador, computador, aplicação etc.

## 🔄 RESTful

No fim das contas, é a mesma coisa.

Estamos falando da criação de uma **interface de comunicação utilizando puramente HTTP**.

**API** = basicamente uma interface de comunicação de uma aplicação de forma programática.

As APIs são criadas utilizando padrões de design chamados **RESTful**.

Essas são as chamadas **APIs REST**.

---

## 🔗 Endpoints

Para entender **endpoints**, podemos falar de gramática portuguesa.

Na língua portuguesa temos substantivos, verbos, pronomes etc. Ao todo, são 10 classes gramaticais.

Para criar bons endpoints, você precisa saber o que é **substantivo** e **verbo**, pois são os conceitos usados para criá-los.

### Exemplos de endpoints

**Coleção:**

```text
/api/v1/produtos
```

**Individual:**

```text
/api/v1/produtos/42
```

### Verbos HTTP em endpoints

* **HTTP PUT:** atualizar um recurso.
* **HTTP GET:** pegar uma coleção ou indivíduo.
* **HTTP POST:** postar/criar um novo recurso.
* **HTTP DELETE:** deletar um recurso existente.

### GET

```http
GET /api/v1/produtos
```

Traz uma lista de todos os produtos.

### POST

O **POST** é sempre utilizado na **coleção** e não individualmente. Serve para adicionar/criar um novo recurso.

### PUT

Serve para atualizar um recurso existente e nunca deve ser utilizado na coleção, e sim em um recurso.

### DELETE

Serve para excluir um recurso na coleção. Nunca deve ser efetuado para a coleção inteira.

---

## 📦 Resources

Na API REST temos um elemento chamado **resources (recursos)**.

Um **resource** pode ser um **model**.

É com esses recursos que iremos realizar operações **CRUD**:

* **Create**
* **Retrieve**
* **Update**
* **Delete**

Fazemos isso através de **URIs específicas**.

Essas URIs são os **endpoints**.

---

## 📤 Requests

Quando você pega seu navegador e entra em algum site, está fazendo um **HTTP request (requisição HTTP)**.

Você pode alterar essas requisições, por exemplo:

```text
/api/v1/produtos?order=desc&limit=10
```

Nosso endpoint vai até:

```text
/api/v1/produtos
```

Tudo após o ponto de interrogação (`?`) é composto por um conjunto de **chave e valor**.

**Chave:**

```text
order
```

**Valor:**

```text
desc
```

Eles vêm separados por `&`.

Esse conjunto é conhecido como **query strings**.

---

## 📋 Accept

Especifica o formato do arquivo que o **requester (solicitante)** quer.

```http
Accept: application/json
```

Especifica o tipo de arquivo que ele espera.

---

## 🔢 Versionamento da API

```text
/api/v1/produtos
```

O **v1** indica a versão da aplicação.

Podemos atualizar e, por exemplo, criar uma **v2** que tenha ações que não existam na v1.

É importante lembrar que clientes podem estar usando a **v2**, mas ainda assim pode haver clientes usando a **v1**.

Nesse caso, a v1 não deve ser desabilitada até que todo mundo tenha migrado para a v2.

---

## 📥 Responses

O usuário (PC) enviou uma **request**, e nós (servidor) enviamos uma **response**.

Em uma response são enviados os dados e, em alguns casos, cabeçalhos.

Exemplos:

```text
200 = OK
404 = Page Not Found
```

---

## 🚦 HTTP Status Codes

Os **HTTP Status Codes** são divididos em categorias:

* **1XX:** informação.
* **2XX:** sucesso.
* **3XX:** houve algum redirecionamento.
* **4XX:** erro do cliente; o cliente enviou algo errado ou não conseguiu encontrar o recurso.
* **5XX:** erro no servidor; indica que o servidor não conseguiu processar algo ou ocorreu algum erro do lado do servidor.

### Faixas de status

**200–299:** OK / sucesso.

**300–399:** a requisição foi entendida, mas o recurso está em outro local.

**400–499:** erro do lado de quem solicitou. Por exemplo, uma URI informada errada ou uma URI requisitada com `GET` quando deveria ser `POST`.

Exemplos:

```text
403
405
```

**500–599:** indica que a requisição foi realizada, mas houve algum erro do lado do servidor.

---

## 📄 XML e JSON

São **formatos de arquivos**.

O **XML** era muito utilizado antigamente e, hoje em dia, o **JSON** é muito utilizado.

**JSON** significa **JavaScript Object Notation**.

> Uma API que não consegue suprir a demanda é tão ruim quanto não ter nenhuma API.

---

## 🔐 Segurança de API

### ⚡ Cache

Um cliente faz uma requisição. Se o servidor de cache não tinha os dados, ele vai até o servidor, pega os dados, coloca no cache e entrega para o cliente.

Com isso, o próximo cliente a procurar os mesmos dados vai pegá-los do **cache** e não precisará ir diretamente ao servidor.

Ferramentas como **Redis** ou **Memcache** podem ser usadas para isso.

Nem todo cache vai salvar sua API. É preciso tomar cuidado para ela não ser inundada de requisições, pois você pode receber mais requisições do que o servidor pode suportar.

Seu servidor não pode receber mais requisições do que aguenta.

Pode acontecer de, ao passar do limite, as próximas requisições serem rejeitadas.

---

## 🔑 Autenticação e Autorização

A forma mais comum é com **tokens**, uma "chave criptográfica que identifica o cliente".

Quando o cliente cria uma conta na sua aplicação, ele recebe uma chave (**Public Key**) e, através dessa chave (token), ele envia a informação no cabeçalho ou no corpo da requisição para realizar a autenticação.

### 👤 Autenticação

**Autenticação:** é **quem você é**.

> "Você se autenticou aqui? Você é um cliente nosso? Eu não te conheço, você não pode fazer uso da nossa API."

### 🛡️ Autorização

**Autorização:** é **o que você pode fazer**.

> "Você pode criar? Você pode deletar?"

### Ordem

Primeiro fazemos a **autenticação** e depois a **autorização**.
