from geo import utils

def test_calculate_distance():
    assert utils.calculate_distance(0, 0, 3, 4) == 5, "거리 계산 오류"
    assert utils.calculate_distance(1, 1, 4, 5) == 5, "거리 계산 오류"

if __name__ == "__main__":
    test_calculate_distance()
    print("모든 테스트가 통과되었습니다!")
