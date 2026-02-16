# AI Sales Agent 🤖

A production-ready, multi-platform AI sales assistant that automates customer interactions, order processing, and inventory management across WhatsApp, Instagram, and Facebook Messenger.

## 🌟 Features

- **Multi-Platform Support**: Unified interface for WhatsApp, Instagram, Facebook
- **AI-Powered Conversations**: Natural language understanding for order intent, extraction, and response generation
- **Smart Order Flow**: Guided conversation (Product → Customer Type → Quantity → Confirmation)
- **Dynamic Pricing**: Wholesaler, retailer, and individual pricing tiers
- **Inventory Management**: Real-time stock checking and low-stock alerts
- **Session Management**: Redis-based conversation state across platforms
- **Production-Ready**: Caching, monitoring, rate limiting, and security built-in

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Redis
- PostgreSQL (or SQLite for testing)

### Install
```bash
git clone https://github.com/9uxsnx-sys/ai-sales-agent.git
cd ai-sales-agent
pip install -r requirements.txt
```

### Configure
Create `.env`:
```bash
DATABASE_URL=sqlite+aiosqlite:///./test.db
REDIS_URL=redis://localhost:6379/0
GEMINI_API_KEY=your-api-key-here
ENVIRONMENT=development
```

### Run
```bash
uvicorn app.main:app --reload
```

## 🔧 Using Real LLM (Not Mock)

1. Remove from test files: `from tests import test_config`
2. Set real API key: `GEMINI_API_KEY=your-key`
3. Run tests: `pytest tests/`

## 📁 Project Structure
- `app/` - FastAPI, caching, security, monitoring
- `agents/` - Intent, Extraction, Response agents
- `logic/` - Business logic
- `models/` - Database models
- `tests/` - Test suite

MIT License
