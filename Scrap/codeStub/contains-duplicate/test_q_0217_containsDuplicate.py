import pytest
from q_0217_containsDuplicate import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
class TestSolution:
    def test_containsDuplicate(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.containsDuplicate(
                nums,
            )
            == output
        )
