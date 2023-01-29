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
"""RZ gate related decompose rule."""

from mindquantum.core import gates
from mindquantum.core.circuit import Circuit
from mindquantum.utils.type_value_check import _check_control_num, _check_input_type


def crz_decompose(gate: gates.RZ):
    """
    Decompose crz gate.

    Args:
        gate (RZ): a RZ gate with one control qubits.

    Returns:
        List[Circuit], all possible decompose solution.

    Examples:
        >>> from mindquantum.algorithm.compiler.decompose import crz_decompose
        >>> from mindquantum.core.circuit import Circuit
        >>> from mindquantum.core.gates import X, RZ
        >>> crz = RZ(1).on(1, 0)
        >>> origin_circ = Circuit() + crz
        >>> decomposed_circ = crz_decompose(crz)[0]
        >>> origin_circ
        q0: ────●────
                │
        q1: ──RZ(1)──
        >>> decomposed_circ
        q0: ──────────────●─────────────────●──
                          │                 │
        q1: ──RZ(1/2)─────X─────RZ(-1/2)────X──
    """
    _check_input_type('gate', gates.RZ, gate)
    _check_control_num(gate.ctrl_qubits, 1)
    circuit = Circuit()
    control = gate.ctrl_qubits[0]
    target = gate.obj_qubits[0]
    circuit += gates.RZ(gate.coeff / 2).on(target)
    circuit += gates.X.on(target, control)
    circuit += gates.RZ(-gate.coeff / 2).on(target)
    circuit += gates.X.on(target, control)
    return [circuit]


decompose_rules = ['crz_decompose']

__all__ = decompose_rules
