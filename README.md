## Varför prata om kvantdatorer?

- [DEF CON Hacking Conference](https://defcon.org)
- [When will the cracking begin?](https://www.youtube.com/watch?v=OkVYJx1iLNs)
- [Ekerå, KTH](https://www.kth.se/om/nyheter/centrala-nyheter/forskar-om-att-framtidssakra-internet-1.1366813)
2030 har vi kvantdatorer som knäcker dagens krypto
- ["Chinese Scientists Hacked ..."](https://www.infosecglobal.com/news/chinese-scientists-allegedly-quantum-hack-military-grade-encryption-with-quantum-computer)

## Scope

### Del 1

- Vad är en kvantdator?

### Del 2

- Vad betyder Q-day?
- Hur kan kvantdatorer knäcka dagens krypto?
- Hur ska vi skydda oss från kvantdatorattacker?

## De första experimenten

- Young's dubbelspalt
- Newton Opticks "corpuscular"
- Svartkroppsstrålning
- Fotoelektriska effekten
- Stern Gerlach

## Solvay Conference 1927

Mest kända Solvay, var en konferens i Bryssel 1927

"The Most Intelligent Picture Ever Taken"

## Nobelpriser

Några viktiga årtal för kvantfysiken
- [1918](https://www.nobelprize.org/prizes/physics/1918/summary/)
- [1921](https://www.nobelprize.org/prizes/physics/1921/summary/)
- [1922](https://www.nobelprize.org/prizes/physics/1922/summary/)
- [1932](https://www.nobelprize.org/prizes/physics/1932/summary/)
- [1933](https://www.nobelprize.org/prizes/physics/1933/summary/)
- [1965](https://www.nobelprize.org/prizes/physics/1965/summary/)
- [2022](https://www.nobelprize.org/prizes/physics/2022/summary/)
- [2025](https://www.nobelprize.org/prizes/physics/2025/summary/)

[John Bell](https://en.wikipedia.org/wiki/John_Stewart_Bell) hann inte få sitt pris 🥹

## Världen utan upptäkten av kvantfysik

Steampunk?

## Viktiga upptäckter och begrepp

- Kvantobjekt (inte partikel, inte våg), tex foton, elektron, joner (atomer)
- Bells teorem
- Quantum Superposition (spin, energinivå, elektrisk laddning)
- Quantum Measurement, superposition collapses
- Quantum Entanglement, sammanflätning, nobelpris 2022
- (Quantum Tunneling) nobelpris 2025

## Kvantdator

- Varför ser den ut som den gör?
- Eliminering av termisk strålning, bakgrundsstrålning
- Kylning
- Mikrovågor & laser för styrning
- Olika typer: Supraledande qubits, Trapped ions, Photonic qubits, Neutral atoms
- Andra typer av kvantdatorer: Quantum annealer

## Kvantdator byggblock

- Qubit
- Bloch sphere
- Transformationer, tex Hadamart
- Hadamart ger Equal superposition
- Circuit diagram
- Fysiska (noisy) vs logiska qubits

## Jämför med första radiorörsdatorerna

- Några 1000 radiorör
- Viktigt med felhantering
- Checkpoints, spara undan beräkningar för att kunna backa vid ev. krasch
- Checksummor
- Felkorrigerande kod (Error Correction tex Hamming code)

## Kryptografi

- Cyclic group, modulo-beräkning
- RSA, modulo upphöjt i
- Elliptisk kurva
- Diffie Hellman
- Discrete logarithm problem [DLP](https://fse.studenttheses.ub.rug.nl/22792/1/bMATH_2020_HofmanSJ.pdf)

Find p such that: g^p mod N = 1

- Ca 4000 logiska qubits knäcker RSA 2048

Om N = r * q

och du hittar p genom DLP, då är

(g^p -1) = (g^(p/2) - 1)*(g^(p/2) + 1) = m*N

Och 

r = gcd(g^(p/2) - 1, N)

q = gcd(g^(p/2) + 1, N)

## Beräkningar

### Mjukvara

- [IBM Qiskit](https://www.ibm.com/quantum/qiskit)
- [Quirk (enbart simulator)](https://algassert.com/quirk)
- [Classiq](https://platform.classiq.io/)
- [Google Cirq](https://quantumai.google/cirq)

### On-premise

- [D-Wave](https://www.dwavequantum.com/)

### Cloud

- [IBM Cloud](https://quantum.cloud.ibm.com/)
- [IONQ](https://ionq.com/quantum-cloud)
- [Microsoft](https://quantum.microsoft.com/)

## Shor's algoritm 1994

- Kvantalgoritm för att hitta primtalsfaktorerna för ett heltal
- Löser Discrete log problemet

[Quirk](https://algassert.com/quirk#circuit=%7B%22cols%22:[[1,1,1,1,1,1,1,1,1,1,%22~input%22,1,1,1,%22~guess%22],[1,1,1,1,1,1,1,1,1,1,%7B%22id%22:%22setR%22,%22arg%22:55%7D,1,1,1,%7B%22id%22:%22setB%22,%22arg%22:17%7D],[],[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22X%22],[%22inputA10%22,1,1,1,1,1,1,1,1,1,%22*BToAmodR6%22],[%22QFT%E2%80%A010%22],[1,1,1,1,%22~out%22],[%22Chance10%22]],%22gates%22:[%7B%22id%22:%22~guess%22,%22name%22:%22guess:%22,%22matrix%22:%22%7B%7B1,0,0,0%7D,%7B0,1,0,0%7D,%7B0,0,1,0%7D,%7B0,0,0,1%7D%7D%22%7D,%7B%22id%22:%22~input%22,%22name%22:%22input:%22,%22matrix%22:%22%7B%7B1,0,0,0%7D,%7B0,1,0,0%7D,%7B0,0,1,0%7D,%7B0,0,0,1%7D%7D%22%7D,%7B%22id%22:%22~out%22,%22name%22:%22out:%22,%22matrix%22:%22%7B%7B1,0,0,0%7D,%7B0,1,0,0%7D,%7B0,0,1,0%7D,%7B0,0,0,1%7D%7D%22%7D]%7D)

## Grover's algoritm 1996

[CNOT](https://cnot.io/quantum_algorithms/grover/grovers_algorithm.html)

[Grover 1 step loop](https://algassert.com/quirk#circuit=%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22],[1,1,1,1,1,1,%22Z%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22Chance6%22]],%22gates%22:[%7B%22id%22:%22~oibm%22,%22name%22:%22Uw%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~s7dn%22,%22name%22:%22Uw*%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~d7ap%22,%22name%22:%22H%22,%22circuit%22:%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22]]%7D%7D]%7D)

[Grover 2 steps loop](https://algassert.com/quirk#circuit=%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22],[1,1,1,1,1,1,%22Z%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22Chance6%22]],%22gates%22:[%7B%22id%22:%22~oibm%22,%22name%22:%22Uw%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~s7dn%22,%22name%22:%22Uw*%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~d7ap%22,%22name%22:%22H%22,%22circuit%22:%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22]]%7D%7D]%7D)

[Grover 3 steps loop](https://algassert.com/quirk#circuit=%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22],[1,1,1,1,1,1,%22Z%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22Chance6%22]],%22gates%22:[%7B%22id%22:%22~oibm%22,%22name%22:%22Uw%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~s7dn%22,%22name%22:%22Uw*%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~d7ap%22,%22name%22:%22H%22,%22circuit%22:%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22]]%7D%7D]%7D)

[Grover 4 steps loop](https://algassert.com/quirk#circuit=%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22],[1,1,1,1,1,1,%22Z%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22~oibm%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22],[%22~s7dn%22],[%22~d7ap%22],[%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22%E2%97%A6%22,%22X%22],[%22~d7ap%22],[%22Chance6%22]],%22gates%22:[%7B%22id%22:%22~oibm%22,%22name%22:%22Uw%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~s7dn%22,%22name%22:%22Uw*%22,%22circuit%22:%7B%22cols%22:[[1,%22X%22,%22X%22,1,1,%22X%22]]%7D%7D,%7B%22id%22:%22~d7ap%22,%22name%22:%22H%22,%22circuit%22:%7B%22cols%22:[[%22H%22,%22H%22,%22H%22,%22H%22,%22H%22,%22H%22]]%7D%7D]%7D)

# Hur ser krypton ut efter att fungerande kvantdatorer finns?

[Redhat](https://www.redhat.com/en/blog/post-quantum-cryptography-lattice-based-cryptography)

- PQC post quantum cryptography
- Lattice-based cryptography
- Hybrid post-quantum encryption

Innebär att man kombinerar klassiska krypteringssalgoritmer med post kvantdator kryptering
