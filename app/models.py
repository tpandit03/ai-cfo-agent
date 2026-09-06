from pydantic import BaseModel, Field
from typing import List, Optional


class Transaction(BaseModel):
    description: str
    amount: float = Field(gt=0)
    category: str
    month: Optional[str] = None


class AnalyzeRequest(BaseModel):
    revenue: List[float]
    expenses: List[float]
    cash: float = Field(ge=0)
    monthly_expenses: List[float]
    transactions: List[Transaction] = []
