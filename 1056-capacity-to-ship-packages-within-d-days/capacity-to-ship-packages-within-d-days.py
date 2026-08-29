class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canfinish(weights, days, caps):
            load = 0
            reqdays = 1

            for weight in weights:
                if load + weight <= caps:
                    load += weight
                else:
                    reqdays += 1
                    load = weight

            return reqdays <= days

        l = max(weights)
        h = sum(weights)

        while l < h:
            mid = (l + h) // 2

            if canfinish(weights, days, mid):
                h = mid
            else:
                l = mid + 1

        return l