# AI CFO Agent

> An agentic AI finance platform for SME financial analysis, forecasting, anomaly detection, and evidence-backed recommendations.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)](https://fastapi.tiangolo.com/)
[![Status](https://img.shields.io/badge/status-MVP-orange)](https://github.com/tpandit03/ai-cfo-agent)

## Why this project

Finance teams often have data available but still spend significant time turning raw numbers into answers.

AI CFO Agent explores a governed workflow for turning financial data into:

**Data → Analysis → Evidence → Recommendation**

The goal is not just to generate financial commentary, but to make recommendations traceable to the underlying calculations and signals.

## Current MVP

- Financial KPI analysis
- Burn-rate and runway calculation
- Expense anomaly detection
- 3-month cash-flow projection
- CFO-style recommendations
- Evidence fields for explainability
- FastAPI REST API
- Swagger / OpenAPI documentation
- Automated tests

## Architecture

```text
Financial Data
     │
     ▼
┌──────────────────────┐
│ Financial Analysis   │
│ KPIs • Burn • Runway │
│ Forecast • Anomalies │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Evidence Layer       │
│ Calculations • Data  │
│ Signals • Context    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Recommendation Layer │
│ CFO-style insights   │
└──────────┬───────────┘
           │
           ▼
      API / Consumer
```

## Run locally

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

**Windows**

```powershell
.venv\\Scripts\\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

### 5. Open API documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

## Example workflow

A typical request follows this path:

1. Provide financial inputs.
2. Calculate core financial metrics.
3. Detect unusual expense or cash-flow patterns.
4. Generate a forward-looking projection.
5. Produce recommendations.
6. Return evidence that explains how the recommendation was derived.

## Roadmap

### Phase 1 — Data & product foundation
- CSV / Excel ingestion
- Input validation
- PostgreSQL persistence
- Financial data models

### Phase 2 — AI reasoning
- LLM-assisted CFO reasoning
- Retrieval of financial context
- Recommendation explanations
- Structured agent outputs

### Phase 3 — Governance
- Audit trails
- Decision/evidence lineage
- Evaluation datasets
- Financial-agent evaluation framework
- Guardrails for high-impact recommendations

### Phase 4 — Platform
- Authentication and authorization
- Docker deployment
- CI/CD
- Monitoring and observability
- Dashboard / web interface

## Design principles

- **Evidence before explanation** — recommendations should trace back to data and calculations.
- **Deterministic calculations** — financial math should remain testable and reproducible.
- **Structured outputs** — downstream systems should consume predictable schemas.
- **Governance by design** — AI reasoning should operate inside explicit controls.
- **Test before trust** — financial-agent behavior should be evaluated continuously.

## Disclaimer

This is a software prototype for financial analysis. It is not financial, investment, lending, tax, or accounting advice.
