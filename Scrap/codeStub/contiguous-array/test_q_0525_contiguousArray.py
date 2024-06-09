import pytest
from q_0525_contiguousArray import Solution


@pytest.mark.parametrize("nums, output", [([0, 1], 2), ([0, 1, 0], 2)])
class TestSolution:
    def test_findMaxLength(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMaxLength(
                nums,
            )
            == output
        )
