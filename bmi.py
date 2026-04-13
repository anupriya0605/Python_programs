class person:
   def __init__(self,name,age,weight,height):
      self.name=name
      self.age=age
      self.weight=weight
      self.height=height
      print "Person class created"
   def get_bmi_result(self):
      h=self.height*0.3048
      bmi=(self.weight/(h**2))
      if(bmi < 18.5):
         print "Underweight"
      elif(18.5<= bmi <25):
         print "Healthy"
      else:
         print "Obese"
p1=person('Anu',20,41,4.8)
p1.get_bmi_result()
