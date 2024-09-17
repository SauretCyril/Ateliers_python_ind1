# Application Singleton

# • Définir la classe Singleton, classe pour laquelle on ne peut définir qu’une instance unique

class Singleton:
  _instance = None

ins1 = Singleton()
ins2 = Singleton()
print(ins1 is ins2) # retourne True