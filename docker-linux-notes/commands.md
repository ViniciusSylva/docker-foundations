# ⚙️ Docker & Linux — Commands

---

# 🐳 Docker Commands

```bash
docker run -it ubuntu        # run Ubuntu interactively
docker build -t my-image .   # build image
docker images                # list images
docker run my-image          # run container
docker ps -a                 # list containers
```

---

# 🐧 Linux Commands

## 📂 Navigation

```bash
pwd
cd /etc
cd ..
cd ~
```

---

## 📁 Directory Management

```bash
mkdir folder
mv old new
rm -r folder
```

---

## 📄 File Management

```bash
touch file.txt
rm file.txt
rm hi*
```

---

## 📖 Viewing Files

```bash
cat file.txt
more file.txt
```

---

## ✍️ Writing & Redirection

```bash
echo hello > file.txt
cat source.txt > target.txt
```

---

## 🔍 Search

```bash
grep hello file.txt
grep -i -r hello .

find
find /etc/
find -type f
find -type d
find -name "file.txt"
```

---

## ⚙️ Command Execution

```bash
cmd1 ; cmd2
cmd1 && cmd2
```

---

## 🧠 Processes

```bash
ps
sleep 5
sleep 5 &
kill 502
```

---

## 👤 Users & Groups

```bash
whoami
useradd -m vinicius
usermod -G docker vinicius
userdel vinicius

cat /etc/group
groups vinicius
```

---

## 🔐 Permissions

```bash
chmod -u+x docker.txt
```

---

## 🔄 WSL

```bash
wsl --shutdown
```

---

## 📦 APT

```bash
apt update
apt list
apt install nano
apt remove nano
```

---

## 🧩 System

```bash
whoami
echo hi
echo $0
history
ls
```
