import pytest
from q_0503_nextGreaterElementIi import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 1], [2, -1, 2]), ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4])]
)
class TestSolution:
    def test_nextGreaterElements(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.nextGreaterElements(
                nums,
            )
            == output
        )
