import pytest
from q_2935_maximumStrongPairXorIi import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4, 5], 7), ([10, 100], 0), ([500, 520, 2500, 3000], 1020)],
)
class TestSolution:
    def test_maximumStrongPairXor(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumStrongPairXor(
                nums,
            )
            == output
        )
