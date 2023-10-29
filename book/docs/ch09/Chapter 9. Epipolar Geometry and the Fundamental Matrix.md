# **Chapter 9. Epipolar Geometry and the Fundamental Matrix**

9장에서는 Epipolar Geometry와 Fundamental matrix에 대해서 학습합니다.


Epipolar Geometry는 두 이미지 사이의 기하학을 의미하는 것으로, 두 이미지 사이에 존재하는 관계를 표현하는 기하학이라고 할 수 있습니다. Fundamental Matrix는 이 Epipolar Geometry를 대수적으로 표현한 것입니다.

본 챕터에서는 이 Epipolar Geometry와 Fundamental Matrix를 소개하고 그 개념에 대해 알아보는 것이 주된 목표입니다. Fundamental Matrix를 계산하는 방법은 이후 Chapter 11에서 다뤄봅니다.


## **학습 목표**
---
### **9.1 Epipolar Geometry**
이번 섹션에서는 Epipolar Geometry의 개념과 용어에 대해 학습합니다.

### **9.2 Fundamental Matrix and Essential Matrix**
위에서 학습한 Epipolar Geometry를 어떻게 수식으로 나타내는지 알아보고, Fundamental matrix와 Essential Matrix의 차이를 알아봅니다.

### **9.3 Camera Motion에 따른 좌표 변환**
camera motion을 어떻게 정의하는지 알아보고 이 motion의 변화에 따라 어떤 과정을 거쳐서 변환되는지 학습하겠습니다.

### **9.4 Camera Matrix의 모호성**
Epipolar Geometry에서 projection matrix와 fundamental matrix 사이에 어떤 대응 관계가 있는지 알아봅니다.

<br>

### **Reference**
---
1. [Multiple View Geometry in Computer Vision](https://www.amazon.com/Multiple-View-Geometry-Computer-Vision/dp/0521540518)