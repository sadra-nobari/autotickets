# AI-Powered Internal Ticket Automation System

An intelligent internal operations and support ticket routing system built with **n8n** and powered by the **deepseek API**. This system automates the manual triage process by parsing unstructured ticket text, classifying it by department and priority using advanced prompt engineering, and routing the results to target channels.

## 🚀 Features
- **Automated Ingestion:** Exposes a secure REST API Webhook endpoint to receive incoming tickets.
- **LLM-Driven Triage:** Leverages Gemini LLM to extract structured JSON data (`category`, `priority`, `summary`) from raw, unstructured natural language text.
- **Dynamic Routing:** Instantly forwards high-priority IT incidents to communication channels (e.g., Slack/Discord) and logs HR/Finance tickets into spreadsheets or databases.
- **Error Resilient:** Enforces a strict JSON-only output format from the LLM for reliable downstream parsing.

## 🛠️ Tech Stack
- **Workflow Automation:** n8n (Self-hosted via Docker)
- **AI/LLM:** DeepSeek API / Google AI Studio
- **Languages & Protocols:** Python (for automated testing), Webhooks, REST API, JSON

---

## ⚙️ Setup & Installation

### 1. Run n8n locally via Docker
Launch an isolated instance of n8n on your local machine by running the following command in your terminal:
```bash
docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n


### 2. Import autoticket.json file in n8n

For using the project you need to import it on your n8n on your machine.

###3. Add API

you need to add your api key in AI Agent settings. 

now you can test it on your own :)