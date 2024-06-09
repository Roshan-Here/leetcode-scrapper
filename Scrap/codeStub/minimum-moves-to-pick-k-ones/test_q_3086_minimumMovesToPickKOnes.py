import pytest
from q_3086_minimumMovesToPickKOnes import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumMoves(self, nums: List[int], k: int, maxChanges: int, output: int):
        sc = Solution()
        assert sc.minimumMoves() == output
