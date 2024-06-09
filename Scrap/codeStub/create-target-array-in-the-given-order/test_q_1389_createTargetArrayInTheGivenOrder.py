import pytest
from q_1389_createTargetArrayInTheGivenOrder import Solution


@pytest.mark.parametrize(
    "nums, index, output",
    [
        ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]),
        ([1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4]),
        ([1], [0], [1]),
    ],
)
class TestSolution:
    def test_createTargetArray(
        self, nums: List[int], index: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.createTargetArray(
                nums,
                index,
            )
            == output
        )
