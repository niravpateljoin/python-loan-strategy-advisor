import numpy as np


def calculate_emi(principal, rate, months):
    r = rate / 12  # Monthly interest rate
    emi = principal * r * (1 + r) ** months / ((1 + r) ** months - 1)  # EMI formula
    return emi


def simulate_loan(principal, rate, emi, extra_per_month=0, lump_sum_schedule={}, grow_emi=False, grow_rate=0.01):
    balance = principal
    month = 0
    interest_paid = 0
    current_emi = emi

    while balance > 0:
        month += 1
        interest = balance * (rate / 12)
        payment = current_emi + extra_per_month
        principal_payment = payment - interest

        if principal_payment > balance:
            principal_payment = balance
            payment = balance + interest

        balance -= principal_payment
        interest_paid += interest

        # Grow EMI every 12 months
        if grow_emi and month % 12 == 0 and month > 0:
            current_emi *= (1 + grow_rate)

        # Apply lump sum if available
        if month in lump_sum_schedule:
            lump_sum = lump_sum_schedule[month]
            if lump_sum > balance:
                lump_sum = balance
            balance -= lump_sum

    return {
        "months": month,
        "years": round(month / 12, 2),
        "interest_paid": round(interest_paid)
    }


def format_currency(value):
    return f"₹{value:,.0f}"


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("⚠️ Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("⚠️ Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")


def main():
    print("📈 Welcome to the Loan Strategy Advisor 📈")
    print("Let's figure out smart ways to finish your loan faster!\n")

    # User Input
    principal = get_float_input("Enter loan amount (e.g., 2500000): ")
    rate = get_float_input("Enter annual interest rate (e.g., 9 for 9%): ") / 100
    tenure_years = get_int_input("Enter loan tenure in years (e.g., 25): ")

    months = tenure_years * 12
    emi = calculate_emi(principal, rate, months)  # Correct EMI calculation
    print(f"\n💰 Standard EMI: {format_currency(round(emi))}/month")

    # Strategy 1 - Regular
    base = simulate_loan(principal, rate, emi)

    # Strategy 2 - +₹2000 per month
    strat1 = simulate_loan(principal, rate, emi, extra_per_month=2000)

    # Strategy 3 - One extra EMI per year
    extra_emi_schedule = {i * 12: emi for i in range(1, tenure_years)}
    strat2 = simulate_loan(principal, rate, emi, lump_sum_schedule=extra_emi_schedule)

    # Strategy 4 - ₹50,000 lump sum every year
    lump_sum_schedule = {i * 12: 50000 for i in range(1, tenure_years)}
    strat3 = simulate_loan(principal, rate, emi, lump_sum_schedule=lump_sum_schedule)

    # Strategy 5 - 1% Growing EMI every year
    strat4 = simulate_loan(principal, rate, emi, grow_emi=True)

    strat5 = simulate_loan(principal, rate, emi, lump_sum_schedule=extra_emi_schedule, grow_emi=True)

    # Output
    print("\n📊 Strategy Comparison:\n")
    print(f"1️⃣ Regular:              {base['years']} years | Interest: {format_currency(base['interest_paid'])}")
    print(f"2️⃣ +₹2000/month:         {strat1['years']} years | Interest: {format_currency(strat1['interest_paid'])}")
    print(f"3️⃣ +1 EMI/year:          {strat2['years']} years | Interest: {format_currency(strat2['interest_paid'])}")
    print(f"4️⃣ ₹50K/year:            {strat3['years']} years | Interest: {format_currency(strat3['interest_paid'])}")
    print(f"5️⃣ +1% EMI yearly:       {strat4['years']} years | Interest: {format_currency(strat4['interest_paid'])}")
    print(
        f"6️⃣​ +1% EMI yearly +1 EMI/year:       {strat5['years']} years | Interest: {format_currency(strat4['interest_paid'])}")

    # Advice
    print("\n💡 Advice:")
    if strat1['years'] < base['years']:
        print(
            f"👉 If you can afford +₹2000/month, you’ll save {format_currency(base['interest_paid'] - strat1['interest_paid'])} in interest and close in {round(base['years'] - strat1['years'], 2)} fewer years.")
    if strat2['years'] < base['years']:
        print(
            f"👉 Paying 1 extra EMI every year helps you save {format_currency(base['interest_paid'] - strat2['interest_paid'])} and close the loan earlier by {round(base['years'] - strat2['years'], 2)} years.")
    if strat3['years'] < base['years']:
        print(
            f"👉 Yearly ₹50K payments save you {format_currency(base['interest_paid'] - strat3['interest_paid'])} and shorten tenure by {round(base['years'] - strat3['years'], )} years.")
    if strat4['years'] < base['years']:
        print(
            f"👉 Growing your EMI by 1% every year helps you close your loan in {round(base['years'] - strat4['years'], 2)} fewer years and saves {format_currency(base['interest_paid'] - strat4['interest_paid'])} in interest.")
    if (strat5['years'] < base['years']):
        print(
            f"👉 Growing your EMI by 1% every year and paying one extra EMI end of each year helps you close your loan in {round(base['years'] - strat5['years'], 2)} fewer years and saves {format_currency(base['interest_paid'] - strat5['interest_paid'])} in interest.")
    print("✅ Pick a strategy that fits your income growth and lifestyle!")


if __name__ == "__main__":
    main()
