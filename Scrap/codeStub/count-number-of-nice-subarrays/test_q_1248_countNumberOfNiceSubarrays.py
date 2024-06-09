import pytest
from q_1248_countNumberOfNiceSubarrays import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 1, 2, 1, 1], 3, 2),
        ([2, 4, 6], 1, 0),
        ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2, 16),
    ],
)
class TestSolution:
    def test_numberOfSubarrays(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfSubarrays(
                nums,
                k,
            )
            == output
        )
