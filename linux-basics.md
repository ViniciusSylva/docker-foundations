# 🐳 Docker & 🐧 Linux — Study Notes

> 📚 Summary of my studies on Docker and Linux fundamentals.
> This document serves as a quick reference and consolidation of what I learned.

---

## 🐳 Docker Fundamentals

### 📌 What is Docker?

Docker is a platform used to **build, run, and deploy applications** in a consistent way.

Instead of deploying only the application code, Docker allows you to package:

* Application files
* Dependencies
* System configurations
* Software versions

➡️ This ensures the application runs the same in any environment.

---

### ⚖️ Container vs Virtual Machine

| Feature        | Virtual Machine 🖥️ | Container 📦 |
| -------------- | ------------------- | ------------ |
| OS             | Full OS per VM      | Shared OS    |
| Performance    | Heavy               | Lightweight  |
| Startup Time   | Slow                | Fast         |
| Resource Usage | High                | Low          |

---

### 🧱 Core Concepts

* **Dockerfile** → Instructions to build an image
* **Image** → Environment snapshot
* **Container** → Running instance of an image

```bash
Dockerfile → Image → Container
```

---

### 📦 Docker Hub

* Repository for Docker images
* Similar to GitHub
* Used to store and share images

---

### 🚀 Main Commands

```bash
# Run Ubuntu (interactive)
docker run -it ubuntu

# Build image
docker build -t my-image .

# List images
docker images

# Run container
docker run my-image

# List containers
docker ps -a
```

---

## 🐧 Linux Fundamentals

### 📁 File System Structure

Everything starts from the root:

```bash
/
```

#### Important directories

| Directory | Description            |
| --------- | ---------------------- |
| `/`       | Root                   |
| `/etc`    | Configuration files    |
| `/home`   | User files             |
| `/var`    | Logs and variable data |
| `/bin`    | Essential commands     |
| `/usr`    | Programs and libraries |

---

### 📂 Navigation

```bash
pwd        # current directory
cd /etc    # enter directory
cd ..      # go back
cd ~       # home directory
```

---

### 📁 Directory Management

```bash
mkdir folder        # create directory
mv old new          # rename/move
rm -r folder        # remove directory
```

---

### 📄 File Management

```bash
touch file.txt      # create file
rm file.txt         # remove file
rm hi*              # remove files starting with "hi"
```

---

### 📖 Viewing Files

```bash
cat file.txt        # full content
more file.txt       # paginated view
```

---

### ✍️ Writing & Redirection

```bash
echo hello > file.txt
cat source.txt > target.txt
```

---

### 🔍 Search with grep

```bash
grep hello file.txt
grep -i -r hello .
```

* `-i` → ignore case
* `-r` → recursive search

---

### 🔎 Search with find

```bash
find
find /etc/
find -type f
find -type d
find -name "file.txt"
find -name "an*"
```

---

### ⚙️ Command Execution

```bash
cmd1 ; cmd2 ; cmd3       # runs all commands
cmd1 && cmd2 && cmd3    # runs only if previous succeeds
```

---

### 🧠 Processes

```bash
ps            # list processes
sleep 5       # pause execution
sleep 5 &     # run in background
kill 502      # terminate process
```

---

### 🔄 WSL

```bash
wsl --shutdown
```

➡️ Useful to restart and fix issues in the Linux environment

---

## 🧩 System Commands

```bash
whoami     # current user
echo hi    # output text
echo $0    # current shell
history    # command history
ls         # list files
```

---

## 📦 Package Manager (APT)

```bash
apt update          # update package list
apt list            # list installed packages
apt install nano    # install editor
nano                # open editor
apt remove nano     # remove editor
```

---

## 💡 Tips

* Always run `apt update` before installing packages
* Containers are **temporary by default**
* Use `-it` for interactive containers
* Use `docker ps -a` to view all containers
* Use `pwd` and `ls` frequently

---

## ⚠️ Common Mistake

```bash
❌ apr install nano
✅ apt install nano
```

---

## 🚀 Conclusion

This study helped me strengthen my knowledge in:

* Docker and containerization
* Linux file system and commands
* Terminal usage and environment management

📈 Next step: apply these concepts in real projects.

---
