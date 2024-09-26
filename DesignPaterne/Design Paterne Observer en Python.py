# Il faut rédiger un code python pour répondre à la "problématique" en fonction des éléments "Application - Observer (Design pattern)"

# Problématique : Soient des clients d'une collections de services, ils souhaitent accéder à la disponibilité d'un des
# services pour effectuer une tâche. Doivent-ils demander la disponibilité du service régulièrement pour effectuer
# leur tâche?
# • Solution : La collection de services doit définir des notifications, adressées à l'ensemble de ses clients pour qu'ils
# puissent faire appel au service demandé.

# Application - Observer (Design pattern)

# • Problématique : Un objet éditeur (publisher) souhaite, suite à certaines actions, transmettre des notifications à une liste
# d'observateurs, liste que l'éditeur ne connait pas au préalable.
# • Solution : L'éditeur dispose d'une liste d'observateurs, et à chaque action il doit envoyer une notification à ses observateurs,
# qui à leur tour doivent traiter de manière personnalisée.
# • Objectif Application :
# – Définir le diagramme de classes faisant intervenir les différents classes et leurs relations. Les classes:
# • publisher : correspond à un Editeur de texte et dispose des méthodes pour ouvrir, écrire et fermer (sur) un fichier
# • Observers :
# – La classe LogObserver : correspond à une gestion de log, qui permet d'écrire les messages des les notifications
# auxquelles il est abonné
# – La classe ConsoleObserver : correspond à la console, qui permet d'afficher sur la console les message des
# notifications auxquelles il est abonné

# copilote : 
#     Pour répondre à cette problématique en utilisant le design pattern Observer, nous allons définir les classes nécessaires et leurs relations. Voici un diagramme de classes simplifié et une implémentation en Python.

# Diagramme de Classes
# Publisher : Éditeur de texte avec des méthodes pour ouvrir, écrire et fermer un fichier.
# Observer : Interface pour les observateurs.
# LogObserver : Observateur qui gère les logs.
# ConsoleObserver : Observateur qui affiche les notifications sur la console.
# EventManager : Gère les observateurs et les notifications.


from abc import ABC, abstractmethod

# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# LogObserver
class LogObserver(Observer):
    def update(self, message: str):
        with open("log.txt", "a") as log_file:
            log_file.write(message + "\n")

# ConsoleObserver
class ConsoleObserver(Observer):
    def update(self, message: str):
        print(f"Console: {message}")

# EventManager
class EventManager:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer: Observer):
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Publisher
class Publisher:
    def __init__(self, event_manager: EventManager):
        self._event_manager = event_manager

    def open_file(self, filename: str):
        self._event_manager.notify(f"Opening file: {filename}")

    def write_file(self, filename: str, content: str):
        self._event_manager.notify(f"Writing to file: {filename}")
        with open(filename, "a") as file:
            file.write(content + "\n")

    def close_file(self, filename: str):
        self._event_manager.notify(f"Closing file: {filename}")

# Utilisation
event_manager = EventManager()
log_observer = LogObserver()
console_observer = ConsoleObserver()

#Cyril on ouvert 2 canaux (Log et Fichier Log)pour une seul action action ?
#
event_manager.subscribe(log_observer)
event_manager.subscribe(console_observer)

publisher = Publisher(event_manager)
publisher.open_file("example.txt")
publisher.write_file("example.txt", "Hello, World!")
publisher.close_file("example.txt")


# Explication
# Observer : Interface abstraite pour les observateurs avec une méthode update.
# LogObserver : Implémente Observer et écrit les messages dans un fichier log.
# ConsoleObserver : Implémente Observer et affiche les messages sur la console.
# EventManager : Gère l’abonnement, le désabonnement et la notification des observateurs.
# Publisher : Éditeur de texte qui utilise EventManager pour notifier les observateurs des actions effectuées sur les fichiers.
# Cette implémentation permet aux clients de recevoir des notifications en temps réel sans avoir à interroger constamment la disponibilité des services.