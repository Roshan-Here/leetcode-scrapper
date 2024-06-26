import pytest
from q_1333_filterRestaurantsByVeganFriendlyPriceAndDistance import Solution


@pytest.mark.parametrize(
    "restaurants, veganFriendly, maxPrice, maxDistance, output",
    [
        (
            [
                [1, 4, 1, 40, 10],
                [2, 8, 0, 50, 5],
                [3, 8, 1, 30, 4],
                [4, 10, 0, 10, 3],
                [5, 1, 1, 15, 1],
            ],
            1,
            50,
            10,
            [3, 1, 5],
        ),
        (
            [
                [1, 4, 1, 40, 10],
                [2, 8, 0, 50, 5],
                [3, 8, 1, 30, 4],
                [4, 10, 0, 10, 3],
                [5, 1, 1, 15, 1],
            ],
            0,
            50,
            10,
            [4, 3, 2, 1, 5],
        ),
        (
            [
                [1, 4, 1, 40, 10],
                [2, 8, 0, 50, 5],
                [3, 8, 1, 30, 4],
                [4, 10, 0, 10, 3],
                [5, 1, 1, 15, 1],
            ],
            0,
            30,
            3,
            [4, 5],
        ),
    ],
)
class TestSolution:
    def test_filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.filterRestaurants(
                restaurants,
                veganFriendly,
                maxPrice,
                maxDistance,
            )
            == output
        )
