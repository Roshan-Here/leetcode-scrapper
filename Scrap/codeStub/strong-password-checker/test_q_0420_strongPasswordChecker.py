import pytest
from q_0420_strongPasswordChecker import Solution


@pytest.mark.parametrize("password, output", [("a", 5), ("aA1", 3), ("1337C0d3", 0)])
class TestSolution:
    def test_strongPasswordChecker(self, password: str, output: int):
        sc = Solution()
        assert (
            sc.strongPasswordChecker(
                password,
            )
            == output
        )
