# 🌐 EC2 + NGINX + Domain Project

## 🚀 Project Overview
I deployed a fully working web server using AWS EC2, installed NGINX, and connected it to a custom domain using Cloudflare DNS.

This project demonstrates cloud infrastructure, networking, and basic DevOps skills.

---

## ☁️ Infrastructure Setup

- Cloud Provider: AWS EC2
- OS: Ubuntu 22.04 LTS
- Web Server: NGINX
- Domain Provider: Cloudflare

---

## 🏗️ What I Built

- Launched EC2 instance in AWS
- Configured security groups (ports 22 and 80)
- Installed and started NGINX web server
- Verified server using public IP
- Connected domain to EC2 using DNS A records
- Successfully hosted a live website

---

## ⚙️ Commands Used

```bash
sudo apt update -y
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
