const fibonacci = require("./fibonacci");

describe("test fibonacci", () => {
  test("fibonacci(0) === 0", () => {
    expect(fibonacci(0)).toBe(0);
  });

  test("fibonacci(2) === 1", () => {
    expect(fibonacci(2)).toBe(1);
  });

  test("fibonacci(5) === 5", () => {
    expect(fibonacci(5)).toBe(5);
  });

  test("fibonacci(8) === 21", () => {
    expect(fibonacci(8)).toBe(21);
  });

  test("fibonacci(11) === 89", () => {
    expect(fibonacci(11)).toBe(89);
  });
});
