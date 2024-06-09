import pytest
from q_1041_robotBoundedInCircle import Solution


@pytest.mark.parametrize(
    "instructions, output", [("GGLLGG", True), ("GG", False), ("GL", True)]
)
class TestSolution:
    def test_isRobotBounded(self, instructions: str, output: bool):
        sc = Solution()
        assert (
            sc.isRobotBounded(
                instructions,
            )
            == output
        )
