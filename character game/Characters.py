class Character:
    def __init__(self, name, age, ranking, position, special_power = "Nothing"):
        self.name = name
        self.age = age
        self.ranking = ranking
        self.position = position
        self.special_power = special_power
    def details(self):
        print(f"The charcter details: \nName:{self.name}\nAge:{self.age}\nRanking:{self.ranking}\nPosition:{self.position}\nspecial power:{self.special_power}")

class Hero(Character):
    def __init__(self, job, name, age, ranking, position, special_power = "Nothing"):
        super().__init__(name, age, ranking, position, special_power = "Nothing")
        self.job = job
        
     
    def intelligence(self):
        print(f"{self.name} have high intelligence")
            
    def shooter(self):
        print(f"{self.name} is a best shooter")
            
    def mission(self):
        print(f"{self.name} will help daugther of america president, Ashley")
            

        
class Villan(Character):
    def strength(self):
        print(f"{self.name} has strength power ")
    def recover(self):
        print(f"{self.name} get his health recover")
    def fast(self):
        print(f"{self.name} have high speed")
            
class Vilian2(Villan):
    def monster(self):
        print(f"{self.name} get monster with 4 legs")
    def bulletproof(self):
        print(f"{self.name} skin is bulletproof")
    def recover(self):
        print(f"{self.name} recovers from any injury quickly")
    
    
    

    