import pytest
from q_3134_findTheMedianOfTheUniquenessArray import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_medianOfUniquenessArray(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.medianOfUniquenessArray() == output
