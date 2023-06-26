import pygame
from projectile import Projectile
# créer un prémier classe qui va representer notre joueur
 # pygame.sprite.Sprite Classe de base simple pour les objets de jeu visibles
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        # losrsqu'on genere un nouveau joueur passe l'instance de la classe game ds les parametre et c est poukoi on met  self.game = game
       # Et on va ceder par la fonction move_right
        super().__init__() # on va initialise la methode classe sprite
        self.game = game # elle
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 10 #deplacement
        self.all_projectiles = pygame.sprite.Group() # on veut lancer plusieurs projectiles
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect() # on crée un rectange pour recupere notre image et pour le fait déplacer grace à ses cotes
        self.rect.x = 400
        self.rect.y = 390

# on va verifier si le joueur peut subir des dommge tant que le monstre le touche notre  joueur elle diminue sa vie debut de code la classe monster et
    def damage(self, amount):
        if self.health - amount > amount:
             self.health -= amount # alors on subit la diminution du point de vue
        else:  # sinon
             self.game.game_over() # on va cree la methode dans la classe game_over




    # self cible l'objet courant la fontion de la barre de vie
    def update_health_bar(self, surface): # surface représent l'endroit ou va dessiner notre barre
        #Definir une couleur pour notre jauge de vie (vert claire)
        bar_color = (112,210,46)
       #Definissons une couleur pourl'arriere plan de la jauge(gris foncé)
        back_bar_color = (60,63,60)
    # Definir la position de notre jauge de vie ainsi que sa largeur ,son épaisseur et sera au dessus du monstre
        # self.rect.x et self.rect.y répresentent la position en x du joueur
        bar_position = [self.rect.x + 50 ,self.rect.y + 20 ,self.health,7]  # height = h et w = wigth et on recupere les coordonnées du monstre pour place la bar
        back_bar_position = [self.rect.x + 50, self.rect.y +20,self.max_health ,7] # bar gris de couleur de font de la barre
        # dessinons la couleur de font de notre barre
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessinons la barre de vie
        pygame.draw.rect(surface,bar_color,bar_position)

    def launch_projectile(self):
        #Créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self)) # on veut lancer un groupe de projectile
         # on prend self dans Projectile(self) les coordonnées pour qu'elle soit du meme niveau que la position du joueur
    def move_right(self):
         # si le joueur n est pas en collision avec un monstre alors il peut se deplace
        # Et sinon le joueur ne pas se deplacer
        if not self.game.check_collision(self,self.game.all_monsters):
           self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity