import pytest
from q_0434_numberOfSegmentsInAString import Solution


@pytest.mark.parametrize("s, output", [("Hello, my name is John", 5), ("Hello", 1)])
class TestSolution:
    def test_countSegments(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countSegments(
                s,
            )
            == output
        )
