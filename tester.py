from geo import utils

def test_geo_functions():
    """geo 패키지의 함수들을 테스트하는 함수"""
    distance = utils.calculate_distance(0, 0, 3, 4)
    assert distance == 5, f"Expected 5, but got {distance}"
    
    # 예시로 면적 계산을 추가합니다.
    area = utils.calculate_area(10)  # 예를 들어, 반지름이 10인 원의 면적을 계산
    assert area == 314.1592653589793, f"Expected area to be 314.1592653589793, but got {area}"

    print(f"c = {distance}")
    print(f"area = {area}")

if __name__ == "__main__":
    test_geo_functions()
    print("모든 테스트가 통과되었습니다!")
