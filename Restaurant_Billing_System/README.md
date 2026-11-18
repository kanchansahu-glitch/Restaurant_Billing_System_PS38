# Restaurant Billing System

**PS No.: 38**  
**Language:** Python 3

## Project Description
A console-based restaurant billing program. The cashier enters customer items and quantities, and the program calculates the subtotal, discount, GST, and final grand total.

## Menu
| Item | Price |
|---|---:|
| Dosa | Rs. 80 |
| Idli | Rs. 40 |
| Thali | Rs. 150 |
| Tea | Rs. 20 |

## Billing Rules
- A 10% discount is applied when the subtotal is **more than Rs. 500**.
- GST is 5% of the amount after discount.
- Quantity must be a whole number of at least 1.
- Only menu items are accepted.
- Type `done` to generate the final bill.

## Concepts Used
- Dictionaries
- Lists
- Loops
- Conditional statements
- Input validation
- Functions/calculations
- Formatted output

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in terminal or VS Code.
4. Run:

```bash
python one.py
```

## Example
Input:
- Thali x 4
- Dosa x 2
- Tea x 2

Output calculations:
- Subtotal: Rs. 800.00
- Discount (10%): Rs. 80.00
- GST (5% after discount): Rs. 36.00
- Grand Total: Rs. 756.00

## Project Files
- `one.py` – Python source code
- `README.md` – Project documentation
- `Test_cases_passed.pdf` – Test-case report
- `Project_Details_PS38.jpg` – Project allocation screenshot
