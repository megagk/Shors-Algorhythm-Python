**Introduction**

Shor's Algorithm is a quantum algorithm for integer factorisation. Given a composite odd integer N (typically assumed to be not a power of a prime), it attempts to efficiently find its
nontrivial prime factors. 
Classically, factorisation takes exponential time in the number of digits of N (for large numbers), whiler
Generally utilised for crpytography to gain access to encrpyted keys.

Although, it is kinda not useful right now; it will be in future if large-scale quantum computers become practical. 
In which case it would make RSA, DSA and ECC insecure i.e., prompting the need for post-quantum crpytography.


Algorithm consists of 2 parts:
1. Classical part which reduces factorisation to a problem of finding the period of the function. 
2. Quantum portion: uses a quantum computer to find the period using the Quantum Fourier Transform 

For algorithm the steps are:
1. Pick a random number A such that A < N
2. Compute greatest common divisor (GCD) of an N
3. If GCD != 1 then you've found a factor of N
4. If not then run the quantum circuit that uses a Quantum Fourier Transform
5. If the period is odd then go back to step 1
6. Otherwise you've found the factors of N