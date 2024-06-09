import pytest
from q_1766_treeOfCoprimes import Solution


@pytest.mark.parametrize(
    "nums, edges, output",
    [
        ([2, 3, 3, 2], [[0, 1], [1, 2], [1, 3]], [-1, 0, 0, 1]),
        (
            [5, 6, 10, 2, 3, 6, 15],
            [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
            [-1, 0, -1, 0, 0, 0, -1],
        ),
    ],
)
class TestSolution:
    def test_getCoprimes(
        self, nums: List[int], edges: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.getCoprimes(
                nums,
                edges,
            )
            == output
        )
