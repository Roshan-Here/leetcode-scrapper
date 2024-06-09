import pytest
from q_0457_circularArrayLoop import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([2, -1, 1, 2, 2], True),
        ([-1, -2, -3, -4, -5, 6], False),
        ([1, -1, 5, 1, 4], True),
    ],
)
class TestSolution:
    def test_circularArrayLoop(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.circularArrayLoop(
                nums,
            )
            == output
        )
