import pytest
from q_3129_findAllPossibleStableBinaryArraysI import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_numberOfStableArrays(self, zero: int, one: int, limit: int, output: int):
        sc = Solution()
        assert sc.numberOfStableArrays() == output
