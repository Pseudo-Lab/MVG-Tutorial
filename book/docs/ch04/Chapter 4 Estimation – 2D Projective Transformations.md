# **Chapter 4 - Estimation – 2D Projective Transformations(작성 중)**

4장에서는 여러 가지 행렬의 estimation 문제에 대해 알아봅니다.<br>
여기서 추정하고자 하는 행렬은 4가지로 분류할 수 있습니다.

**1. 2D Homography**<br>
2. 3D to 2D camera projection(6장)<br>
3. Fundamental matrix computation(9장)<br>
4. Trifocal tensor computation(15장)<br>

여기서는 1번 2D homography에 대해서만 이야기합니다.<br>
2D homography는 2D 좌표 to 2D 좌표 변환 행렬 H를 말하며, 서로가 같은 점인 $x_i$와 $x_i'$에 대해 $\text{H}x_i=x_i'$가 성립합니다.<br>

Sub-section은 크게 2가지로 이뤄지며 각각 아래와 같습니다.
1. The Direct Linear Transformation (DLT) algorithm
2. Different cost functions
3. Statistical cost functions and Maximum Likelihood estimation
4. Transformation invariance and normalization
5. Iterative minimization methods

<br>

## **학습 목표**
---
### **4.1 The Direct Linear Transformation (DLT) algorithm**
먼저 4개의 2D 좌표 대응이 주어지면 H를 결정할 수 있는 선형 알고리즘 The Direct Linear Transformation(DLT) 알고리즘에 대해 알아봅니다.

### **4.2 Different cost functions**
이제 2개 섹션동안 조건이 여러 가지인 경우 H를 최대한 잘 결정하기 위해 사용하는 cost function에 대해 알아봅니다.<br>
여기서는 기하학적 cost function에 대해 학습합니다.

### **4.3 Statistical cost functions and Maximum Likelihood estimation**
이번 섹션에서는 통계학적 cost function에 대해 학습합니다.

### **4.4 Transformation invariance and normalization**
DLT 알고리즘의 특성과, 성능, 기하학적 오류를 최소화하는 알고리즘과 그들을 비교하는 방법을 학습합니다.

### **4.5 Iterative minimization methods**
Cost function들을 최소화 하기 위해 사용되는 반복적인 방법들에 대해 학습하며, DLT 알고리즘과 같은 선형 알고리즘들에 비교해봅니다.

<br>

### **Reference**
---
1. [Multiple View Geometry in Computer Vision](https://www.amazon.com/Multiple-View-Geometry-Computer-Vision/dp/0521540518)