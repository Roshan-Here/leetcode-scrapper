import pytest
from q_2449_minimumNumberOfOperationsToMakeArraysSimilar import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([8, 12, 6], [2, 14, 10], 2),
        ([1, 2, 5], [4, 1, 3], 1),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 0),
    ],
)
class TestSolution:
    def test_makeSimilar(self, nums: List[int], target: List[int], output: int):
        sc = Solution()
        assert (
            sc.makeSimilar(
                nums,
                target,
            )
            == output
        )
