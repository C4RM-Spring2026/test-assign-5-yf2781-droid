import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    y_period = y / ppy
    n = m * ppy
    t = np.arange(1, n + 1)
    coupon = face * couponRate / ppy
    cashflows = np.full(n, coupon)
    cashflows[-1] += face 
    discount = 1 / (1 + y_period) ** t
    pv = cashflows * discount
    price = np.sum(pv)
    duration_periods = np.sum(t * pv) / price
    duration_years = duration_periods / ppy 
    return duration_years
