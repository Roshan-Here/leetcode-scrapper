import pytest
from q_1658_minimumOperationsToReduceXToZero import Solution


@pytest.mark.parametrize(
    "nums, x, output",
    [([1, 1, 4, 2, 3], 5, 2), ([5, 6, 7, 8, 9], 4, -1), ([3, 2, 20, 1, 1, 3], 10, 5)],
)
class TestSolution:
    def test_minOperations(self, nums: List[int], x: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
                x,
            )
            == output
        )
