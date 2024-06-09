import pytest
from q_0136_singleNumber import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)]
)
class TestSolution:
    def test_singleNumber(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.singleNumber(
                nums,
            )
            == output
        )
