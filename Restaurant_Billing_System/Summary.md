# Summary - Restaurant Billing System (PS 38)

**Name:** Kanchan Sahu

## How It Is Implemented
- The menu is a dictionary `MENU` with item names as keys and prices as values.
- Ordered items are stored in a list; each item is a dictionary `{"name", "qty", "amount"}`.
- Constants at the top (`DISCOUNT_LIMIT`, `DISCOUNT_RATE`, `GST_RATE`) make the rules easy to change.
- `add_item()` checks the item name, then the quantity (whole number, at least 1), and adds it to the order.
- `calculate_subtotal()`, `calculate_discount()` and `calculate_gst()` each do one calculation.
- `generate_bill()` prints the items and totals, then the order is cleared for the next customer.
- `main()` shows the menu in a loop until the user chooses Exit.

## Test Cases

| # | Case | Input | Output |
|---|------|-------|--------|
| 1 | Normal | Dosa, quantity 2 | Dosa x2 added \| Amount: 160 |
| 2 | Boundary | Tea, quantity 1, generate bill | Subtotal: 20 \| Discount: 0.00, GST (5%): 1.00 \| Grand Total: 21.00 |
| 3a | Invalid item | Pizza | Item not on the menu. Available: Dosa, Idli, Thali, Tea |
| 3b | Invalid quantity | Quantity 0 | Quantity must be at least 1. |
| 3c | Invalid quantity | Quantity abc | Invalid quantity. Enter a whole number. |
| 4 | Different valid scenario | Thali x4, Dosa x2, Tea x2, generate bill | Thali x4 = 600 \| Dosa x2 = 160 \| Tea x2 = 40, Subtotal: 800 \| Discount (10%): 80.00, GST (5%): 36.00, Grand Total: 756.00 |

## Screenshots
- Test Case 1: `screenshots/tc1.png`
- Test Case 2: `screenshots/tc2.png`
- Test Case 3: `screenshots/tc3.png`
- Test Case 4: `screenshots/tc4.png`
