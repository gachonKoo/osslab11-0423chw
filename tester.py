from geo import utils

def test_geo_functions():
    # 여기에 geo 패키지의 함수들을 테스트하는 코드를 작성합니다
    # 예: utils.py에 calculate_distance 함수가 있다고 가정
    result = utils.calculate_distance(0, 0, 3, 4)
    assert result == 5, f"Expected 5, but got {result}"

    # 더 많은 테스트 케이스를 추가할 수 있습니다

if __name__ == "__main__":
    test_geo_functions()
    print("모든 테스트가 통과되었습니다!")
