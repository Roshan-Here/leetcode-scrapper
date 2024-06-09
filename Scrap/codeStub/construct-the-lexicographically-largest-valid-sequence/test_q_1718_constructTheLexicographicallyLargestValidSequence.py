import pytest
from q_1718_constructTheLexicographicallyLargestValidSequence import Solution


@pytest.mark.parametrize(
    "n, output", [(3, [3, 1, 2, 3, 2]), (5, [5, 3, 1, 4, 3, 5, 2, 4, 2])]
)
class TestSolution:
    def test_constructDistancedSequence(self, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.constructDistancedSequence(
                n,
            )
            == output
        )
