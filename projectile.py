import pygame


#definissons la classe qui va gerer le projectile de notre joueur
# pygame.sprite.Sprite Classe de base simple pour les objets de jeu visibles
class Projectile(pygame.sprite.Sprite):
    #definissons le constructeur de cette classe
    def __init__(self, player): # je recupere les coordonnées du joueur
        super().__init__()
        self.velocity = 5 # la vitesse du projectile
        self.player = player # elle a être utilise dans la fonction remove avec le groupe de projectiles
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50)) #On redimensionne la taille du projectile
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image # elle sert à garder le projectile sans la rotation pour ne pas perdre l' image original lorsqu'elle toume
        self.angle = 0 # la valeur de l'angle du projectile qui nous sert a tourner sur elle même

    def rotate(self):
        # elle sert a tourne projectille lorsqu'elle est en deplacement
        self.angle += 8 # la vitesse de rotation
        # A chaque on transforme une image ou un composant on utilise pygame.transform.rotozoom
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1) # 0n met toujour 1
        self.rect = self.image.get_rect(center = self.rect.center) # cetle methode a le projectile par rapport a son centre de rotation


    def remove(self): # Cette fonction permet de retirer les projectille or de l ecran
        self.player.all_projectiles.remove(self)

    def move(self): # fonction qui sert a deplace le projectile

        self.rotate()  # la fonction rotate sert a faire tourner le projectile sur lui même
        self.rect.x += self.velocity
        #verifier si le projectile entre en collision avec un monstre et je connais la liste des monstres qui etait impacté par le projectiles
        for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            # on va supprime le projectile si le projectile touche le joueur
            self.remove()
            # infliger des dégats et on recupere le points d'attaque de notre joueur
            monster.damage(self.player.attack)


        # On va verifier si notre projectile n'est plus présent sur notre écran
        if self.rect.x > 980:
            # Supprimé le projectile (en dehors de l ècran)
            self.remove()
            print("Projectile supprimé")