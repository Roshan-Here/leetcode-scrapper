import pytest
from q_0189_rotateArray import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
class TestSolution:
    def test_rotate(self, nums: List[int], k: int, output: None):
        sc = Solution()
        assert (
            sc.rotate(
                nums,
                k,
            )
            == output
        )
