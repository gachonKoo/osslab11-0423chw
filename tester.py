# 1. 저장소 클론
git clone https://github.com/your-classroom-repo-url.git
cd your-repo-name

# 2. 파일 구조 생성
mkdir geo
touch geo/__init__.py
touch geo/utils.py
touch tester.py

# 3. geo/utils.py 파일 작성
cat > geo/utils.py << EOL
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
EOL

# 4. tester.py 파일 작성
cat > tester.py << EOL
from geo import utils

def test_calculate_distance():
    assert utils.calculate_distance(0, 0, 3, 4) == 5, "테스트 실패: 거리 계산 오류"
    assert utils.calculate_distance(1, 1, 4, 5) == 5, "테스트 실패: 거리 계산 오류"

if __name__ == "__main__":
    test_calculate_distance()
    print("모든 테스트가 통과되었습니다!")
EOL

# 5. 변경사항 커밋 및 푸시
git add .
git commit -m "Implement geo package and test code"
git push origin main

# 6. 테스트 실행 (선택사항)
python tester.py

# 7. GitHub Actions에서 자동 채점 결과 확인
echo "GitHub 저장소의 Actions 탭에서 자동 채점 결과를 확인하세요."
