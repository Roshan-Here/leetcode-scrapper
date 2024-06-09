import pytest
from q_3146_permutationDifferenceBetweenTwoStrings import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_findPermutationDifference(self, s: str, t: str, output: int):
        sc = Solution()
        assert sc.findPermutationDifference() == output
