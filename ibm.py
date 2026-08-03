import sys

import qiskit
import qiskit_aer
import qiskit_ibm_runtime

def generate_bell_phi_plus():
    qsys = qiskit.QuantumCircuit(2)
    qsys.h(0)
    qsys.cx(0,1)
    return qsys

def generate_bell_phi_minus():
    qsys = qiskit.QuantumCircuit(2)
    qsys.h(0)
    qsys.z(0)
    qsys.cx(0,1)
    return qsys

def generate_bell_psi_plus():
    qsys = qiskit.QuantumCircuit(2)
    qsys.h(0)
    qsys.x(1)
    qsys.cx(0,1)
    return qsys

def generate_bell_psi_minus():
    qsys = qiskit.QuantumCircuit(2)
    qsys.h(0)
    qsys.x(1)
    qsys.z(0)
    qsys.z(1)
    qsys.cx(0,1)
    return qsys

def print_pyver():
    print(f"Python: {sys.version.split()[0]}")

def print_qiskit_info():
    print(f"qiskit: {qiskit.__version__}")
    print(f"qiskit-aer: {qiskit_aer.__version__}")
    print(f"qiskit-ibm-runtime: {qiskit_ibm_runtime.__version__}")