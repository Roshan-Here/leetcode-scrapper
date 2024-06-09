import pytest
from q_2731_movementOfRobots import Solution


@pytest.mark.parametrize(
    "nums, s, d, output", [([-2, 0, 2], "RLL", 3, 8), ([1, 0], "RL", 2, 5)]
)
class TestSolution:
    def test_sumDistance(self, nums: List[int], s: str, d: int, output: int):
        sc = Solution()
        assert (
            sc.sumDistance(
                nums,
                s,
                d,
            )
            == output
        )
