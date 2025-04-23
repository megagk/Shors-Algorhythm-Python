from qiskit_ibm_provider import IBMProvider
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.primitives import Sampler
from qiskit import Aer
from math import gcd
import numpy as np
import random

# Simulating the  classical part of Shor's Algorithm
N = 15
a = 7

if gcd(a, N) != 1:
    print("Not coprime — trivial factors found:", gcd(a, N), N // gcd(a, N))
else:
    print(f"Attempting to factor N={N} using a={a}...")

    # In Shor's algorithm you'd typically use QPE (Quantum Phase Estimation) for period finding.
    # Here i'm simulating the period finding step. Potentially add this in a future commit
    r = 4  # Example measurement of a period of 4

    if r % 2 != 0:
        print("Period is odd, retrying...")
    else:
        plus = pow(a, r // 2) + 1
        minus = pow(a, r // 2) - 1
        factor1 = gcd(plus, N)
        factor2 = gcd(minus, N)

        print("Factors found:", factor1, "and", factor2)