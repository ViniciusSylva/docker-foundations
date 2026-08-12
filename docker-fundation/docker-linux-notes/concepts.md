# 📘 Docker & Linux — Concepts

---

# 🐳 Docker

## 📌 What is Docker?

Docker is a platform used to build, run, and deploy applications in a consistent way.

It packages:

* Application code
* Dependencies
* System configurations
* Software versions

➡️ Ensures the application runs the same in any environment.

---

## ⚖️ Container vs Virtual Machine

| Feature      | Virtual Machine 🖥️ | Container 📦 |
| ------------ | ------------------- | ------------ |
| OS           | Full OS per VM      | Shared OS    |
| Performance  | Heavy               | Lightweight  |
| Startup Time | Slow                | Fast         |
| Resource Use | High                | Low          |

---

## 🧱 Core Concepts

* **Dockerfile** → Instructions to build an image
* **Image** → Environment snapshot
* **Container** → Running instance

---

## 🖼️ Image

* Lightweight OS (cut-down)
* Contains everything needed to run the application:

  * Files
  * Libraries
  * Dependencies
  * Environment variables

---

## 📦 Container

* Isolated environment
* Runs an image
* Works like a lightweight VM
* Technically a running process

---

## 🧾 Dockerfile

Main instructions:

* **FROM** → Base image
* **WORKDIR** → Working directory
* **COPY / ADD** → Add files
* **RUN** → Execute commands
* **ENV** → Environment variables
* **EXPOSE** → Application port
* **USER** → Execution user
* **ENTRYPOINT / CMD** → Startup command

---

# 🐧 Linux

## 📁 File System

Everything starts from:

```
/
```

### Important directories

| Directory | Description    |
| --------- | -------------- |
| /         | Root           |
| /etc      | Configurations |
| /home     | User files     |
| /var      | Logs           |
| /bin      | Commands       |
| /usr      | Programs       |

---

## 👤 User Management

* Users represent people or processes in the system
* Each user can belong to groups
* Groups control permissions

---

## 🔐 Permissions

### File types

* `d` → directory
* `-` → file

### Structure

```
rwx r-x r--
│   │   └── others
│   └────── group
└────────── user
```

* `r` → read
* `w` → write
* `x` → execute

---

## 🧠 Processes

* A process is a running program
* Each process has an ID (PID)
* Can run in foreground or background

---

## 🔄 WSL

Windows Subsystem for Linux allows running Linux inside Windows.

Useful for:

* Development
* Docker
* Linux commands on Windows

---

## 📦 Package Manager (APT)

Used to install and manage software on Debian-based systems.

---

## 💡 Key Idea

Linux is:

* File-based
* Permission-based
* Command-driven
