# Actiation Function
입력 신호의 총합을 출력 신호로 변환하는 함수  
입력 신호의 총합이 활성화를 일으키는지 정하는 역할  
-> data를 비선형으로 바꾸기 위해서 사용한다  

출력층의 활성화 함수는 풀고자 하는 문제의 성질에 맞게 정한다   
regression에서는 identity function,  
2class classification에서는 sigmoid function,  
multi classification에서는 softmax function 사용하는 것이 일반적  

## 1. sigmoid function
h(x) = 1 / (1+exp(-x))

## 2. ReLU function
입력이 0을 넘으면 입력 그대로 출력되고, 넘지 않으면 0을 출력하는 함수  
h(x) = x(x>0), 0(x<=0)

## 3. softmax function
출력값이 0과 1.0 사이의 실수, 총합이 1  
따라서 출력을 **확률**로 해석할 수 있다
