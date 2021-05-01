#https://leetcode-cn.com/problems/employee-importance/
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for i in range(0, len(employees)):
            if employees[i].id == id:
                imp = employees[i].importance;
                for j in range(0, len(employees[i].subordinates)):
                    imp = imp + self.getImportance(employees, employees[i].subordinates[j]);
                return imp;