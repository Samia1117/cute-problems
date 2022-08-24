class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # distDict = {}
        distList = []
        for point in points:
            distFromOrigin = self.distanceFromOrigin(point)
            # distDict[(point[0], point[1])] = distFromOrigin
            distList.append((distFromOrigin, point))

        # sortedPoints = sorted(distDict.items(), key=lambda x: x[1])
        sortedPoints = sorted(distList, key=lambda x: x[0])
        
        return [tup[1] for tup in sortedPoints[0:k]]
    
    
    def distanceFromOrigin(self, coords):
        return sqrt((coords[0]*coords[0]) + (coords[1]*coords[1]))
