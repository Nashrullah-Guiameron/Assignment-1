# number 1. x^2 - 10
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**2 - 10
x = np.linspace(-5, 5, 50)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("1. Graph of x^2 - 10")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 2. x^2 + x - 100
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**3 + x - 100
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2. Graph of x^3 + x - 10")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 3. x^10 - x^8 + x^2 - 8
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**10 - x**8 + x**2 - 8
x = np.linspace(-5, 5, 50)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("3. Graph of x^10 - x^8 +x^2 - 8")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 4. x^4 + x^3 + x^2 + x + 1
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**4 + x**3 + x**2 + x +1 
x = np.linspace(-5, 5, 50)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("4. Graph of x^4 + x^3 + x^2 + x + 1")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 5. (x^2 + x + 10)/(2x)
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return (x**2 + x + 10)/(2*x)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("5. Graph of (x^2 + x + 10)/(2x)")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 6. (sin(x))/(3x)
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return np.sin(x)/(3*x)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("6. Graph of (sin(x))/(3x)")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 7. x^3 + 2x^2 - 10x + 3
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**3 + (2*x**2) - (10*x) +3
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("7. Graph of x^3+2x^2-10x+3")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 8. (cos(x))/(5x)
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return np.cos(x)/(5*x)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("8. Graph of (cos(x))/(5x)")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 9. (x^3)/(2x) - 10x
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return ((x**3)/(2*x))-(10*x)
x = np.linspace(-5, 5, 50)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("9. Graph of (x^3)/(2x) - 10x")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()

# number 10. f(x) = (x + 2)(x + 3)(x - 4)
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return (x+2)*(x+3)*(x-4)
x = np.linspace(-5, 5, 50)  
y = f(x)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("10. Graph of f(x)=(x+2)(x+3)(x-4)")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.show()