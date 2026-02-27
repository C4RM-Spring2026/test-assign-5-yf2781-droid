import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    y_period = y / ppy
    n = m * ppy
    coupon = face * couponRate / ppy
    t = np.arange(1, n + 1)
    discount_factors = 1 / (1 + y_period) ** t
    pv_coupons = np.sum(coupon * discount_factors)
    pv_face = face / (1 + y_period) ** n
    return pv_coupons + pv_face
