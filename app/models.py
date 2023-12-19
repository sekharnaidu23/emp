from django.db import models

# Create your models here.
class Emp(models.Model):
    Eid=models.CharField(max_length=100,primary_key=True)
    Ename=models.CharField(max_length=100,unique=True)
    Esal=models.IntegerField()

    def __str__(self):
         return self.Eid


class Dept(models.Model):
     Eid=models.ForeignKey(Emp,on_delete=models.CASCADE)
     Dname=models.CharField(max_length=100)
     Dno=models.IntegerField()
     Dloc=models.CharField(max_length=100)

     def __str__(self):
          return self.Dname
 
class Salgrade(models.Model):
     Eid=models.ForeignKey(Emp,on_delete=models.CASCADE)
     Salary=models.IntegerField()
     Bonus=models.IntegerField()
     def __str__(self):
          return self.Salary
