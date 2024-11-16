# utils.py
import math

def calculate_distance(x1, y1, x2, y2):
    """두 점 사이의 거리를 계산하는 함수"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
