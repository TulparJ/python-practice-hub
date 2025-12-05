# Tugrik → USD (simple fx rate)
rate = 0.00029  # approx

def mnt_to_usd(mnt):
    return round(mnt * rate, 2)

print(mnt_to_usd(10000), "USD")
