import sys
import numpy as np

class Full_name_student:
  def __init__ (self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
  
  def full_name (self):
    full_name_detail = f"The student name is {self.first_name} {self.last_name}."
    return full_name_detail

  



best_student = Full_name_student("Behzad", "Farshchiyan")
best_student.first_name = "Farzad"

print(best_student.full_name())