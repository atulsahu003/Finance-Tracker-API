from datetime import datetime
from calendar import monthrange 

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from database import get_db
from models import Transaction, User
from schemas import TransactionCreate
from security import get_current_user

router = APIRouter(prefix="/transactions", tags=["Expenses"])

@router.post("/add")
def create_transaction(
    transaction:TransactionCreate,
    current_user: User = Depends(get_current_user),
    db:Session = Depends(get_db)
):
    new_transaction = Transaction(
        amount = transaction.amount,
        type = transaction.type,
        category = transaction.category,
        description = transaction.description,
        user_id = current_user.id
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return {
        "message": "Transaction added successfully",
        "transaction_id": new_transaction.id
    }

@router.get("/all")
def get_all_transaction(
    current_user:User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transactions = db.execute(select(Transaction).where(Transaction.user_id == current_user.id)).scalars().all()

    return transactions

@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: int, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    transaction = db.execute(select(Transaction).where(Transaction.id == transaction_id)).scalar_one_or_none()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    db.delete(transaction)
    db.commit()

    return {
        "message": "Transaction deleted successfully"
    }

@router.get("/analytics/monthly")
def monthly_summary(
    year: int,
    month: int,
    current_user: User = Depends(get_current_user),
    db:Session = Depends(get_db)
):

    start_date = datetime(year, month, 1)
    last_day = monthrange(year, month)[1]
    end_date = datetime(year, month, last_day, 23, 59, 59)

    income = db.scalar(
        select(func.sum(Transaction.amount))
        .where(
            Transaction.user_id == current_user.id,
            Transaction.type == 'income',
            Transaction.created_at >= start_date,
            Transaction.created_at <= end_date
        )
    )

    expense = db.scalar(
        select(func.sum(Transaction.amount))
        .where(Transaction.user_id == current_user.id,
               Transaction.type == "expense",
               Transaction.created_at >= start_date,
               Transaction.created_at <= end_date)     
    )

    total_income = income or 0
    total_expense = expense or 0

    balance = total_income - total_expense

    return {
        "month": f"{year}---{month}",
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }

@router.get("/analytics/categories")
def category_analytics(
    current_user: User = Depends(get_current_user),
    db:Session = Depends(get_db)
):

    results = db.execute(
        select(
            Transaction.category,
            func.sum(Transaction.amount).label("total")
        )
        .where(
            Transaction.user_id == current_user.id,
            Transaction.type == "expense"
        )
        .group_by(Transaction.category)
    ).all()

    return {
        category: float(total)
        for category, total in results
    }

@router.get("/analytics/top-category")
def top_category(
    current_user: User = Depends(get_current_user),
    db:Session = Depends(get_db)
):
    result = db.execute(
            select(
                Transaction.category,
                func.sum(Transaction.amount).label("total")
            )
            .where(
                Transaction.user_id == current_user.id,
                Transaction.type == "expense"
            )
            .group_by(Transaction.category)
            .order_by(func.sum(Transaction.amount).desc())
            .limit(1)
        ).first()

    if not result:
        return {
            "message": "No Expense found"
        }

    return {
        "Highest_expense_category": result.category,
        "amount": result.total
    }
    
