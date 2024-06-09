import pytest
from q_0228_summaryRanges import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ],
)
class TestSolution:
    def test_summaryRanges(self, nums: List[int], output: List[str]):
        sc = Solution()
        assert (
            sc.summaryRanges(
                nums,
            )
            == output
        )
