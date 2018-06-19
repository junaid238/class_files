from sklearn.datasets import load_digits
import numpy as np 
import matplotlib.pyplot as plt
digits = load_digits()

print("Data SHape" ,digits.data.shape)
print("Label Data Shape", digits.target.shape)
# plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
 plt.subplot(1, 5 ,index + 1 )
 plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
 plt.title('Training: %i\n' % label, fontsize = 10)
plt.show()


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)
# print(x_train.data.shape)
# print(y_train.data.shape)
# print(x_test.data.shape)
# print(y_test.data.shape)
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
for i in range(0,10):
    plt.subplot(1, 10, i + 1 )
    ans =log_reg.predict(x_test[i].reshape(1,-1))
    plt.imshow(np.reshape(x_test[i], (8,8)), cmap=plt.cm.gray)
    plt.title('Ans: %i\n' % ans, fontsize = 10)
plt.show()    

log_reg.predict(x_test[0:10])
predictions = log_reg.predict(x_test)
# print(len(x_test))
predictions
score = log_reg.score(x_test, y_test)
print(score*100)

