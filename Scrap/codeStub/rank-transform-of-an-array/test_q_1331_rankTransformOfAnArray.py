import pytest
from q_1331_rankTransformOfAnArray import Solution


@pytest.mark.parametrize(
    "arr, output",
    [
        ([40, 10, 20, 30], [4, 1, 2, 3]),
        ([100, 100, 100], [1, 1, 1]),
        ([37, 12, 28, 9, 100, 56, 80, 5, 12], [5, 3, 4, 2, 8, 6, 7, 1, 3]),
    ],
)
class TestSolution:
    def test_arrayRankTransform(self, arr: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.arrayRankTransform(
                arr,
            )
            == output
        )
