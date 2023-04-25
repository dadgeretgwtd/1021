import randomclass Human:
  def __init__(self,name="Human", job=None, home=None, car=None):
          self.name=name
          self.money=100
          self.gladness=50
          self.satiety=50
          self.job=job
          self.home=homes
  else.car=car
   def get_home(self):
        self.home=House
  def get_job(self):
    if self.car.drive():
        pass
    else:
        self.to_repair()
        return
        self.job=Job(job_list)
  def get_car(self):
        self.car=Auto(brand_of_car)
        def eat(self):
            if self.home.food<0:
        self.shopping("food")
     else:
    if  self.satiety>=100:
        self.satiety=100
        return
        self.satiety+=5
        self.satiety-=5
        def work(self):
            if self.car.drive():
                pass
     else:
            if self.car.fuel<20:
       self.shopping("fuel")
        return
        self.money+=self.job.salary
        self.gladness-=self.job.gladnes_less
        self.satiety-=4
  def shopping(self,manage):
           if self.car.drive():
               pass
     else:
       if self.car.fuel<20:
       self.shopping("fuel")
     else:
       self.to_repair()
    return
  if manage=="fuel":
     print("Купив пальне")
     self.money-=100
     self.car.fuel+=100
 elif manage=="food":

    print("Купив їжу")
    self.money-=50

    self.home.food+=50
 elif manage=="delicacies":
    print("Ура! Смаколики!")
    self.gladness+=10
    self.satiety+=2
    self.money-=15

 elif manage == "food":

    print("Купив їжу коту")
    self.money -= 50

    self.home.food+=50
  def chill(self):
     self.gladness+=10
     self.home.mess+=5
  def clean_home(self):
    self.gladness-=5
    self.home.mess=0
  def to_repair(self):
    self.car.strength+=100
    self.money-=50
  def day_indexes(self):
          pass
  def is_alive(self):
          pass
  def live(self):
  class Auto:
  def __init__(self,brand_list):
    self.brand=random.choice(list(brand_list))
    self.fuel=brand_list[self.brand]["fuel"]
    self.strength =brand_list[self.brand]["strength"]
    self.strength = brand_list[self.brand]["consumption"]
  def drive(self):
    if self.strength>0 and self.fuel>=self.consumptoin:
       self.fuel-=self.consumptoin
       self.strength-=1
    return True
      else:


   print("Машина не може рухатись")
    return Falseclass
    House:
  def __init__(self):
    self.mess = 0
    self.food = 0
    brand_of_car = {
        "BMV": {"fuel": 100, "strength": 100, "consumption": 6},
        "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
        "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
        "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}}

    class Job:
        def __init__(self, job_list):
          self.job = random.choice(list(job_list))
          self.salary = job_list[self.job]["salary"]
          self.gladnes_less = job_list[self.job]["gladness_less"]
         job_list = {
            "Java developer": {"salary": 50, "gladness_less": 10},
            "Paython developer": {"salary": 40, "gladness_less": 3},
            "C++ developer": {"salary": 45, "gladness_less": 25},
            "Rust developer": {"salary": 70, "gladness_less": 1}}

    class Cat:
      def __init__(self,job_list_new)
        self.job = random.choice(list(job_list_new))
        self.salary = job_list_new[self.job]["salary"]
        self.gladnes_less = job_list_new[self.job]["gladness_less"]
       job_list = {
           "eat corm": {"gladness_more": 40},
           "scolded": {"gladness_less": 30},
           "stroked": {"gladness_more": 25},
           "played": {"gladness_more": 50}