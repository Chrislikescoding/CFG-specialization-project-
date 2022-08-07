def tax_rate_multiplier_of(n):
    def multiplier(x):
        return x * n/100
    return multiplier
# Multiplier of 45p for up to 10,000 miles
times45 = tax_rate_multiplier_of(45)
# Multiplier of 25 for over 10,000 miles
times25 = tax_rate_multiplier_of(25)
# Output: 45
#print(times45(100))
# Output: 25
#print(times25(100))
total_miles_claimed =9600
claim_amount = 200
miles_this_claim =500
# we know that the first 10000 miles will be charged at 45p
if total_miles_claimed > 10000:
    print(times25(miles_this_claim))
elif total_miles_claimed + miles_this_claim>10000:
    over_tenk_amount=times25(total_miles_claimed + miles_this_claim -(10000))
    under_tenk_amount = times45(10000 - total_miles_claimed)
    print(over_tenk_amount)
    print(under_tenk_amount)
elif total_miles_claimed + miles_this_claim<=10000:
    print(times45( miles_this_claim))
