# Production-Grade Microservices Platform on Kubernetes

A production-style cloud-native platform built using FastAPI, Docker, Kubernetes, Helm, and GitHub Actions.

## Tech Stack

- Python
- FastAPI
- Docker
- Kubernetes
- Helm
- GitHub Actions

## Features

- Containerized application
- Kubernetes deployment manifests
- Helm chart packaging
- CI pipeline with GitHub Actions
- ConfigMap and Secret management
- Health check endpoints

## Project Structure

backend/
kubernetes/
helm/
.github/workflows/
docs/

## API Endpoints

GET /

GET /health

GET /version

## CI/CD Flow

Developer → GitHub → GitHub Actions → Docker → Kubernetes

## Future Enhancements

- ArgoCD GitOps
- AKS Deployment
- Monitoring with Prometheus
- Grafana Dashboards