from dwave.system import EmbeddingComposite, DWaveSampler
import hashlib
from itertools import product
import numpy as np

# Function to check if a given password matches the target hash
def check_password(password, target_hash):
    hashed_password = hashlib.md5(password.encode()).hexdigest()  # Adjust for PKZIP hash
    return hashed_password == target_hash

# Generate QUBO for brute-forcing password (simple approach)
def generate_qubo(charset, password_length):
    num_bits = len(charset) * password_length
    qubo = np.zeros((num_bits, num_bits))

    # Example: Favor specific bit combinations (requires tuning)
    for i in range(num_bits):
        qubo[i, i] = -1  # Adjust to reflect the specific encoding of the password search

    return qubo

# Quantum brute force
def quantum_brute_force(target_hash, charset, password_length):
    sampler = EmbeddingComposite(DWaveSampler())

    qubo = generate_qubo(charset, password_length)
    response = sampler.sample_qubo(qubo, num_reads=100)

    for sample in response.samples():
        # Decode QUBO solution into a candidate password
        password = ""
        for i in range(password_length):
            # Map binary variables back to charset index
            index = np.argmax([sample[j] for j in range(i * len(charset), (i + 1) * len(charset))])
            password += charset[index]

        # Check password locally
        if check_password(password, target_hash):
            return password
    return None

# Dynamic search for unknown length
def search_password(target_hash, charset, max_length):
    for length in range(8, max_length + 1):  # Start from 8
        print(f"Trying password length {length}...")
        password = quantum_brute_force(target_hash, charset, length)
        if password:
            return password
    return None

# Main program
if __name__ == "__main__":
    CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    MAX_PASSWORD_LENGTH = 12  # Adjust based on expectations
    TARGET_HASH = "your_hash_here"  # Replace with your hash

    print("Starting quantum-assisted password recovery...")
    result = search_password(TARGET_HASH, CHARSET, MAX_PASSWORD_LENGTH)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found. Consider increasing max length or refining charset.")
