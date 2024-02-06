const { linearSearch, globalLinearSearch } = require("./linearSearch.js");

describe("tests linearSearch", () => {
  test("linearSearch(1, [1, 2, 3]) === 0", () => {
    expect(linearSearch(1, [1, 2, 3])).toBe(0);
  });

  test("linearSearch(3, [1, 2, 3]) === 2", () => {
    expect(linearSearch(3, [1, 2, 3])).toBe(2);
  });

  test("linearSearch(4, [1, 2, 3]) === undefined", () => {
    expect(linearSearch(4, [1, 2, 3])).toBe(undefined);
  });

  test("linearSearch('a' [1, 'a', 3, 4, 'z']) === 1", () => {
    expect(linearSearch('a', [1, 'a', 3, 4, 'z'])).toBe(1);
  });

  test("linearSearch('a', [1, 2, 3]) === undefined", () => {
    expect(linearSearch("a", [1, 2, 3])).toBe(undefined);
  });
});

describe("tests globalLinearSearch", () => {
  test("globalLinearSearch('a', 'bananas'.split('')) === [1, 3, 5]", () => {
    expect(globalLinearSearch("a", "bananas".split(""))).toEqual([1, 3, 5]);
  });

  test("globalLinearSearch('s', 'bananas'.split('')) === [6]", () => {
    expect(globalLinearSearch("s", "bananas".split(""))).toEqual([6]);
  });

  test("globalLinearSearch('n', 'bananas'.split('')) === [2, 4]", () => {
    expect(globalLinearSearch("n", "bananas".split(""))).toEqual([2, 4]);
  });

  test("globalLinearSearch('3', [2,3,5,6,3]) === [1, 4]", () => {
    expect(globalLinearSearch(3, [2,3,5,6,3])).toEqual([1, 4]);
  });

  test("globalLinearSearch('z', 'bananas'.split('')) === undefined", () => {
    expect(globalLinearSearch("z", "bananas".split(""))).toEqual(undefined);
  });
});
