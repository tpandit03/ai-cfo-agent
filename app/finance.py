from statistics import mean
from typing import Any


def safe_mean(values: list[float]) -> float:
    return mean(values) if values else 0.0


def analyze_finances(
    revenue: list[float],
    expenses: list[float],
    cash: float,
    monthly_expenses: list[float],
    transactions: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    total_revenue = sum(revenue)
    total_expenses = sum(expenses)
    net_cash_flow = total_revenue - total_expenses
    avg_monthly_expense = safe_mean(monthly_expenses)
    runway = cash / avg_monthly_expense if avg_monthly_expense > 0 else None

    anomalies = []
    if transactions:
        amounts = [float(t["amount"]) for t in transactions]
        baseline = safe_mean(amounts)
        threshold = baseline * 2.5 if baseline else float("inf")
        for t in transactions:
            amount = float(t["amount"])
            if amount > threshold:
                anomalies.append({
                    "description": t["description"],
                    "amount": amount,
                    "category": t["category"],
                    "reason": "Transaction is materially above the observed transaction baseline.",
                })

    growth = None
    if len(revenue) >= 2 and revenue[-2] != 0:
        growth = (revenue[-1] - revenue[-2]) / revenue[-2]

    recommendations: list[str] = []
    if net_cash_flow < 0:
        recommendations.append("Reduce discretionary spending and review the largest expense categories.")
    if runway is not None and runway < 6:
        recommendations.append("Runway is below six months; prioritize liquidity preservation and near-term cash planning.")
    if growth is not None and growth < 0:
        recommendations.append("Revenue declined versus the prior period; investigate churn, pipeline, and pricing drivers.")
    if anomalies:
        recommendations.append("Review flagged transactions for unusual or potentially erroneous spending.")
    if not recommendations:
        recommendations.append("Financial position looks stable based on the supplied metrics; continue monitoring cash flow and margins.")

    forecast = []
    current_cash = cash
    for i in range(1, 4):
        forecasted_net = safe_mean(revenue) - safe_mean(expenses)
        current_cash += forecasted_net
        forecast.append({
            "month": i,
            "forecast_net_cash_flow": round(forecasted_net, 2),
            "projected_cash": round(current_cash, 2),
        })

    return {
        "summary": {
            "total_revenue": round(total_revenue, 2),
            "total_expenses": round(total_expenses, 2),
            "net_cash_flow": round(net_cash_flow, 2),
            "average_monthly_expense": round(avg_monthly_expense, 2),
            "burn_rate": round(avg_monthly_expense, 2),
            "runway_months": round(runway, 2) if runway is not None else None,
            "revenue_growth": round(growth, 4) if growth is not None else None,
        },
        "anomalies": anomalies,
        "cash_forecast": forecast,
        "recommendations": recommendations,
        "evidence": {
            "revenue_periods": len(revenue),
            "expense_periods": len(expenses),
            "transaction_count": len(transactions or []),
        },
    }
