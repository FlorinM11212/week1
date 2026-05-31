# Lean Thinking: Eliminating "Muda" through the Waste Audit and Refactoring

**Module:** SWE6301 Agile Programming — Week 5: Lean Dev & Waste
**Project:** Food Delivery App (Sprint 1)
**Branch:** `lean-audit`

We act as the Lean consultants hired to reduce waste in the Food Delivery
project. Scrum told us *how to organise the work*; Lean tells us *how to avoid
wasting effort*. This audit applies Lean principles to identify and eliminate
**Muda (waste)**: Needless Complexity (Gold-plating), Needless Repetition, and
Opacity, then leaves the code cleaner than we found it (Boy Scout Rule).

---

## Part 1 — Lean's Core Principle

Lean originates from the **Toyota Production System**. The central idea is:

> **Maximize Value — Minimize Waste.**

In Agile this is *Simplicity*, "the art of maximizing the amount of work not
done". The first Lean question for any piece of code is:

> **Does this create value NOW?** If not, it is waste (Muda).

### Sprint 1 scope (the only value we owe the customer right now)

Allow customers to:

- Log in
- Browse restaurants
- Add food to the cart

Features such as an animated logo, dark mode, AI recommendations,
cryptocurrency payment, and voice ordering do **not** help us reach the Sprint 1
goal, so anything in the code that exists only to support them is waste.

---

## Part 2 — Gold Plating (Needless Complexity)

Agile teams do not build "the grand system in the sky". Waste appears when we add
elements that anticipate requirements that have not arrived yet. During the audit
each such section was marked with `# MUDA: Needless Complexity` before removal.

**BEFORE** (`cart.py` / `data_service.py`)

```python
class Cart:
    def __init__(self):
        self.items = []
        self.ai_recommendation_engine = []   # MUDA: Needless Complexity
        self.future_crypto_payments = []     # MUDA: Needless Complexity
        self.future_voice_ordering = []      # MUDA: Needless Complexity
```

`DataService` also carried a broad `except Exception` no story required and an
overly generic `fetch(resource, *args, **kwargs)` interface that nothing called.

**AFTER**

```python
class Cart:
    def __init__(self):
        self.items = []
```

Only the data the current user story needs survives.

---

## Part 3 — Needless Repetition (Once and Only Once)

Repetition is a primary "odour of rotting software". Every test re-created the
same objects. The fix is an abstraction that unifies the shared behaviour — a
`setUp()` method in `unittest`.

**BEFORE** (`test_cart.py`)

```python
def test_remove_item(self):
    cart = Cart()
    cart.add_item({"name": "Pizza", "price": 10})
    cart.remove_item({"name": "Pizza", "price": 10})
    self.assertEqual(len(cart.items), 0)
```

**AFTER**

```python
def setUp(self):
    self.cart = Cart()
    self.cart.add_item({"name": "Pizza", "price": 10})

def test_remove_item(self):
    self.cart.remove_item({"name": "Pizza", "price": 10})
    self.assertEqual(len(self.cart.items), 0)
```

The same `setUp()` consolidation was applied to `test_data_service.py`, where the
mock API client and the service under test are now built once. **Verification:**
the suite stays Green while the total lines of the test files have decreased.

---

## Part 4 — Opacity & the Boy Scout Rule

The customer requested a simple **Log Counter** feature. But the total-price
function was opaque — it did not express its intent:

**BEFORE** (`cart.py`)

```python
def p(self, x):
    t = 0
    for i in x:
        t += i["price"]
    return t
```

Following the Boy Scout Rule ("clean the kitchen first"), the function was made
expressive *before* the new feature was added:

**AFTER**

```python
def calculate_total(self):
    total_price = 0
    for item in self.items:
        total_price += item["price"]
    return total_price
```

Only once the code was clean did we add the Log Counter (`operation_log_count`
incremented on every `add_item` / `remove_item`, read via `operation_count()`).
This aligns with Agile Principle 9: *"Continuous attention to technical
excellence and good design enhances agility."*

---

## Part 5 — Reflection / Review

**1. How does maximizing "the amount of work not done" help the team maintain a
constant, Sustainable Pace indefinitely?**

Every line of code is a line that must be read, tested, debugged, and maintained
for the life of the project. By not writing code that delivers no current value,
the team keeps the system small enough to reason about. There is less to break,
less to retest after each change, and no speculative features draining effort.
The team is never "borrowing tomorrow's energy" to keep an over-engineered code
base alive, so the effort required next sprint stays roughly the same as this
one — which is exactly what a sustainable, indefinite pace means.

**2. Why is "Needless Complexity" a risk even if the code currently passes all
unit tests?**

Passing tests only prove the code does what it does today; they say nothing about
the cost it imposes tomorrow. Unused abstractions, speculative fields, and generic
interfaces still have to be understood by every developer who reads the file, still
widen the surface where bugs can hide, and still slow down genuine changes because
real logic is buried among "just in case" scaffolding. Worse, that speculative
design often guesses the future wrong, so it must be torn out anyway. Green tests
mask this carrying cost rather than removing it.

**3. Robert Martin suggests refactoring "every hour or every half hour". What are
the dangers of waiting until the end of the project to clean up?**

Waste compounds. Duplication and opaque code make the *next* change harder, which
encourages more shortcuts, which is how software "rots". By the end of the project
the mess is large, deeply entangled, and touches code no one remembers writing, so
cleaning it becomes a high-risk rewrite under deadline pressure — usually it is
simply never done. Continuous small refactors keep each clean-up tiny, safe, and
covered by the tests that are already Green, instead of saving up one dangerous
clean-up that the schedule will never allow.

---

## How to run the tests

```bash
cd week5
python -m unittest discover -v
```

All 7 tests are Green at every stage of the audit.

## Audit progression (commit history)

```
SETUP    -> initialize Lean waste audit workspace and verify baseline tests
AUDIT    -> identify needless complexity and gold-plating in service logic
REFACTOR -> apply "Once and Only Once" to eliminate repetitive test setup
BOY SCOUT-> refactor opaque logic for expressiveness before adding Log Counter
REFLECT  -> analysis of Lean waste identification and design smells
```
