class Solution(object):
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        print targets
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            # every visit will be recorded
            # the second visit differs from the first
            route.append(airport) 
        visit('JFK')
        return route[::-1]
