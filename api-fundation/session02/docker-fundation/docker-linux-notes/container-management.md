# 🐳 Docker — Container Management Commands

> 📌 Advanced commands for managing containers via terminal

---

## 🏷️ Naming Containers

```bash
# Create container with custom name
docker run --name my-container nginx

# Run in background with name
docker run -d --name web-server nginx
```

---

## 📜 Logs

```bash
# Show container logs
docker logs my-container

# Follow logs in real time
docker logs -f my-container

# Show last lines
docker logs --tail 50 my-container
```

---

## 🌐 Port Mapping

```bash
# Map host port to container port
docker run -p 8080:80 nginx

# Multiple ports
docker run -p 3000:3000 -p 9229:9229 node-app
```

---

## 💻 Execute Commands in Container

```bash
# Run command inside container
docker exec my-container ls

# Interactive terminal access
docker exec -it my-container bash
```

---

## ▶️ Container Lifecycle

```bash
# Stop container
docker stop my-container

# Start container
docker start my-container

# Restart container
docker restart my-container
```

---

## ❌ Remove Containers

```bash
# Remove stopped container
docker rm my-container

# Force remove running container
docker rm -f my-container

# Remove all stopped containers
docker container prune
```

---

## 💾 Volumes (Persistence)

```bash
# Create volume
docker volume create my-volume

# List volumes
docker volume ls

# Use volume in container
docker run -v my-volume:/app nginx
```

---

## 📂 Copy Files

```bash
# Copy from host to container
docker cp file.txt my-container:/app/

# Copy from container to host
docker cp my-container:/app/file.txt .
```

---

## ⚡ Extra Utilities

```bash
# Run in background
docker run -d nginx

# Show container details
docker inspect my-container

# Show resource usage (CPU, RAM)
docker stats

# Remove unused resources
docker system prune
```

---

## 🧠 Flags Summary

* `-d` → detached (background)
* `-it` → interactive terminal
* `--name` → container name
* `-p` → port mapping
* `-v` → volume
