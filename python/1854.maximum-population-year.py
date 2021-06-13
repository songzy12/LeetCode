# https://leetcode.com/contest/weekly-contest-240/problems/maximum-population-year/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_count = {}
        for birth, death in logs:
            for year in range(birth, death):
                if year in year_count:
                    year_count[year] += 1
                else:
                    year_count[year] = 1

        max_count = -1
        max_year = -1
        for year in range(1950, 2050):
            if year in year_count and year_count[year] > max_count:
                max_year = year
                max_count = year_count[year]
        return max_year
