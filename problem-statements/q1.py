def calculate_total_bill(amount: float, tip_percent: int) -> float:
    amount = float(amount)
    total = amount + (amount * (tip_percent / 100))
    return round(total, 2)
