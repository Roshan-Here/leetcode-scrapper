import pytest
from q_3147_takingMaximumEnergyFromTheMysticDungeon import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_maximumEnergy(self, energy: List[int], k: int, output: int):
        sc = Solution()
        assert sc.maximumEnergy() == output
