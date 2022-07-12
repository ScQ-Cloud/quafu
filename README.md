# ScQKit

Python toolkit for submitting quantum circuits on the superconducting quantum computing cloud [ScQ.Cloud](http://q.iphy.ac.cn/). 


## Introduction

ScQkit is developed for the users of [ScQ.Cloud](http://q.iphy.ac.cn/) to construct, compile and execute quantum circuits on real quantum devices. One can use ScQKit to interact with different quantum backends provides by the experimental group of [ScQ.Cloud](http://q.iphy.ac.cn/). 

## Examples

1. Execute circuit on ScQ.Cloud:

```python

import numpy as np
from quantum_circuit import QuantumCircuit

q = QuantumCircuit(5)
for i in range(5):
    if i % 2 == 0:
        q.x(i)

q.barrier([0])
q.cnot(2, 1)
q.ry(1, np.pi/2)
q.rx(2, np.pi)
q.rz(3, 0.1)
q.cz(2, 3)
measures = [0, 1, 2, 3, 4]
q.measure(measures, 1000)
q.set_backend("IOP")
q.set_compiler("default")
res = q.send()
```

2. Execute circuit with observables measurement task. The following code measures the energy expectation of an Ising Hamiltonian with the output states of the quantum circuit:

```python
q = QuantumCircuit(5)

for i in range(5):
    if i % 2 == 0:
        q.h(i)
measures = [0, 1, 2, 3, 4]
q.measure(measures, 1000)
q.set_backend("IOP")
test_Ising = [["X", [i]] for i in range(5)]
test_Ising.extend([["ZZ", [i, i+1]] for i in range(4)])
res, obsexp = q.submit_task(test_Ising)
E = sum(obsexp)
```
## Authors
This project is developed by the quantum cloud computing team at the Beijing Academy of Quantum Information Sciences.