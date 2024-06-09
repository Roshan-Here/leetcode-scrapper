import pytest
from q_0077_combinations import Solution


@pytest.mark.parametrize(
    "n, k, output",
    [(4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]), (1, 1, [[1]])],
)
class TestSolution:
    def test_combine(self, n: int, k: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.combine(
                n,
                k,
            )
            == output
        )
