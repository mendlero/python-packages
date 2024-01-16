from src import Quaternion

q1 = Quaternion(1, 1, 1, 1)
q2 = Quaternion.from_complex(3+4j)

assert q1 == q1
assert q1 != q2

assert q2 == Quaternion(3, 4)
assert Quaternion.form_tuple((1, 1, 1, 1)) == q1
assert Quaternion.from_float(1) == Quaternion(1)

assert (q1+q2) == Quaternion(4, 5, 1, 1)
assert (q2-q1) == Quaternion(2, 3, -1, -1)
assert (q1*q2) == Quaternion(-1, 7, 1, -7)
assert (q1/q2) == Quaternion(0.04, -0.28, -0.04, 0.28)

assert abs(q1) == 5
