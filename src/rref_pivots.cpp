#include <RcppArmadillo.h>
// [[Rcpp::depends(RcppArmadillo)]]

/**
 * @title Compute Row Reduced Echelon Form (RREF) and Pivot Columns
 * @description This function computes the row reduced echelon form (RREF) of a matrix and returns the indices of the pivot columns.
 * @param A A numeric matrix.
 * @return A list containing the RREF matrix and the indices of the pivot columns.
 * @examples
 * \dontrun{
 * A <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, byrow = TRUE)
 * result <- rref_with_pivots(A)
 * print(result$RREF)
 * print(result$pivots)
 * }
 */
// [[Rcpp::export]]
Rcpp::List rref_with_pivots(const arma::mat& A) {
  arma::mat R = A;  // Copy of the input matrix to avoid modifying the original
  int lead = 0;  // Leading column index
  int rowCount = R.n_rows;  // Number of rows in the matrix
  int columnCount = R.n_cols;  // Number of columns in the matrix
  std::vector<int> pivot_columns;  // Vector to store pivot column indices

  for (int r = 0; r < rowCount; ++r) {
    if (lead >= columnCount) {
      return Rcpp::List::create(Rcpp::Named("RREF") = R, Rcpp::Named("pivots") = pivot_columns);
    }
    int i = r;
    // Find the pivot row
    while (R(i, lead) == 0) {
      ++i;
      if (i == rowCount) {
        i = r;
        ++lead;
        if (lead == columnCount) {
          return Rcpp::List::create(Rcpp::Named("RREF") = R, Rcpp::Named("pivots") = pivot_columns);
        }
      }
    }
    // Swap rows r and i
    if (i != r) {
      arma::rowvec temp = R.row(r);
      R.row(r) = R.row(i);
      R.row(i) = temp;
    }
    // Normalize the pivot row
    R.row(r) /= R(r, lead);
    // Eliminate the leading coefficient from other rows
    for (int j = 0; j < rowCount; ++j) {
      if (j != r) {
        R.row(j) -= R.row(r) * R(j, lead);
      }
    }
    pivot_columns.push_back(lead);  // Store the pivot column index
    ++lead;
  }
  return Rcpp::List::create(Rcpp::Named("RREF") = R, Rcpp::Named("pivots") = pivot_columns);
}
