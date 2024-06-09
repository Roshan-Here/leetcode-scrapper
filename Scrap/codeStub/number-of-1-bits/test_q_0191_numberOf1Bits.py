import pytest
from q_0191_numberOf1Bits import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_hammingWeight(self, n: int, output: int):
        sc = Solution()
        assert sc.hammingWeight() == output
