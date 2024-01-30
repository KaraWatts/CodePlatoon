// factorial-spec.js
const factorial = require("./factorial.js");

/**
 * Just 1 test
 */

test("tests factorial(4) = 24", () => {
  expect(factorial(4)).toBe(24);
});


/**
 * Multiple tests
 */

test("tests factorial(0) = 1", () => {
  expect(factorial(0)).toBe(1);
});

test("tests factorial(1) = 1", () => {
  expect(factorial(1)).toBe(1);
});

test("tests factorial(2) = 2", () => {
  expect(factorial(2)).toBe(2);
});

test("tests factorial(3) = 6", () => {
  expect(factorial(3)).toBe(6);
});

/**
 * Using `describe` blocks to organize our tests
 */

describe("tests factorial for small numbers", () => {
  test("tests factorial(0) = 1", () => {
    expect(factorial(0)).toBe(1);
  });

  test("tests factorial(1) = 1", () => {
    expect(factorial(1)).toBe(1);
  });

  test("tests factorial(2) = 2", () => {
    expect(factorial(2)).toBe(2);
  });

  test("tests factorial(3) = 6", () => {
    expect(factorial(3)).toBe(6);
  });
});

describe("tests factorial for large numbers", () => {
  test("tests factorial(10) = 3628800", () => {
    expect(factorial(10)).toBe(3628800);
  });

  test("tests factorial(20) = 2432902008176640000", () => {
    expect(factorial(20)).toBe(2432902008176640000);
  });

  test("tests factorial(40) = 8.15915283247898e47", () => {
    expect(factorial(40)).toBe(8.15915283247898e47);
  });
});