# First Plot With Matplotlib slide 14.py
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.show()

#### slide 17.py
# import matplotlib.pyplot as plt
# x =range(5)
# plt.plot(x, [x1**2 for x1 in x])
# plt.show()

#### slide 18.py
# import numpy, matplotlib.pyplot as plt
# x = numpy.arange(0, 5, 0.01)
# plt.plot(x, [x1**2 for x1 in x])
# plt.show()

#### slide 20.py
# import matplotlib.pyplot as plt
# x =range(5)
# plt.plot(x, [x1 for x1 in x])
# plt.plot(x, [x1*x1 for x1 in x])
# plt.plot(x, [x1*x1*x1 for x1 in x])
# plt.show()

#### slide 21.py
# import matplotlib.pyplot as plt
# x =range(5)
# plt.plot(x, [x1 for x1 in x], x,
#          [x1*x1 for x1 in x], x, [x1*x1*x1 for x1 in x])
# plt.show()

##### slide 53.py
# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.arange(1, 3, 0.2)
# plt.plot(y, '*', y+0.5, 'o', y+1, 'D', y+2, '^', y+3, 's')
# plt.show()

##### slide 49.py
# import matplotlib.pyplot as plt
# import numpy as np
# y = np.arange(1, 3)
# plt.plot(y, 'y')
# plt.plot(y+5, 'm')
# plt.plot(y+10, 'c')
# plt.show()
##### slide 51.py
# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.arange(1, 100)
# plt.plot(y, '--', y*5, '-.', y*10, ':')
# plt.show()
