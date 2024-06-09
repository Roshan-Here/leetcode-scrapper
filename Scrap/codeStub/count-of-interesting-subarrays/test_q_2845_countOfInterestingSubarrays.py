import pytest
from q_2845_countOfInterestingSubarrays import Solution


@pytest.mark.parametrize(
    "nums, modulo, k, output", [([3, 2, 4], 2, 1, 3), ([3, 1, 9, 6], 3, 0, 2)]
)
class TestSolution:
    def test_countInterestingSubarrays(
        self, nums: List[int], modulo: int, k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.countInterestingSubarrays(
                nums,
                modulo,
                k,
            )
            == output
        )
