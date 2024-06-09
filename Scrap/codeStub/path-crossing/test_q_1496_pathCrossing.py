import pytest
from q_1496_pathCrossing import Solution


@pytest.mark.parametrize("path, output", [("NES", False), ("NESWW", True)])
class TestSolution:
    def test_isPathCrossing(self, path: str, output: bool):
        sc = Solution()
        assert (
            sc.isPathCrossing(
                path,
            )
            == output
        )
