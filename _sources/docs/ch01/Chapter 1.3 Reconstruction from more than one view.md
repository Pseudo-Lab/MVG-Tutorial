## **1.3 Reconstruction from more than one view**

이 책의 주요한 주제 중 하나입니다. 가장 간단한 두 개의 이미지의 경우를 먼저 고려해봅니다.

두 개의 시점의 경우, $x_i \leftrightarrow x_i'$의 관계를 가지는 두 이미지가 있다고 합시다. 이 둘은 각각 3D points $\mathbf{X}_i$로의 변환을 위한 camera matrix $\mathbf{P}$와 $\mathbf{P'}$를 갖습니다. 따라서 $PX_i=x_i$이며, $\mathbf{P'}\mathbf{X}_i=x_i'$입니다. 하지만 우리는 각 이미지 좌표 매칭 쌍 외에 우리는 $\mathbf{P, P', X_i}$ 모두 모르는 상태입니다. 이 뒤의 챕터에서 이러한 것들을 결정하는 방법에 대해 다룹니다. 여기서는 간단하게만 이야기 하겠습니다.

3차원 점의 위치를 특정하는 것은 불가능합니다. 아무리 매칭 쌍이 많이 주어졌다고 해도 3차원 좌표를 모르는 건 마찬가지입니다. 여기서 카메라가 보정되어 있지 않은 경우, 이 문제는 사영 변환으로 표현할 수 있습니다.

좌표의 특정이 불가능한 이유는 사영된 이미지 좌표를 변경하지 않고 각 3D 좌표 $\mathbf{X}_i$와 각 camera matrix에 사영 변환을 적용할 수 있기 때문입니다. 적용된 수식은 아래와 같습니다.

$$
\mathbf{P}_j\mathbf{X}_i = (\mathbf{P}_j\mathbf{H}^{-1})(\mathbf{H}\mathbf{X}_i)
$$

여기서 j는 이미지의 번호이며, 사실상 어떤 이미지를 선택해도 동일합니다. 또한, 여기서 $H$는 4x4의 사영 변환 행렬이며 임의의 값으로 정해집니다. 우리는 이러한 복원을 projective ambiguity 또는 projective reconstruction 이라고 말합니다. 하지만 이것은 최악의 경우이고, 최소 7개의 좌표 매칭 쌍이 존재한다면 여기서도 충분히 3D 복원이 가능합니다.

두 시점에서 3D 점들을 복원하는 가장 기본적인 방법은 fundamental matrix 입니다. 이것은 이미지 좌표 $x_i$와 $x_i'$가 있을 때, 이들이 같은 3D 좌표에 매핑된다는 제약 조건을 갖게 해줍니다. fundamental matrix $\mathbf{F}$가 주어졌을 때, 매칭 좌표 쌍 $x_i, x_i'$는  $x_i'\mathbf{F}x_i=0$ 이라는 수식을 만족하며, $\mathbf{F}$는 rank 2의 3x3 행렬입니다. $\mathbf{F}$가 알려지지 않은 경우, 일련의 대응점들을 활용해 계산해낼 수 있습니다.

한 쌍의 camera matrix $\mathbf{P, P'}$는 $\mathbf{F}$를 유일하게 결정할 수 있고, 반대로 $\mathbf{F}$는 한 쌍의 camera matrix를 결정할 수 있습니다. 따라서, fundamental matrix는 두 시점의 사영 기하를 캡슐화하며 3D의 사영 변환에 의해 바뀌지 않습니다.

복원하는 과정을 간단하게 정리하면 다음과 같습니다.

>1. 두 개의 뷰에서 여러 개의 좌표 매칭 쌍$(x_i, x_i')$들이 주어지면, 공면(coplanarity) 방정식 $x_i'Fx_i=0$를 기반으로하는 F의 원소들에 대한 선형 방정식들을 구성합니다.
>2. 구성된 연립 선형 방정식들의 해로 $F$를 찾습니다.
>3. 이후 챕터에(section 9.5) 등장하는 공식에 따라 $F$를 통해 한 쌍의 camera matrix를 계산합니다.
>4. 계산된 camera matrix $P,$ $P'$를 이용해 이미지 좌표 매칭쌍들을 사영해 $X_i$를 찾습니다. 이후 삼각측량(triangulation)을 활용해 3D 공간 좌표를 결정합니다.

이에 대한 자세한 부분은 이후 챕터에서 다룹니다.

지금까지 2 View geometry 까지의 내용을 개요 형태로 훑어보았습니다. 이후 챕터 2에서부터는 위에서 간단히 설명한 내용들을 자세하게 살펴보고 갑니다.

### **Reference**
1. Multiple view geometry in computer vision chapter 1.3