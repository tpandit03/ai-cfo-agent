from app.finance import analyze_finances


def test_financial_summary_and_runway():
    result = analyze_finances(
        revenue=[10000, 12000, 11000],
        expenses=[7000, 8000, 7500],
        cash=30000,
        monthly_expenses=[7000, 8000, 7500],
    )

    assert result["summary"]["net_cash_flow"] == 10500
    assert result["summary"]["runway_months"] > 3
    assert len(result["cash_forecast"]) == 3


def test_transaction_anomaly_detection():
    result = analyze_finances(
        revenue=[10000],
        expenses=[5000],
        cash=20000,
        monthly_expenses=[5000],
        transactions=[
            {"description": "Cloud", "amount": 100, "category": "software"},
            {"description": "Large purchase", "amount": 1000, "category": "equipment"},
        ],
    )

    assert len(result["anomalies"]) == 1
    assert result["anomalies"][0]["description"] == "Large purchase"
