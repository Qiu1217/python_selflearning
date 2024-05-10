#BMI指数=身高/体重的平方
h = input('请输入您的身高(单位:米):')
w = input('请输入您的体重(单位:千克):')
h = float(h)
w = float(w)

BMI = w / (h**2)

print('你的BMI指数为%.2f' % BMI)

