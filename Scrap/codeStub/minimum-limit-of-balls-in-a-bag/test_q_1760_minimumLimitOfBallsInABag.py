import pytest
from q_1760_minimumLimitOfBallsInABag import Solution


@pytest.mark.parametrize(
    "nums, maxOperations, output", [([9], 2, 3), ([2, 4, 8, 2], 4, 2)]
)
class TestSolution:
    def test_minimumSize(self, nums: List[int], maxOperations: int, output: int):
        sc = Solution()
        assert (
            sc.minimumSize(
                nums,
                maxOperations,
            )
            == output
        )
