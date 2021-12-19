import torch
import numpy as np
from torch.autograd import Variable

# Variable(变量)
# Create Variable
x = Variable(torch.FloatTensor([1.0]), requires_grad=True)
w = Variable(torch.FloatTensor([2.0]), requires_grad=True)
b = Variable(torch.FloatTensor([3.0]), requires_grad=True)

# Build a computational graph.
y = w * x + b

print('y is: {}'.format(y))
y.backward(torch.FloatTensor([0.1]))

print(w.grad) #dy/dw = x
print(x.grad) #dy/dx = w
print(b.grad) #dy/db = 1

x = torch.randn(3)
x = Variable(x, requires_grad=True)

y = x * 2 #dy = 2
print(y)
y.backward(torch.FloatTensor([1, 0.1, 0.01]))
print(x.grad)
