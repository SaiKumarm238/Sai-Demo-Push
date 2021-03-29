for i in range(1000):
    print("I am working in Ojas")



class Employee(models.Model):
   name = models.CharField(max_length=100)
   adress = models.TextField()
   email= models.EmailField(max_length=100)

