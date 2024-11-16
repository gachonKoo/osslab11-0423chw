# tester.py
from geo import utils

def test_geo_functions():
    """geo 패키지의 함수들을 테스트하는 함수"""
    distance = utils.calculate_distance(0, 0, 3, 4)
    assert distance == 5, f"Expected 5, but got {distance}"
    print("테스트 통과")

if __name__ == "__main__":
    test_geo_functions()
    print("모든 테스트가 통과되었습니다!")
