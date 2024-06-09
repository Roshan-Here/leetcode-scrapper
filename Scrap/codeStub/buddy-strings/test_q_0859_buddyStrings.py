import pytest
from q_0859_buddyStrings import Solution


@pytest.mark.parametrize(
    "s, goal, output", [("ab", "ba", True), ("ab", "ab", False), ("aa", "aa", True)]
)
class TestSolution:
    def test_buddyStrings(self, s: str, goal: str, output: bool):
        sc = Solution()
        assert (
            sc.buddyStrings(
                s,
                goal,
            )
            == output
        )
