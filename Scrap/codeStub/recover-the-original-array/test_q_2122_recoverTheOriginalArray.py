import pytest
from q_2122_recoverTheOriginalArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([2, 10, 6, 4, 8, 12], [3, 7, 11]), ([1, 1, 3, 3], [2, 2]), ([5, 435], [220])],
)
class TestSolution:
    def test_recoverArray(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.recoverArray(
                nums,
            )
            == output
        )
