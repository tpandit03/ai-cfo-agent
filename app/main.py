from fastapi import FastAPI
from app.models import AnalyzeRequest
from app.finance import analyze_finances

app = FastAPI(
    title="AI CFO Agent",
    description="SME financial analysis and CFO-style insights API.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    return analyze_finances(
        revenue=request.revenue,
        expenses=request.expenses,
        cash=request.cash,
        monthly_expenses=request.monthly_expenses,
        transactions=[t.model_dump() for t in request.transactions],
    )
