# AWS Application Load Balancer Project

## What I Built

In this project, I built a simple but realistic web setup using AWS.

I deployed two EC2 instances running basic web servers and placed them behind an Application Load Balancer. The load balancer handles all incoming traffic and sends requests to either server.

Each server displays a different message so I can clearly see traffic switching between them.

---

## Architecture

- 1 Application Load Balancer (ALB)
- 2 EC2 instances (Web-1 and Web-2)
- 2 Availability Zones
- 1 Target Group with health checks

Traffic flow:

Users → ALB → Web-1 / Web-2

---

## What I Learned

This project helped me understand:

- How load balancers distribute traffic across servers
- How health checks keep systems reliable
- How security groups control access between resources
- How to deploy resources across multiple availability zones
- How AWS handles scalable web architecture

---

## Challenges I Faced

At first, I had issues with:

- Security group rules blocking traffic
- Instances not registering as healthy
- Git push conflicts when uploading files

I fixed these by carefully reviewing security settings, waiting for health checks to pass, and resolving Git sync issues step by step.

---

## Testing

To confirm everything worked, I opened the ALB DNS link in my browser and refreshed the page multiple times.

I could see responses switching between:

- "Hello from Server 1"
- "Hello from Server 2"

This confirmed that load balancing was working correctly.

---

## Final Result

A working, simple, and scalable AWS architecture that demonstrates how real-world applications balance traffic and stay highly available.
