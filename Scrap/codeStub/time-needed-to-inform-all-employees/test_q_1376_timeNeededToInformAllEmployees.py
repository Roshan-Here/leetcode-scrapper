import pytest
from q_1376_timeNeededToInformAllEmployees import Solution


@pytest.mark.parametrize(
    "n, headID, manager, informTime, output",
    [(1, 0, [-1], [0], 0), (6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0], 1)],
)
class TestSolution:
    def test_numOfMinutes(
        self,
        n: int,
        headID: int,
        manager: List[int],
        informTime: List[int],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.numOfMinutes(
                n,
                headID,
                manager,
                informTime,
            )
            == output
        )
