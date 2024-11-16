from geo import utils

def test_geo_functions():
    distance = utils.calculate_distance(0, 0, 3, 4)
    assert distance == 5, f"Expected distance 5, but got {distance}"

    area = utils.calculate_area(3, 4)
    assert area == 12, f"Expected area 12, but got {area}"

if __name__ == "__main__":
    test_geo_functions()
    print("All tests passed!")
