# Bad PR Review:
So far, the initial structure is good, but there's room for improvement.

## Pull Request Summary
"Implemented checkout logic in cart. Also added slot checking and order placing."

Need more imporovement
Microserice SAGA or 2 pache commit and not service to service communication found.
No test case or unit test, ingetration test not found
---

## Code (Bad Sample)
No time found for code rivew will continue

## Review Feedback

### Naming
- Function `checkout()` is too generic. Should be `process_checkout()` or `perform_checkout()`.

### Logic Separation
- All business logic is packed in one endpoint function.
- Should separate:
  - Slot checking
  - Price calculation
  - Order placing
  - Cart cleanup
  into individual helper functions or services.

### REST Correctness
  - This breaks microservice abstraction and makes testing difficult.
  - Use service layer or proxy method.

### Error Handling
- No timeout or exception handling for HTTP requests.
- No check for valid cart before proceeding.

### Auth
- Missing JWT protection (no role check).

---
