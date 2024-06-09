import pytest
from q_2009_minimumNumberOfOperationsToMakeArrayContinuous import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 2, 5, 3], 0), ([1, 2, 3, 5, 6], 1), ([1, 10, 100, 1000], 3)]
)
class TestSolution:
    def test_minOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
            )
            == output
        )
