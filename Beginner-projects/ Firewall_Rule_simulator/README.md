#  Firewall Rule Simulator

A beginner-friendly Python project that simulates how a firewall checks incoming IP addresses against predefined firewall rules.

The program generates random IP addresses, checks whether they are blocked or allowed, and prints the result along with a randomly generated request ID.

---

## 📌 Features

- Generate random IPv4 addresses
- Simulate firewall rule matching
- Allow or block IP addresses based on predefined rules
- Generate a random request ID for each request
- Demonstrates the use of dictionaries for fast lookups

---

## 🛠️ Technologies

- Python 3
- Built-in `random` module


## 🚀 How It Works

1. A random IP address is generated.
2. The program checks whether the IP exists in the firewall rule list.
3. If the IP is found, the corresponding action (`block`) is returned.
4. If the IP is not found, the default action (`allow`) is returned.
5. A random request ID is generated.
6. The result is displayed.
7. The process repeats 12 times.

---

##  Concepts 

- Functions
- Parameters
- Return statements
- Dictionaries
- Dictionary `.get()` method
- Loops
- Conditional statements
- Random number generation
- f-Strings
- Python modules
- Program entry point (`if __name__ == "__main__":`)
- Creating reusable functions
- Passing arguments between functions
- Using dictionaries to store firewall rules
- Performing fast dictionary lookups with `.get()`
- Simulating simple cybersecurity concepts using Python
- Writing cleaner and more modular code
---

