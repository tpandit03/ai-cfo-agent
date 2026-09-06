# AI CFO Agent

Agentic AI CFO platform for SME financial analysis, forecasting, anomaly detection, and evidence-backed recommendations.

## MVP

- Financial KPI analysis
- Burn rate and runway calculation
- Expense anomaly detection
- 3-month cash-flow projection
- CFO-style recommendations
- Evidence fields for explainability
- FastAPI REST API with Swagger/OpenAPI
- Automated tests

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for API documentation.

## Disclaimer

This is a software prototype for financial analysis. It is not financial, investment, lending, tax, or accounting advice.
