import pytest

from sort import radix as mod

CASES = [
    ('digit', [123, 10], 2, False),
    ('digit', [-45, 1], 5, False),
    ('counting_sort', [[21, 12, 11], 1], [21, 11, 12], False),
    ('radix_sort', [[170, 45, 75, 90]], [45, 75, 90, 170], False),
    ('radix_sort', [[]], [], False),
    ('max_value', [[3, 1, 2]], 3, False),
    ('is_sorted', [[1, 2, 2, 3]], True, False),
    ('is_sorted', [[2, 1]], False, False),
    ('digit', [0, 1], 0, False),
    ('counting_sort', [[], 1], [], False),
    ('radix_sort', [[9, 8, 7]], [7, 8, 9], False),
    ('max_value', [[]], 0, False),
    ('is_sorted', [[]], True, False),
    ('radix_sort', [[1]], [1], False),
    ('max_value', [[-5, -1]], -1, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_radix_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
