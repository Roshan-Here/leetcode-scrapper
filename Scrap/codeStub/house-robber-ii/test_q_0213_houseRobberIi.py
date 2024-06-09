import pytest
from q_0213_houseRobberIi import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 3, 2], 3), ([1, 2, 3, 1], 4), ([1, 2, 3], 3)]
)
class TestSolution:
    def test_rob(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.rob(
                nums,
            )
            == output
        )
