import pytest
from q_2612_minimumReverseOperations import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minReverseOperations(
        self, n: int, p: int, banned: List[int], k: int, output: List[int]
    ):
        sc = Solution()
        assert sc.minReverseOperations() == output
