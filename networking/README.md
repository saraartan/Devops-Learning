# 🌐 Networking Project (AWS EC2 + NGINX + Domain)

## 🚀 Overview
This project demonstrates how to deploy a web server using AWS EC2, install and configure NGINX, and connect a custom domain using DNS.

---

## ☁️ What I Built

- Launched an EC2 instance on AWS
- Configured security groups (SSH 22 and HTTP 80)
- Installed and started NGINX web server
- Verified server using public IP
- Connected a domain using Cloudflare DNS
- Hosted a live website successfully

---

## ⚙️ Commands Used

```bash
sudo apt update -y
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
