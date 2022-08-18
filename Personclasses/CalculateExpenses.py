# In the UK, mileage expense claims aer paid at 45p per mile up to 10,000 miles
# and 25p per mile over 10000 miles
# This function will selectively update amounts depending on the mileage rate that applies
class CalculateExpenses:
    def __init__(self, total_miles_claimed,  miles_this_claim):
        # initialize attributes
        self.total_miles_claimed = total_miles_claimed
        self.miles_this_claim = miles_this_claim

    def calculate(self):

        # decorator to enable the two tax rates to be processed
        def tax_rate_multiplier_of(n):
            def multiplier(x):
                return x * n / 100
            return multiplier
        times25 = tax_rate_multiplier_of(25)
        times45 = tax_rate_multiplier_of(45)

        # case 1 previous miles clained already over 10,000
        if self.total_miles_claimed > 10000:
            amount_claimed = times25(self.miles_this_claim)
        # case 2 not currently over 10,000 but will be with the amount claimed this time
        elif self.total_miles_claimed + self.miles_this_claim > 10000:
            over_tenk_amount = times25(self.total_miles_claimed + self.miles_this_claim - 10000)
            under_tenk_amount = times45(10000 - self.total_miles_claimed)
            amount_claimed = over_tenk_amount + under_tenk_amount
        # case 3 not currently over 10,000 and wont be with the amount claimed this time
        elif self.total_miles_claimed + self.miles_this_claim <= 10000:
            amount_claimed = times45(self.miles_this_claim)
        return amount_claimed
