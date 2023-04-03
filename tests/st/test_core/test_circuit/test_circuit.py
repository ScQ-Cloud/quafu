# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

# pylint: disable=invalid-name
"""Test circuit."""
import numpy as np
import pytest

from mindquantum.config import set_context
from mindquantum.core import gates as G
from mindquantum.core.circuit import UN, Circuit, add_prefix, shift
from mindquantum.core.parameterresolver import ParameterResolver
from mindquantum.simulator import Simulator
from mindquantum.simulator.simulator import available_backend

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

try:
    importlib_metadata.import_module("numba")
    _HAS_NUMBA = True
except ImportError:
    _HAS_NUMBA = False

AVAILABLE_BACKEND = available_backend()


def test_circuit_qubits_grad():
    """
    Description: Test circuit basic operations
    Expectation:
    """
    circuit1 = Circuit()
    circuit1 += G.RX('a').on(0)
    circuit1 *= 2
    circuit2 = Circuit([G.X.on(0, 1)])
    circuit3 = circuit1 + circuit2
    assert len(circuit3) == 3
    assert circuit3.n_qubits == 2
    circuit3.insert(0, G.H.on(0))
    assert circuit3[0] == G.H(0)
    circuit3.no_grad()
    assert len(circuit3[1].coeff.requires_grad_parameters) == 0
    circuit3.requires_grad()
    assert len(circuit3[1].coeff.requires_grad_parameters) == 1
    assert len(circuit3.parameter_resolver()) == 1


@pytest.mark.level0
@pytest.mark.platform_x86_gpu_training
@pytest.mark.platform_x86_cpu
@pytest.mark.env_onecard
@pytest.mark.parametrize('config', AVAILABLE_BACKEND)
def test_get_matrix(config):
    """
    test
    Description:
    Expectation:
    """
    backend, dtype, device = config
    if backend:
        return
    set_context(dtype=dtype, device_target=device)
    circ = Circuit().ry('a', 0).rz('b', 0).ry('c', 0)
    matrix = circ.matrix(np.array([7.902762e-01, 2.139225e-04, 7.795934e-01]), backend=backend)
    assert np.allclose(matrix[0, 0], 0.70743435 - 1.06959724e-04j)


def test_circuit_apply():
    """
    Description: Test apply value to parameterized circuit
    Expectation:
    """
    circuit = Circuit()
    circuit += G.RX('a').on(0, 1)
    circuit += G.H.on(0)
    circuit = circuit.apply_value({'a': 0.2})
    circuit_exp = Circuit([G.RX(0.2).on(0, 1), G.H.on(0)])
    assert circuit == circuit_exp


@pytest.mark.level0
@pytest.mark.platform_x86_gpu_training
@pytest.mark.platform_x86_cpu
@pytest.mark.env_onecard
@pytest.mark.parametrize('config', AVAILABLE_BACKEND)
def test_evolution_state(config):
    """
    test
    Description:
    Expectation:
    """

    backend, dtype, device = config
    set_context(dtype=dtype, device_target=device)
    a, b = 0.3, 0.5
    circ = Circuit([G.RX('a').on(0), G.RX('b').on(1)])
    simulator = Simulator(backend, circ.n_qubits)
    simulator.apply_circuit(circ, ParameterResolver({'a': a, 'b': b}))
    state = simulator.get_qs()
    state_exp = [0.9580325796404553, -0.14479246283091116j, -0.2446258794777393j, -0.036971585637570345]
    if backend == "mqmatrix":
        assert np.allclose(state, np.outer(state_exp, np.conj(state_exp)))
    else:
        assert np.allclose(state, state_exp)


def test_is_measure_end():
    """
    test
    Description:
    Expectation:
    """
    circ1 = Circuit().x(0)
    assert circ1.is_measure_end
    circ1 += G.Measure().on(0)
    circ1 += G.BARRIER
    assert circ1.is_measure_end
    circ1 += G.X.on(0, 1)
    assert not circ1.is_measure_end


def test_circuit_operator():
    """
    test
    Description: test sum of circuit and shift qubit and add prefix of parameters.
    Expectation: success.
    """
    template = Circuit([G.X.on(1, 0), G.RX('a').on(1), G.X.on(1, 0)])
    circ = sum(shift(add_prefix(template, f'l{i}'), i) for i in range(3))
    circ_exp = Circuit()
    for i in range(3):
        circ_exp += G.X.on(i + 1, i)
        circ_exp += G.RX(f'l{i}_a').on(i + 1)
        circ_exp += G.X.on(i + 1, i)
    assert circ == circ_exp


@pytest.mark.skipif(not _HAS_NUMBA, reason='Numba is not installed')
def test_circ_subs():
    """
    test circ substitute.
    Description: test substitute value to parameterized quantum circuit.
    Expectation: success.
    """

    def rx_matrix_generator(x):
        return np.array([[np.cos(x / 2), -1j * np.sin(x / 2)], [-1j * np.sin(x / 2), np.cos(x / 2)]])

    def rx_diff_matrix_generator(x):
        return np.array([[np.sin(x / 2), 1j * np.cos(x / 2)], [1j * np.cos(x / 2), np.sin(x / 2)]]) / -2

    circuit = Circuit()
    circuit += UN(G.H, 3)
    circuit.x(0).y(1).z(2)
    circuit += G.SWAP([0, 2], 1)
    circuit.rx('x', 1).ry('y', 0).rzz('zz', [1, 2])
    circuit += G.gene_univ_parameterized_gate('fake_x', rx_matrix_generator, rx_diff_matrix_generator)('a').on(0)
    circuit += G.FSim('theta', 'phi').on([0, 2])
    pr = {'x': 1.2, 'y': 3.4, 'zz': 5.6, 'a': 1.4, 'theta': 3.5, 'phi': 5.7}
    qs_1 = circuit.get_qs(pr=pr)
    qs_2 = circuit.subs(pr).get_qs()
    assert np.allclose(qs_1, qs_2)
