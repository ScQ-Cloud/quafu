//   Copyright 2022 <Huawei Technologies Co., Ltd>
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.

#ifndef FERMION_OPERATOR_HPP
#define FERMION_OPERATOR_HPP

#include <tuple>
#include <vector>

#include <Eigen/SparseCore>

#include "core/config.hpp"

#include "ops/gates/terms_operator.hpp"

namespace mindquantum::ops {

//! Definition of a fermionic operator
/*!
 *
 *  The Fermion Operator such as FermionOperator(' 4^ 3 9 3^ ') are used to represent
 *  \f$a_4^\dagger a_3 a_9 a_3^\dagger\f$.
 *
 *  These are the Basic Operators to describe a fermionic system, such as a Molecular system. The FermionOperator are
 *  follows the anti-commutation relationship.
 */
class FermionOperator : public TermsOperator<FermionOperator> {
    friend TermsOperator<FermionOperator>;

 public:
    using csr_matrix_t = Eigen::SparseMatrix<std::complex<double>, Eigen::RowMajor>;

    static constexpr std::string_view kind() {
        return "mindquantum.fermionoperator";
    }

    FermionOperator() = default;

    explicit FermionOperator(term_t term, coefficient_t coefficient = 1.0);

    explicit FermionOperator(const std::vector<term_t>& term, coefficient_t coeff = 1.0);

    explicit FermionOperator(complex_term_dict_t terms);

    // -------------------------------------------------------------------

    MQ_NODISCARD std::optional<csr_matrix_t> matrix(std::optional<uint32_t> n_qubits) const;

    //! Split the operator into its individual components
    MQ_NODISCARD std::vector<FermionOperator> split() const noexcept;

    //! Return the normal ordered form of the Fermion Operator.
    MQ_NODISCARD self_t normal_ordered() const;

 private:
    //! Return the normal ordered term of the FermionOperator with high index and creation operator in front.
    static FermionOperator normal_ordered_term_(std::vector<term_t> terms, coefficient_t coeff);

    //! Simplify the list of local operators
    static std::tuple<std::vector<term_t>, coefficient_t> simplify_(std::vector<term_t> terms,
                                                                    coefficient_t coeff = 1.);
};

}  // namespace mindquantum::ops

#endif /* FERMION_OPERATOR_HPP */
