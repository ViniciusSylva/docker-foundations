# 🐳 Docker — Images Workflow

> 📌 Comandos focados em criação, otimização e distribuição de imagens

---

## 🏗️ Build de Imagens

```bash
# Build padrão
docker build -t my-image .

# Build com versão (tag)
docker build -t my-image:1.0 .

# Build sem cache (forçar rebuild)
docker build --no-cache -t my-image .

# Build especificando Dockerfile
docker build -f Dockerfile.dev -t my-image .
```

---

## 🖼️ Gerenciamento de Imagens

```bash
# Listar imagens
docker images

# Remover imagem
docker rmi my-image

# Remover imagem forçando
docker rmi -f my-image

# Remover imagens não utilizadas
docker image prune
```

---

## 🏷️ Tags (Versionamento)

```bash
# Criar nova tag
docker tag my-image my-user/my-image:1.0

# Tag latest
docker tag my-image my-user/my-image:latest
```

---

## ☁️ Compartilhamento (Docker Hub)

```bash
# Login no Docker Hub
docker login

# Enviar imagem
docker push my-user/my-image:1.0

# Baixar imagem
docker pull my-user/my-image:1.0
```

---

## 💾 Exportar e Importar Imagens

```bash
# Salvar imagem em arquivo
docker save -o my-image.tar my-image

# Carregar imagem
docker load -i my-image.tar
```

---

## ⚙️ Dockerfile na Prática

### 📌 Instruções principais

```Dockerfile
FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

ENV PORT=3000

EXPOSE 3000

CMD ["npm", "start"]
```

---

## 👤 Usuário na Imagem

```Dockerfile
# Criar usuário
RUN useradd -m appuser

# Usar usuário
USER appuser
```

---

## ⚡ Boas Práticas de Performance

```bash
# Aproveitar cache (ordem importa no Dockerfile)
docker build -t my-image .

# Evitar cache (debug)
docker build --no-cache -t my-image .
```

### 📌 Dicas importantes

* Coloque `COPY package.json` antes do restante do código
* Use `.dockerignore`
* Prefira imagens menores (`alpine`)
* Reduza camadas (`RUN` único quando possível)

---

## 🔍 Inspeção de Imagens

```bash
# Ver detalhes da imagem
docker inspect my-image

# Histórico de camadas
docker history my-image
```
