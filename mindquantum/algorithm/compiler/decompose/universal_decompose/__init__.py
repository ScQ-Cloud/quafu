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
"""Universal unitary gate decomposition"""

from .one_qubit_decompose import euler_decompose
from .two_qubit_decompose import tensor_product_decompose, abc_decompose, kak_decompose
from .qs_decompose import qs_decompose, cu_decompose, demultiplex_pair, demultiplex_pauli

__all__ = [
    'euler_decompose',
    'tensor_product_decompose',
    'abc_decompose',
    'kak_decompose',
    'qs_decompose',
    'cu_decompose',
    'demultiplex_pair',
    'demultiplex_pauli',
]
