import pytest
from q_1095_findInMountainArray import Solution


@pytest.mark.parametrize(
    "array, target, output",
    [([1, 2, 3, 4, 5, 3, 1], 3, 2), ([0, 1, 2, 4, 2, 1], 3, -1)],
)
class TestSolution:
    def test_findInMountainArray(
        self, target: int, mountain_arr: "MountainArray", output: int
    ):
        sc = Solution()
        assert (
            sc.findInMountainArray(
                array,
                target,
            )
            == output
        )
