import pygame
from player import Player
from monster import Monster
class Game:
    def __init__(self):
        # definir si notre jeu a commence ou non  is_playing représente un booleen
        self.is_playing = False

        # lorsque un monstre rentre avec un joueur qui bouge plus on le fait avec un group de sprite qui contient le joueur
        self.all_players = pygame.sprite.Group()
        # generer notre joueur et on ensuite l'ajoute dans le groupe sprite
        self.player = Player(self)
        self.all_players.add(self.player)
        # pressed c est une table qui contient des touche active  saisit par le joueur
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()  # on recharge le monstre dans le construsteur de la classe Elle represente un monstre dans le jeu
        self.spawn_monster()  # Elle represente un monstre dans le jeu

    def game_over(self):
        # remettre le jeu à neuf , retirer les monstres et remettre les joueur à 100 de vie, le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
    def update(self, screen): # cette fonction regroupe tout les composant du jeux  et pour commencer le jeux

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur et on la met le screen  qui est notre écran
        self.player.update_health_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monster de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)  # screen notre notre surface
        # applique l'ensemble des image de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquons l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)

        # on verifie si le joueur souhaite aller à gauche ou a droite
        # game.player.rect.width la taille  du rectange de notre joueu et r
        #  screen.get_width() la taille de notre ecran
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():

            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:

            self.player.move_left()
        # print(game.player.rect.x) elle sert a les coodonnee deplacement de notre joueur
        # mettre à jour l'ecran


    def check_collision(self,sprite,group):# On met sprite pour comparer un element graphique

        # on met sprite pour comparer avec un groupe de sprite
         # pygame.sprite.spritecollide mask qui permet de tuer l entitè courante lorsqu'il rente en collision
        # False lorsque l entite joueur rentre en colision avec le monstre le joueur meurt immediatement
        # pygame.sprite.collide_mask c est type de collision
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)


    def spawn_monster (self): # fonction qui permet de reproduire un monstre
        monster = Monster(self) # on va modifier la classe monter pour lorsque un montre rentre en collision avec ne peut plus bouger
        self.all_monsters.add(monster) # on met sprite pour comparer un element graphique avec un group de sprite








