import pytest
from q_2615_sumOfDistances import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 1, 1, 2], [5, 0, 3, 4, 0]), ([0, 5, 3], [0, 0, 0])]
)
class TestSolution:
    def test_distance(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.distance(
                nums,
            )
            == output
        )
