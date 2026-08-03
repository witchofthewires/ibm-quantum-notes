import sys

import qiskit
import qiskit_aer
import qiskit_ibm_runtime

def print_pyver():
    print(f"Python: {sys.version.split()[0]}")

def print_qiskit_info():
    print(f"qiskit: {qiskit.__version__}")
    print(f"qiskit-aer: {qiskit_aer.__version__}")
    print(f"qiskit-ibm-runtime: {qiskit_ibm_runtime.__version__}")

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

def run_circuit_and_get_counts(circuit, backend, shots=1000):
    """
    Runs a quantum circuit on a specified backend and returns the measurement counts.

    Args:
        circuit (QuantumCircuit): The quantum circuit to run.
        backend: The Qiskit backend (real device or simulator).
        shots (int): The number of shots to run the circuit.

    Returns:
        dict: A dictionary of measurement counts.
    """
    print("hiya")
    pm = qiskit.transpiler.generate_preset_pass_manager(backend=backend, optimization_level=1)
    print("let's get started")
    isa_circuit = pm.run(circuit)
    print("first here")
    sampler = qiskit_ibm_runtime.Sampler(mode=backend)
    print("and now here")
    job = sampler.run([isa_circuit], shots=shots)
    print("got result!")
    result = job.result()
    print(f"here it is: {result}") 
    
    return result[0].data.meas.get_counts()

import yaml

def register_backend(secrets_file):
    token = ''
    with open(secrets_file) as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        token = cfg['token']
        
    qiskit_ibm_runtime.QiskitRuntimeService.save_account(channel='ibm_quantum_platform', token=token, overwrite=True, set_as_default=True)
    service = qiskit_ibm_runtime.QiskitRuntimeService(channel='ibm_quantum_platform')

    # load saved credentials
    service = qiskit_ibm_runtime.QiskitRuntimeService()

    # use the least busy backend, or uncomment the loading of a specific backend like "ibm_fez"
    backend = service.least_busy(operational=True, simulator=False, min_num_qubits=127)
    # backend = serivce.backend("ibm_fez")
    print(f"Registered backend: {backend.name}")
    return backend