/**
 * cart.js
 * Synthetic test file — contains a DELIBERATE functional bug,
 * tagged ISSUE-1, for code-review-pipeline testing.
 */

function calculateCartTotal(items) {
  let total = 0;

  for (const item of items) {
    // ISSUE-1: price comes from a form field as a string ("19.99"),
    // and `total` starts as a number, but no Number()/parseFloat()
    // conversion happens here. For the first item this coerces `total`
    // to a string, and every item after that gets string-concatenated
    // instead of added — e.g. [ "19.99", "5.00" ] produces "019.995.00"
    // instead of 24.99.
    total += item.price;
  }

  return total;
}

module.exports = { calculateCartTotal };
