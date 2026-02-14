# LootDrop

A personal job application tracking dashboard that helps you organize, monitor, and analyze your job search — with automated email parsing, status tracking, and metrics visualization. Built using **FastAPI** (Python) for the backend and **React** for the frontend.

## 🧠 Project Overview

This application was created to centralize and automate tracking of job applications on your local network. It parses recruiter emails, tracks application statuses, and provides visual metrics so you can stay data-driven in your search. It also sets a solid foundation for future enhancements such as AI-based resume scoring and smart suggestions.

---

## 📌 Features

- 📬 Email parsing from Gmail or Outlook to detect replies/interviews  
- 📊 Dashboard for tracking applications by status, time to reply, and trends  
- 🗂️ Structured data storage (PostgreSQL) with clean API design  
- 🧪 Extensible architecture for future automations and AI scoring

---

## 🚀 Tech Stack

This project uses the following technologies:

**Frontend**
- React (UI components, pages, state management)

**Backend**
- FastAPI (REST API, business logic)
- PostgreSQL (relational database)
- Docker + Docker Compose (development environment)

**Optional Enhancements**
- AI scoring via LLM APIs  
- Email provider integration (Gmail / Microsoft Graph)

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have the following installed:

- Docker & Docker Compose  
- Python 3.10+  
- Node.js 18+ (for frontend development)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lootdrop.git
   cd job-application-tracker