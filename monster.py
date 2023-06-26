
import pygame
import random


# créons une classe qui va gerer la notion de monster sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__() # on appelle la classse sprite pour la charge dans la fonction
        self.game = game # elle permet de les monstre en collision
        self.health = 100 # point de vie au cours du jeu
        self.max_health = 100 # point de vie au initial
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 980 + random.randint(0,300)
        self.rect.y = 430
        self.velocity = random.randint(1,3)  # On choisit la vitesse monstre au hasard entre  1 et 3

   # fonction qui permet de reduire les points de vies au monstre
    def damage(self, amount):
        # infiger les degats
        self.health -= amount
        #verifier si son nouveau nombre de points de vie est inferieur ou égal a 0 si c est qu'il est mort
        if self.health <= 0:
            # Je vais  reapparaitre  un nouveau monstre apres la mort d un autre monster
            self.rect.x = 980 +random.randint(0,300)
            self.health = self.max_health
            self.velocity = random.randint(1, 3) # On donne vitesse au hasard des monstres ou un momstre qui reapparaitre

    # self cible l'objet courant la fontion de la barre de vie
    def update_health_bar(self, surface): # surface représent l'endroit ou va dessiner notre barre
        #Definir une couleur pour notre jauge de vie (vert claire)
        bar_color = (112,210,46)
       #Definissons une couleur pourl'arriere plan de la jauge(gris foncé)
        back_bar_color = (60,63,60)
    # Definir la position de notre jauge de vie ainsi que sa largeur ,son épaisseur et sera au dessus du monstre
        # self.rect.x et self.rect.y répresentent la position en x du joueur
        bar_position = [self.rect.x + 10 ,self.rect.y -20 ,self.health,5]  # height = h et w = wigth et on recupere les coordonnées du monstre pour place la bar
        back_bar_position = [self.rect.x + 10, self.rect.y - 20,self.max_health , 5] # bar gris de couleur de font de la barre
        # dessinons la couleur de font de notre barre
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessinons la barre de vie
        pygame.draw.rect(surface,bar_color,bar_position)

    def forward(self): # fonction deplacement vers l'avant forward

        # Le deplacemet ne se fait pas que si le monstre et un joueur se touche
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity
        # Si le monstre est en collision avec le joueur
        else:
            # Infliger les degats(au joueur) et on va dans la classe avec la damage
            self.game.player.damage(self.attack)



