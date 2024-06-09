import pytest
from q_0989_addToArrayFormOfInteger import Solution


@pytest.mark.parametrize(
    "num, k, output",
    [
        ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
        ([2, 7, 4], 181, [4, 5, 5]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
    ],
)
class TestSolution:
    def test_addToArrayForm(self, num: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.addToArrayForm(
                num,
                k,
            )
            == output
        )
