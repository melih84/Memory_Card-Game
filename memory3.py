import pygame, random, time
def main():
    # Our main function which plays the game and quits afterwards
    pygame.init()
    pygame.display.set_mode((550,416))
    pygame.display.set_caption('Memory')
    w_surface = pygame.display.get_surface()   
    game = Game(w_surface)
    game.play()
    pygame.quit()
    

class Game:
    def __init__(self,surface):
        #initializes a couple of properties which we will going to use in this class
        self.surface = surface 
        self.bg_color = pygame.Color('black')
        self.fps = 60
        self.close_clicked = False
        self.continue_game = True
        self.clicked_tiles = []
        first_image = pygame.image.load('image1.bmp') # We load our first image to test
        self.img_width = first_image.get_width() # We get image width and height
        self.img_height = first_image.get_height()
        images = ['image1.bmp', 'image2.bmp', 'image3.bmp', 'image4.bmp', 'image5.bmp', 'image6.bmp', 'image7.bmp', 'image8.bmp']
        self.question = pygame.image.load('image0.bmp') # Image of question mark (This image is going to be shown before the tile is clicked)
        
        self.img_list = []
        for i in images:
            # Load all of the other images
            self.img_list.append(pygame.image.load(i))
        self.game_clock = pygame.time.Clock()
        self.FPS = 30        
        self.score = 0
        self.game_over = False
        self.first_selection = None
    
        self.img_list = self.img_list * 2 # We will need 2 of each image in order to match them
        random.shuffle(self.img_list) # We shuffle images so that game can be played more than once 
        first_image = pygame.image.load('image1.bmp')
        self.img_width = first_image.get_width()
        self.img_height = first_image.get_height()

        # We create each tile with the parameters we declared on Tile class below
        # I didn't use a for loop here because I changed X and Y coordinates too much to get the best view
            
        self.tile1 = Tile([5,5], self.img_width, self.img_height, pygame.Color('blue'),self.img_list[0], self.surface)
        self.tile2 = Tile([5 + self.img_width + 2,5], self.img_width, self.img_height, pygame.Color('blue'),self.img_list[1], self.surface)
        self.tile3 = Tile([5 + (2 * self.img_width) + 4, 5], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[2], self.surface)
        self.tile4 = Tile([5 + (3 * self.img_width) + 6, 5], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[3], self.surface)
        self.tile5 = Tile([5, 5 + self.img_width + 2], self.img_width, self.img_width, pygame.Color('blue'), self.img_list[4], self.surface)
        self.tile6 = Tile([5 + self.img_width + 2, 5 + self.img_width + 2], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[5], self.surface)
        self.tile7 = Tile([5 + (2 * self.img_width) + 4, 5 + self.img_width + 2], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[6], self.surface)
        self.tile8 = Tile([5 + (3 * self.img_width) + 6, 5 + self.img_width + 2], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[7], self.surface)
        self.tile9 = Tile([5, 5 + (2 * self.img_width) + 4], self.img_width, self.img_width, pygame.Color('blue'), self.img_list[8], self.surface)
        self.tile10 = Tile([5 + self.img_width + 2, 5 + (2 * self.img_width) + 4], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[9], self.surface)
        self.tile11 = Tile([5 + (2 * self.img_width) + 4, 5 + (2 * self.img_width) + 4], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[10], self.surface)
        self.tile12 = Tile([5 + (3 * self.img_width) + 6, 5 + (2 * self.img_width) + 4], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[11], self.surface)
        self.tile13 = Tile([5, 5 + (3 * self.img_width) + 6], self.img_width, self.img_width, pygame.Color('blue'), self.img_list[12],self.surface)
        self.tile14 = Tile([5 + self.img_width + 2, 5 + (3 * self.img_width) + 6], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[13],self.surface)
        self.tile15 = Tile([5 + (2 * self.img_width) + 4, 5 + (3 * self.img_width) + 6], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[14],self.surface)
        self.tile16 = Tile([5 + (3 * self.img_width) + 6, 5 + (3 * self.img_width) + 6], self.img_width, self.img_width, pygame.Color('blue'),self.img_list[15], self.surface)
        
         
    def draw_score(self): 
                # We add a timer on the top right screen
                font_color = pygame.Color("white")
                font_bg    = pygame.Color("black")
                font       = pygame.font.SysFont("arial", 70)
                text_img   = font.render(str(self.score), True, font_color, font_bg)     
                text_pos   = (470,10)
                self.surface.blit(text_img, text_pos)     
                
    
                
    def update(self):
        # Updates the timer
        self.score = pygame.time.get_ticks() // 1000

        
    
    
    def draw_gamecontent(self):
        # Draws all of the tiles and the timer which we called "score"
        tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7, self.tile8, self.tile9,self.tile10, self.tile11, self.tile12, self.tile13, self.tile14, self.tile15, self.tile16]
        for i in range(len(tiles)):
            tiles[i].draw()
            if tiles[i].shown == False:
                self.surface.blit(self.question, (tiles[i].screen_position[0],tiles[i].screen_position[1]))
            else:
                self.surface.blit(self.img_list[i], (tiles[i].screen_position[0],tiles[i].screen_position[1]))
            
        self.draw_score()
        pygame.display.update()
        
    def mouse_clicked(self, event):
        # Checks if the tile is cliked
        tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7, self.tile8, self.tile9,self.tile10, self.tile11, self.tile12, self.tile13, self.tile14, self.tile15, self.tile16]
        self.click_pos = event.pos
        
        for i in range(len(tiles)):
            # Checks all of the tiles if they've been clicked
            if tiles[i].shown == False:
                if tiles[i].tile_rect.collidepoint(self.click_pos):
                    tiles[i].shown = True
                    self.clicked_tiles.append(tiles[i])

        # Player should lose their turn after they chose 2 tiles
        if (len(self.clicked_tiles) % 2 == 0 and len(self.clicked_tiles) != 0):
            self.check_pairs()
        
            
    def check_pairs(self): 
        # Checks if tiles have the same content
        tile_first = self.clicked_tiles.pop()
        tile_second = self.clicked_tiles.pop()
        self.surface.blit(tile_first.content, (tile_first.screen_position[0],tile_first.screen_position[1]))
        self.surface.blit(tile_second.content, (tile_second.screen_position[0],tile_second.screen_position[1]))
        pygame.display.update()
        pygame.time.wait(800)
        if (tile_first is not tile_second) and (tile_first.content == tile_second.content):
            # If tiles match, then both of the images have to appear until the game ends
            tile_first.shown = True
            tile_second.shown = True
        else:
            # If tiles do not match, then we have to close them again
            tile_first.shown = False
            tile_second.shown = False

        
    def play(self):
        #  This is the main game loop. This runs until the game ends or user decides to close the game
        while not self.close_clicked:
            self.handle_events()
            self.draw_gamecontent()
            
            if self.game_over == False:
                if self.decide_continue() == False:
                    self.game_over = True
                self.update()
                
    def decide_continue(self):
        # Cheks if the game ended. If it did, return False, True otherwise
        tiles_shown = 0
        tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7, self.tile8, self.tile9,self.tile10, self.tile11, self.tile12, self.tile13, self.tile14, self.tile15, self.tile16]
        for i in range(len(tiles)):
            if tiles[i].shown == True:
                tiles_shown += 1
            
        if tiles_shown == 16:
            return False
        else:
            return True
        
    
    def handle_events(self):
        # Controls events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_clicked(event)
               
            
             

class Tile:
    def __init__(self, screen_position, width, height, color, content, surface):
        # Initializes tile class with parameters above

        self.screen_position = screen_position
        self.width = width
        self.height = height
        self.surface = surface
        self.color = color     
        self.content = content
        self.tile_rect = pygame.Rect(self.screen_position[0], self.screen_position[1], self.width, self.height) # We have to create a pygame.Rect for each of the tiles to use draw() and collidepoint() methods
        self.shown = False
        
    def draw(self):
        pygame.draw.rect(self.surface, pygame.Color("blue"), self.tile_rect)
    
            
                                  
                            

            
        
       
        



main()