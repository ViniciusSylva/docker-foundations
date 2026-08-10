# 🐳 Docker — Compose

> 📌 Gerenciamento de múltiplos containers com um único arquivo

---

## 📌 O que é o Docker Compose?

O **Docker Compose** é uma ferramenta que permite **definir e gerenciar múltiplos containers** de uma aplicação utilizando um único arquivo de configuração.

Com ele, você pode subir facilmente serviços como:

* Backend
* Frontend
* Banco de dados

Tudo de forma integrada e automatizada.

---

## ⚙️ Comandos Básicos

### 🔍 Verificar versão

```bash
docker compose version
```

---

### ▶️ Subir containers

```bash
docker compose up
```

📌 O que acontece:

* Lê o arquivo `docker-compose.yml`
* Cria os containers
* Inicia todos os serviços definidos

---

### 📄 Visualizar logs

```bash
docker compose logs
```

📌 Função:

* Exibe os logs de todos os containers

```bash
docker compose logs --help
```

* Mostra opções e filtros disponíveis

---

## 📁 Arquivo de Configuração

O Docker Compose utiliza um arquivo:

* Nome padrão: `docker-compose.yml`
* Linguagem: **YAML**
* Define todos os serviços da aplicação

---

## 🧾 YAML (YAML Ain't Markup Language)

### 📌 O que é?

YAML é uma linguagem de **serialização de dados**, muito usada para:

* Arquivos de configuração
* Definição de serviços

---

### ⚠️ Regras importantes

* Leitura de **cima para baixo**
* Segue uma **ordem lógica**
* Depende de **indentação correta (espaços)**

📌 Erros de indentação quebram o funcionamento.

---

## 🔗 Rede no Docker Compose

Ao executar o Compose, é criada automaticamente uma **rede interna**.

Isso permite que os containers:

* Se comuniquem entre si
* Usem o **nome do serviço como hostname**

📌 Exemplo: um backend pode acessar o banco usando `db` como host.

---

## 🧠 Resumo Rápido

* Gerencia múltiplos containers
* Usa um arquivo `.yml`
* YAML exige indentação correta
* `docker compose up` sobe todos os serviços
* `docker compose logs` ajuda no monitoramento
* Containers se comunicam via rede interna automaticamente
