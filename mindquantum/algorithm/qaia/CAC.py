# Copyright 2023 Huawei Technologies Co., Ltd
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
"""Coherent Ising Machine with chaotic amplitude control algorithm."""
# pylint: disable=invalid-name
import numpy as np
from scipy.sparse import csr_matrix

from mindquantum.utils.type_value_check import _check_number_type, _check_value_should_not_less
from .QAIA import QAIA


class CAC(QAIA):
    r"""
    Coherent Ising Machine with chaotic amplitude control algorithm.

    Reference: `Coherent Ising machines with optical error correction
    circuits <https://onlinelibrary.wiley.com/doi/full/10.1002/qute.202100077>`_.

    Note:
        For memory efficiency, the input array 'x' is not copied and will be modified
        in-place during optimization. If you need to preserve the original data,
        please pass a copy using `x.copy()`.

    Args:
        J (Union[numpy.array, scipy.sparse.spmatrix]): The coupling matrix with shape :math:`(N x N)`.
        h (numpy.array): The external field with shape :math:`(N, )`.
        x (numpy.array): The initialized spin value with shape :math:`(N x batch_size)`.
            Will be modified during optimization. If not provided (``None``), will be initialized as
            random values drawn from normal distribution N(0, 10^(-4)). Default: ``None``.
        n_iter (int): The number of iterations. Default: ``1000``.
        batch_size (int): The number of sampling. Default: ``1``.
        dt (float): The step size. Default: ``0.075``.

    Examples:
        >>> import numpy as np
        >>> from mindquantum.algorithm.qaia import CAC
        >>> J = np.array([[0, -1], [-1, 0]])
        >>> solver = CAC(J, batch_size=5)
        >>> solver.update()
        >>> print(solver.calc_cut())
        [1. 1. 1. 1. 1.]
        >>> print(solver.calc_energy())
        [-1. -1. -1. -1. -1.]
    """

    # pylint: disable=too-many-arguments,too-many-instance-attributes
    def __init__(
        self,
        J,
        h=None,
        x=None,
        n_iter=1000,
        batch_size=1,
        dt=0.075,
    ):
        """Construct CAC algorithm."""
        _check_number_type("dt", dt)
        _check_value_should_not_less("dt", 0, dt)
        super().__init__(J, h, x, n_iter, batch_size)
        self.J = csr_matrix(self.J)
        self.N = self.J.shape[0]
        self.dt = dt
        # The number of first iterations
        self.Tr = int(0.9 * self.n_iter)
        # The number of additional iterations
        self.Tp = self.n_iter - self.Tr
        # pumping parameters
        self.p = np.hstack([np.linspace(-0.5, 1, self.Tr), np.ones(self.Tp)])
        # target amplitude
        self.alpha = np.hstack([np.linspace(1, 3, self.Tr), 3.0 * np.ones(self.Tp)])
        # coupling strength
        self.xi = np.sqrt(2 * self.N / np.sum(self.J**2))
        # rate of change of error variables
        self.beta = 0.3
        self.initialize()

    def initialize(self):
        """Initialize spin values and error variables."""
        if self.x is None:
            self.x = np.random.normal(0, 10 ** (-4), size=(self.N, self.batch_size))

        if self.x.shape[0] != self.N:
            raise ValueError(f"The size of x {self.x.shape[0]} is not equal to the number of spins {self.N}")

        self.e = np.ones((self.N, self.batch_size))

    # pylint: disable=attribute-defined-outside-init
    def update(self):
        """Dynamical evolution."""
        for i in range(self.n_iter):
            if self.h is None:
                self.x = (
                    self.x + (-self.x**3 + (self.p[i] - 1) * self.x + self.xi * self.e * (self.J @ self.x)) * self.dt
                )
            else:
                self.x = (
                    self.x
                    + (-self.x**3 + (self.p[i] - 1) * self.x + self.xi * self.e * (self.J @ self.x + self.h)) * self.dt
                )

            self.e = self.e + (-self.beta * self.e * (self.x**2 - self.alpha[i])) * self.dt

            cond = np.abs(self.x) > (1.5 * np.sqrt(self.alpha[i]))
            self.x = np.where(cond, 1.5 * np.sign(self.x) * np.sqrt(self.alpha[i]), self.x)
