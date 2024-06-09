import pytest
from q_2595_numberOfEvenAndOddBits import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_evenOddBit(self, n: int, output: List[int]):
        sc = Solution()
        assert sc.evenOddBit() == output
