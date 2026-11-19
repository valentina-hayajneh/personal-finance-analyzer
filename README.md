# Personal Finance Analyzer

A beginner-friendly Python command-line project that calculates monthly expenses, remaining balance, spending percentages, and savings progress. It then displays a simple financial analysis and recommendations.

## Python Concepts Used

This project applies the topics covered in Parts 1–5 of the Python course:

- Getting started
- Information from the user
- Variables
- Arithmetic operations
- Conditional statements

**Built-in functions used:** `print()`, `input()`, `float()`, `exit()`.

## Financial Calculations

| Calculation | Formula |
|---|---|
| Total Expenses | Rent + Food + Transportation + Shopping + Other Expenses |
| Remaining Balance | Monthly Salary − Total Expenses |
| Expense Percentage | (Total Expenses ÷ Monthly Salary) × 100 |
| Remaining Balance Percentage | (Remaining Balance ÷ Monthly Salary) × 100 |
| Savings Goal Difference | Remaining Balance − Savings Goal |
| Category Percentage | (Category Expense ÷ Monthly Salary) × 100 |

## Financial Analysis Rules

- **Financial Status:** Surplus, Deficit, or Break-even.
- **Spending Level:** Low (below 50%), Moderate (50%–80%), or High (above 80%).
- **Savings Goal:** Exceeded, achieved exactly, or not achieved.
- **Recommendations:** Displayed according to the financial results.

The spending thresholds are fixed rules used in this educational project.

## Test Results

The program was tested with three different financial scenarios. The screenshots below show the complete terminal output, including the calculated results, analysis, and recommendations.

### Test Case 1 — Surplus and Moderate Spending

Monthly income: **1,000 JOD** · Total expenses: **640 JOD** · Remaining balance: **360 JOD**

The user has a surplus, spends 64% of monthly income, and exceeds the 80 JOD savings goal by 280 JOD.

![Test Case 1 — Surplus and Moderate Spending](First%20Case.png)

### Test Case 2 — Deficit and High Spending

Monthly income: **350 JOD** · Total expenses: **450 JOD** · Remaining balance: **-100 JOD**

Expenses exceed income by 100 JOD. Spending reaches 128.57% of income, and the savings goal shortfall is 180 JOD. The program displays three recommendations.

![Test Case 2 — Deficit and High Spending](Second%20Case.png)

### Test Case 3 — Surplus, High Spending, and Savings Goal Not Achieved

Monthly income: **600 JOD** · Total expenses: **500 JOD** · Remaining balance: **100 JOD**

The user has a surplus, but spending reaches 83.33% of income. The remaining balance is 50 JOD below the 150 JOD savings goal, so the program displays two recommendations.

![Test Case 3 — Surplus and High Spending](Third%20Case.png)

## Comparison of the Three Test Cases

All monetary values are in JOD.

| Metric | Test 1 | Test 2 | Test 3 |
|---|---:|---:|---:|
| Monthly Income | 1,000 | 350 | 600 |
| Total Expenses | 640 | 450 | 500 |
| Remaining Balance | 360 | -100 | 100 |
| Expense Percentage | 64.00% | 128.57% | 83.33% |
| Remaining Balance Percentage | 36.00% | -28.57% | 16.67% |
| Savings Goal | 80 | 80 | 150 |
| Savings Goal Difference | +280 | -180 | -50 |
| Financial Status | Surplus | Deficit | Surplus |
| Spending Level | Moderate | High | High |
| Savings Goal Result | Exceeded | Not Achieved | Not Achieved |
| Recommendations | 1 | 3 | 2 |

### Expense Breakdown

Each percentage represents the expense category as a share of monthly income.

| Expense Category | Test 1 | Test 2 | Test 3 |
|---|---:|---:|---:|
| Rent | 25.00% | 42.86% | 33.33% |
| Food | 12.00% | 28.57% | 20.00% |
| Transportation | 9.00% | 14.29% | 10.00% |
| Shopping | 10.00% | 28.57% | 13.33% |
| Other Expenses | 8.00% | 14.29% | 6.67% |

### Key Observations

- **Test 1:** The only case with moderate spending; the savings goal is exceeded.
- **Test 2:** The only case with a deficit; expenses are higher than income.
- **Test 3:** The user has a surplus, but high spending prevents the savings goal from being reached.

These cases show that having a positive balance does not always mean the savings goal has been achieved.

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in a terminal.
3. Run:

```bash
py main.py
```

## Project Structure

```text
personal-finance-analyzer/
├── main.py
├── README.md
├── LICENSE
├── First Case.png
├── Second Case.png
└── Third Case.png
```

## Limitations

- Command-line application; no web or graphical interface.
- Processes one assessment per run and does not save results.
- Validates negative numeric values, but does not currently handle non-numeric input.
- Spending thresholds are fixed project rules, not personalised financial advice.

## Disclaimer

This project is for educational purposes only. Its calculations and recommendations are not professional financial advice.

## License

Copyright (c) 2026 Valentina Hayajneh

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.
