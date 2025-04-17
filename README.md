
# Loan Strategy Advisor

Welcome to the Loan Strategy Advisor! 📈 This project helps you explore various strategies to pay off your loan faster, save on interest, and understand the impact of different repayment tactics.

## 💡 Features

- Calculate your standard EMI based on loan amount, interest rate, and tenure.
- Simulate different loan repayment strategies to pay off the loan faster:
  - Extra payments per month
  - Lump sum payments
  - Growing EMI payments over time
- Compare the strategies based on the time to pay off the loan and interest saved.
- Provides useful advice on which strategies will work best for you based on your financial situation.

## 🏦 How to Use

1. **Clone the repository**:

```bash
git clone https://github.com/niravpateljoin/python-loan-strategy-advisor.git
cd python-loan-strategy-advisor
```

2. **Run the application**:

```bash
python main.py
```

3. **Enter your loan details** when prompted:
   - Loan amount
   - Annual interest rate
   - Loan tenure (in years)

4. The program will calculate and suggest the best strategies to pay off your loan faster.

## 🕹️ How to Play

- The program simulates various loan repayment strategies and shows you how long it will take to pay off your loan and how much interest you will save with each strategy.
- Strategies compared:
  1. **Regular**: Standard EMI calculation with no extra payments.
  2. **+₹2000/month**: Adds ₹2000 to the EMI every month.
  3. **+1 EMI/year**: Adds one extra EMI payment every year.
  4. **₹50K lump sum/year**: Adds ₹50,000 lump sum payments every year.
  5. **Growing EMI yearly**: Increases the EMI by 1% every year.
  6. **+1% EMI yearly + 1 EMI/year**: Combines growing EMI payments and adding one extra EMI each year.

## 📊 Sample Stats

### Example Output

```
📊 Strategy Comparison:

1️⃣ Regular:              25 years | Interest: ₹5,00,000
2️⃣ +₹2000/month:         22 years | Interest: ₹4,30,000
3️⃣ +1 EMI/year:          23 years | Interest: ₹4,50,000
4️⃣ ₹50K/year:            20 years | Interest: ₹4,00,000
5️⃣ +1% EMI yearly:       21 years | Interest: ₹4,10,000
6️⃣​ +1% EMI yearly +1 EMI/year:       19 years | Interest: ₹3,90,000

💡 Advice:
👉 If you can afford +₹2000/month, you’ll save ₹70,000 in interest and close in 3 fewer years.
👉 Paying 1 extra EMI every year helps you save ₹50,000 and close the loan earlier by 2 years.
👉 Yearly ₹50K payments save you ₹1,00,000 and shorten tenure by 5 years.
👉 Growing your EMI by 1% every year helps you close your loan in 4 fewer years and saves ₹90,000 in interest.
👉 Growing your EMI by 1% every year and paying one extra EMI at the end of each year helps you close your loan in 6 fewer years and saves ₹1,10,000 in interest.

✅ Pick a strategy that fits your income growth and lifestyle!
```

## 📈 Why This Project?

This project is designed to demonstrate various financial strategies that can help individuals make better decisions when it comes to managing their loans. By integrating simple mathematical models with Python, this project is ideal for anyone looking to understand loan repayment dynamics better, especially for:

- Students learning finance and Python
- Developers interested in building practical applications
- Financial advisors looking to show clients various repayment strategies

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.