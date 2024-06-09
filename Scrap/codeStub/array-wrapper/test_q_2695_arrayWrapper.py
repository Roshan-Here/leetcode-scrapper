import pytest
from q_2695_arrayWrapper import Solution


@pytest.mark.parametrize(
    "nums, operation, output",
    [
        ([[1, 2], [3, 4]], "Add", 10),
        ([[23, 98, 42, 70]], "String", "[23,98,42,70]"),
        ([[], []], "Add", 0),
    ],
)
class TestSolution:
    def test_arrayWrapper(self, output: Any):
        sc = Solution()
        assert (
            sc.arrayWrapper(
                nums,
                operation,
            )
            == output
        )
