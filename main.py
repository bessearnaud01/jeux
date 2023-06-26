import pygame
import math
from game import Game
pygame.init()


pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((980,580))


# on va importer de charger l'arriere plan de notre jeu

background = pygame.image.load('assets/bg.jpg')

# importer et charger notre bannière
banner = pygame.image.load('assets/banner.png')
# Elle sert a redimensionner l'image pygame.transform.scale
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4) # on va import parce que on veut les valeur de fenetre float en divisant par 4 et la fonction c est arrrondit a lentier suivant

# on charge le boutton de bienvenu
play_button = pygame.image.load('assets/button.png')
# on redimensionne la hauteur et la largeur de notre boutton
play_button = pygame.transform.scale(play_button,(400,100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33) # on place boutton par rapport a taille de l ecran
play_button_rect.y = math.ceil(screen.get_width()/2.6) # on place boutton par rapport a taille de l ecran
# on va charger notre jeu
game = Game()

running = True




# boucle tant que cette condition est vraie

# si le joueur ferme cette fenetre event.get() est une liste d évenement et on cree une variable event#
while running:

    # appliquons l'arriere plan  de notre jeu
    screen.blit(background,(0,-320))
    # On va verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declenche les instruction de la partie
        game.update(screen)

    # verifions si notre jeu n'a pas commencé
    else:
        # ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner,banner_rect)


    # mettre à jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        # on verifie que  l evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
             running = False
             pygame.quit()

             print("Fermmeture du jeux")

        # on va detecter si un joueur lâche une touche du clavier

        elif event.type == pygame.KEYDOWN:

            # on va verifier quelle touche a été utiliser et on veut rendre le déplacement de  notre plus fluid
            # appuyer le boutton plusieur pour effectuer un deplacement

             game.pressed[event.key] = True
            # detecter si la touche espace est enclenché pour lancer le projectille

             if event.key == pygame.K_SPACE:

                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False  #quand la touche n'est pas utilisé

        elif event.type == pygame.MOUSEBUTTONDOWN: # elle sert de gerer les evenement de la souris
        # verfication pour savoir si la souris est en collision avec le boutton jouer
           if play_button_rect.collidepoint(event.pos): # elle recuepere toute les positions du clic de notre souris
              game.start()
