# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner.

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if C<=E or G<=A or B>=H or F>=D:
            return (C-A)*(D-B)+(G-E)*(H-F) # total area
        l = sorted([A, C, E, G])
        h = sorted([B, D, F, H])
        return (C-A)*(D-B)+(G-E)*(H-F)-(l[2]-l[1])*(h[2]-h[1])

print(Solution().computeArea(0, 0, 0, 0, -1, -1, 1, 1))
