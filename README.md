# Quantum-Assisted Password Recovery

This repository demonstrates how to use D-Wave's quantum annealer to assist in recovering a forgotten password by brute-forcing a hash. The approach leverages the capabilities of quantum computing to optimize the password search process for longer and more complex passwords.

## Features
- Dynamically searches for passwords of unknown lengths starting from 8 characters.
- Supports alphanumeric character sets.
- Combines quantum-assisted search with local hash validation for efficient password recovery.
- Configurable for various password hash types.

---

## Prerequisites
1. **D-Wave Leap Account**:
   - Sign up at [D-Wave Leap](https://cloud.dwavesys.com/leap/) to access quantum computing resources.
2. **Install Required Libraries**:
   - Install the D-Wave Ocean SDK:
     ```bash
     pip install dwave-ocean-sdk
     ```
   - Install other required Python libraries:
     ```bash
     pip install numpy
     ```

3. **Extract Target Hash**:
   - Obtain the hash of your file or password. For PKZIP 2 hashes, ensure compatibility with the script's `check_password` function.

---

## How It Works
1. **Password Search**:
   - The script starts from a minimum password length (e.g., 8) and iteratively increases the length.
   - A **QUBO (Quadratic Unconstrained Binary Optimization)** problem is generated for each length, representing the search space for possible passwords.

2. **Quantum Annealing**:
   - The QUBO is submitted to D-Wave's quantum annealer, which identifies candidate solutions.
   - The quantum system helps prioritize plausible combinations of characters.

3. **Local Validation**:
   - Each candidate password generated by the quantum system is validated against the target hash.

---

## Usage
### Modify Parameters
1. Open the script file.
2. Update the following parameters:
   - `CHARSET`: The set of characters to include in the password search.
   - `MAX_PASSWORD_LENGTH`: The maximum password length to search.
   - `TARGET_HASH`: Replace with the hash you wish to recover.

### Run the Script
```bash
python quantum_password_recovery.py
```

### Example Output
```plaintext
Starting quantum-assisted password recovery...
Trying password length 8...
Trying password length 9...
Password found: MySecureP@ssword
```

---

## Configuration
### Character Set
Modify `CHARSET` to reflect the possible characters in your password:
```python
CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
```

### Maximum Password Length
Set a reasonable upper limit for the password length:
```python
MAX_PASSWORD_LENGTH = 12
```

### Target Hash
Replace `TARGET_HASH` with the hash of your forgotten password:
```python
TARGET_HASH = "your_hash_here"
```

---

## Limitations
1. **QUBO Complexity**:
   - The problem size grows with `CHARSET × PASSWORD_LENGTH`. Large problems may exceed the capacity of current quantum systems.
2. **Hardware Constraints**:
   - The quantum system may return suboptimal solutions due to noise or limited qubit connectivity.
3. **Password Search Time**:
   - For very long passwords or large charsets, the search process may be computationally expensive.

---

## Contribution
Feel free to submit issues or pull requests to improve the script or add new features.

---

## Disclaimer
This script is intended for **educational purposes only**. Use it only to recover your own forgotten passwords or with explicit permission from the owner of the hashed data. Unauthorized usage may violate ethical and legal boundaries.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
