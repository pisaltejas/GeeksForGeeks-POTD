class Solution:
    def onSegment(self, p, q, r):
        if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
            return True
        return False

    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  
        elif val > 0:
            return 1 
        else:
            return 2  

    def doIntersect(self, p1, q1, p2, q2):
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return "true"

        if o1 == 0 and self.onSegment(p1, p2, q1):
            return "true"
        if o2 == 0 and self.onSegment(p1, q2, q1):
            return "true"
        if o3 == 0 and self.onSegment(p2, p1, q2):
            return "true"
        if o4 == 0 and self.onSegment(p2, q1, q2):
            return "true"

        return "false"
