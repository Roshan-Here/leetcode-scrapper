import pytest
from q_0658_findKClosestElements import Solution


@pytest.mark.parametrize(
    "arr, k, x, output",
    [([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]), ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4])],
)
class TestSolution:
    def test_findClosestElements(
        self, arr: List[int], k: int, x: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findClosestElements(
                arr,
                k,
                x,
            )
            == output
        )
