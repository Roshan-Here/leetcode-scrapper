import pytest
from q_3158_findTheXorOfNumbersWhichAppearTwice import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_duplicateNumbersXOR(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.duplicateNumbersXOR() == output
