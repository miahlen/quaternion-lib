# quaternion-lib

Library in Python for performing quaternion algebra



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

To run this library you need Python and numpy. You can install the necessary packages by running

```
pip install -r requirements.txt
```



### Installing


Navigate to the desired location of the repository on your local computer, e.g. ~/Documents

```
cd ~/Documents
```

Clone the repository

```
git clone https://github.com/miahlen/quaternion-lib.git
```

Navigate to the newly created directory

```
cd quaternion-lib
```


Finally test the library by creating your own instance q of the Quaternion class representing a rotation of +90 degrees around the z axis.
Use q to rotate an instance of the Position class v (1, 0, 0) accordingly. 

```python
from quaternion import Quaternion
from position import Position
import quaternion_algebra
import numpy as np

# Create quaternion q
theta = 90 * np.pi / 180
q = Quaternion(np.cos(theta / 2.0), 0, 0, np.sin(theta / 2.0))

# Create vector v
v = Position(1, 0, 0)

# Rotate vector using quaternion
v_rotated = quaternion_algebra.rotate_vector_by_quaternion(v, q)

print("Expected v_rotated: (0.0, 1.0, 0.0), your v_rotated: "+str(v_rotated))
```




## Running the tests

There are 4 tests in this repository: 
 - test_position.py
 - test_euler_angle.py
 - test_quaternion.py 
 - test_quaternion_algebra.py

which can be run with the following commands:

```
python test_position.py
python test_euler_angle.py
python test_quaternion.py
python test_quaternion_algebra.py
```

The test_position.py module will test the methods in module position.py, and so forth.
