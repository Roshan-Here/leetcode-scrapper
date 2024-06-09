import pytest
from q_2317_maximumXorAfterOperations import Solution


@pytest.mark.parametrize("nums, output", [([3, 2, 4, 6], 7), ([1, 2, 3, 9, 2], 11)])
class TestSolution:
    def test_maximumXOR(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumXOR(
                nums,
            )
            == output
        )
