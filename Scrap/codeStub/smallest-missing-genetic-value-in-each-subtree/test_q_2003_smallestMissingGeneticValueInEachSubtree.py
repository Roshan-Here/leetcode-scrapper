import pytest
from q_2003_smallestMissingGeneticValueInEachSubtree import Solution


@pytest.mark.parametrize(
    "parents, nums, output",
    [
        ([-1, 0, 0, 2], [1, 2, 3, 4], [5, 1, 1, 1]),
        ([-1, 0, 1, 0, 3, 3], [5, 4, 6, 2, 1, 3], [7, 1, 1, 4, 2, 1]),
        ([-1, 2, 3, 0, 2, 4, 1], [2, 3, 4, 5, 6, 7, 8], [1, 1, 1, 1, 1, 1, 1]),
    ],
)
class TestSolution:
    def test_smallestMissingValueSubtree(
        self, parents: List[int], nums: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.smallestMissingValueSubtree(
                parents,
                nums,
            )
            == output
        )
