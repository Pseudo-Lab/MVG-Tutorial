# **2.1. The 2D projective plane**

점을 평면에서 표현할 때 보통 실수평면($\mathbb{R}^2$)에서 ($x,y$)이고 벡터공간에서 ($x,y$)는 벡터입니다. 

이 section에서는 homogenous의 관점에서 본 점, 선, 면을 어떻게 표현하는지 알아보겠습니다.

### **Row and column vectors**
>볼드체 $\mathbf{x} = (x,y)^T$ 는 항상 column vector 를 나타내고 row vector는 $\mathbf{x}^T=(x,y)$ 로 표현합니다.

## **2.1.1 Points and lines**

### **Homogeneous representation of lines**

>평면에서의 직선의 방정식은 $ax+by+c=0$ 나타냅니다. 여기서 $a,b,c$ 값을 통해 각각의 다른 직선을 그릴 수 있고 벡터로 표현하면 $(a,b,c)^T$ 로 표현할 수 있습니다.

하지만 앞서본 직선의 방정식과 벡터 간의 대응은 일대일이 아닙니다. $(ka)x+(kb)y+(kc)=0$ ($k\neq0$ 인 실수) 와 $ax+by+c=0$ 은 같은 직선 이기 때문입니다.

그러므로 벡터 $(a,b,c)^T$ 와 $k(a,b,c)^T$같은 직선을 나타내는 벡터입니다. 이러한 equivalence한 관계를 갖는 것을 homogeneous vector라고 합니다.

### **Homogeneous representation of points**

>직선 $\mathbf{l}=(a,b,c)^T$ 위에 존재하는 한 점을 $(x,y)^T$라 하면, 이 $(x,y)^T$는 $ax+by+c=0$ 을 만족시키는 점들의 집합이며 이 식을 벡터 간의 내적의 식으로 바꿔주면 $(x,y,1)(a,b,c)^T$ = $(x,y,1)\mathbf{l}= 0$ 으로 바꿀 수 있습니다.<br>

결과적으로 직선 위에 존재하는 한 점 $(x,y)^T$ 에서 마지막 항에 1을 추가한 것과 같으며, 점의 homogeneous 표현은 이렇게 뒤에 1을 하나 덧붙이는 방법으로 할 수 있습니다.

또한, 전 section에서 말한 것 처럼 $(kx,ky,k)^T$ 과  $(x,y,1)^T$ 이 같다는 것을 알 수 있으며 임의의 homogeneous vector $(x_1,x_2,x_3)$ 가 존재한다면 이는 실수평면 $\mathbb{R}^2$에서 $(x_1/x_3,x_2/x_3)^T$ 과 같습니다.


### **Relation between points and lines**
> 직선 $\text{l}$ 위에 있는 점 $\text{x}$ 가 성립할 필요충분조건은 $\text{x}^T\text{l}$=0 입니다. <br>
따라서 $\text{x}^T\text{l} = \text{l}^T\text{x} = \text{l}\cdot\text{x}$ 또한 성립합니다. <br>
즉, $\text{x}^T\text{l}$가 0이면 점 $\text{x}$는 직선 $\text{l}$ 위에 있다는 것을 의미합니다.<br>


### **Degrees of freedom (dof)**
>한 점을 결정하려면 두 가지의 요소 x와 y가 필요한데, 이 때 한 점의 dof는 2라고 얘기합니다. 한 직선은 두 개의 파라미터로 주어질 수 있으므로 dof가 2 입니다.

inhomogeneous로 본다면 gradient와 y로 직선을 결정지을 수 있습니다.

### **Intersection of lines**

>두 직선 $\text{l}=(a,b,c)^T$, $\text{l}'=(a',b',c')^T$ 주어졌을 때 교차점은 $\text{x}=\text{l} \ \times \ \text{l}'$ 로 구할 수 있습니다. 

위 식이 맞다는 것은 이 수식을 활용한 triple scalar product을 활용해서 볼 수 있는데, 
$\text{l}\cdot(\text{l} \ \times \ \text{l}')=\text{l}'\cdot(\text{l} \ \times \ \text{l}')=0$ 두 직선식을 만족시키기 때문에 $\text{x}$ 가 교차점이란 것을 알 수 있습니다.

### **Line joining points**
> 두 점을 지나는 직선은 $\text{l}=\text{x} \ \times \ \text{x}'$ 로 구할 수 있습니다. 

<br>

## **2.1.2 Ideal points and the line at infinity**

>평행한 두 직선 $ax+by+c=0$ 와 $ax+by+c'=0$ 가 있다고 하면 벡터로 표현했을 때는 $\text{l}=(a,b,c)^T$ $\text{l}'=(a,b,c')^T$ 로 쓸 수 있습니다.

위 두 직선의 교점을 구해보면 $\text{l}\ \times \ \text{l}' = (c'-c)(b,-a,0)^T$ 이 되는데 앞의 scale $(c-c')$ 를 제외하고 본다면 $(b,-a,0)^T$ 은 마지막 항이 0인 것이 보일 겁니다.

나머지 두 원소를 마지막 항으로 나누고 inhomogeneous 표현으로 본다면 $(b/0,-a/0)^T$ 이 되고 이는 특정한 점이 아닌 무한한 점(point at infinity)이 됩니다.

그렇기 때문에 평행한 두 직선은 무한한 점(point at infinity)에서 만난다고 하는 것입니다.

### **Ideal points and the line at infinity**

homogeneous vector $\text{x}=(x_1,x_2,x_3)$ 에서 $x_3=0$ 인 경우를 ideal point라고 했습니다. 벡터 형태로 ideal point를 써보면 $(x_1,x_2,0)$이 될 것입니다. 

>모든 ideal point의 집합은 $x_1:x_2$ 의 비율을 가진 점들의 모임일 것이고, 이들은 특정한 직선 위에 있는 점들 일 것입니다. 우리는 이것을 line at infinity라고 말하고 $\text{l}_∞ = (0,0,1)^T$ 로 표현합니다.

다음과 같은 직선의 방정식을 만족함으로써 점 $(x_1,x_2,0)$은 직선 $\text{l}_∞$ 위에 있음을 알 수 있습니다.
$(x_1,x_2,0)\text{l}_\infty=(x_1,x_2,0)(0,0,1)^T=0$

### **Duality**
>2D projective geometry에서 어떤 정리가 있을 때 점과 직선의 역할을 바꾸어도 같은 성질을 duality라고 합니다.<br>
예를 들어, 직선의 방정식 $\text{x}^T\text{l} = \text{l}^T\text{x} = 0$ 이 성립합니다.



### **Reference**
1. Multiple view geometry in computer vision chapter 2.2