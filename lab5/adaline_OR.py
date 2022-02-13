import numpy as np
#combination of 2 bit bipolar OR gate
combination = np.array(
  [
    [-1,-1],
    [-1,1],
    [1,-1],
    [1,1]
  ]
)

#output(label)
labels = np.array([-1,1,1,1])

print(combination, labels)
print("\n")
weight = [0.2, 0.3]
bias = 0.1
learningRate = 0.1 #alpha
epoch = 4

for i in range(epoch):
  print("epoch:", i+1)

  for j in range(combination.shape[0]):
      output = labels[j] #output to be obtained

      x1 = combination[j][0]
      x2 = combination[j][1]

      #netinput
      y_in = (x1*weight[0]) + (x2*weight[1]) + bias

      #error
      error = output - y_in

      #update
      bias = bias + learningRate * error
      weight[0] = weight[0] + learningRate * error * x1
      weight[1] = weight[1] + learningRate * error * x2

      print("error=",error)
      print("y_in= ",y_in)
      print("bias= ",bias)
      print("weight1= ", weight[0])
      print("weight2= ",weight[1])
      print("\n")


    



