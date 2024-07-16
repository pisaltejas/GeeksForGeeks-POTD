class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def boundaryPoints(self, x1, y1, x2, y2):
        return self.gcd(abs(x2 - x1), abs(y2 - y1)) + 1

    def InternalCount(self, p, q, r):
        area = abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]))

        B = self.boundaryPoints(p[0], p[1], q[0], q[1]) + \
            self.boundaryPoints(q[0], q[1], r[0], r[1]) + \
            self.boundaryPoints(r[0], r[1], p[0], p[1]) - 3

        I = (area - B + 2) // 2

        return I
