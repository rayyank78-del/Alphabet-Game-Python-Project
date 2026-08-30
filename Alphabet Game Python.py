import pygame
pygame.font.init()


# defining shortcuts for all of the colours.

white = (255,255,255)
brown = (102,51,0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
purple = (127, 0, 255)
grey = (128,128,128)
orange = (255, 129, 0)
green = (0, 255, 0)
pink = (255, 0, 255)
red = (255, 0, 0)
black = (0,0,0)
yellow = (255, 255, 0)
filled = 0
font = pygame.font.SysFont("comicsansms", 180)


class buttons(object):
    def __init__(self,rect,command,**triggers):   
        self.rect = pygame.Rect(rect)
        self.command = command
        self.clicked = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.process_triggers(triggers)
        self.write_words()

    
  
    def process_triggers(self,triggers):                # buttons settings that determine, the shape, size, colour and font of the buttons
        settings = {


            "color"             : (blue),
            "border_hover_color": (green),          
            "radius"            : 3,
            "call_on_release"   : True,
            "disabled"          : False,
            "clicked_color"     : None,            
            "hover_font_color"  : None,
            "clicked_font_color": None,
            "click_sound"       : None,            
            "font"              : None,             
            "hover_color"       : None,
            "hover_sound"       : None,
            "text"              : None,
            "font"              : pygame.font.Font(None,40),
            "font_color"        : (white),
            "border_color"      : (red),

        }
        
        for trigger in triggers:
            if trigger in settings:
                settings[trigger] = triggers[trigger]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, trigger))
        self.__dict__.update(settings)
        

    def area_buttons(self, photo, rect, color, r):
        corners = rect.inflate(-2*r, -2*r)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            pygame.draw.circle(photo, color, getattr(corners,attribute), r)
        photo.fill(color, rect.inflate(-2*r,0))
        photo.fill(color, rect.inflate(0,-2*r))

    def make_buttons(self, surface, rect, color, r=20, edge=0, interior=(0,0,0,0)):
        rect = pygame.Rect(rect)
        zeroed_rect = rect.copy()
        zeroed_rect.topleft = 0,0
        picture = pygame.Surface(rect.size).convert_alpha()
        picture.fill((0,0,0,0))
        self.area_buttons(picture, zeroed_rect, color, r)
        if edge:
            zeroed_rect.inflate_ip(-2*edge, -2*edge)
            self.area_buttons(picture, zeroed_rect, interior, r)
        surface.blit(picture, rect)


  
    def draw(self,surface): 
        color = self.color
        text = self.text
        border = self.border_color
        self.touch_buttons()
        if not self.disabled:
            if self.clicked and self.clicked_color:
                color = self.clicked_color
                if self.clicked_font_color:
                    text = self.clicked_text
            elif self.hovered and self.hover_color:
                color = self.hover_color
                if self.hover_font_color:
                    text = self.hover_text
            if self.hovered and not self.clicked:
                border = self.border_hover_color
        else:
            color = self.disabled_color
          
       
        if self.radius:
            rad = self.radius
        else:
            rad = 0
        self.make_buttons(surface, self.rect , border, rad, 1, color)
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text,text_rect)

    def press_buttons(self,event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.function()
  

    def position_buttons(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.press_buttons(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.let_go_buttons(event)
  

    
    def touch_buttons(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def write_words(self):
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text,True,color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text,True,color)
            self.text = self.font.render(self.text,True,self.font_color)
            

    def let_go_buttons(self,event):
        if self.clicked and self.call_on_release:
        
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.command()
        self.clicked = False
              


import string
pygame.init()
screen = pygame.display.set_mode((1900,1000))
screen_rect = screen.get_rect()
done = False


# this is a dictionary that stores all the words that correspond to the certain letter which they begin with.

dictionary = {

    "a": "apple",
    "b": "ball",
    "c": "cat",
    "d": "dog", 
    "e": "egg",
    "f": "food",
    "g": "garden",
    "h": "happy",
    "i": "ice",
    "j": "juice", 
    "k": "key",
    "l": "leg",
    "m": "milk",
    "n": "night",
    "o": "outside",
    "p": "police",
    "q": "quick",
    "r": "rice",
    "s": "sun", 
    "t": "toys", 
    "u": "up", 
    "v": "vegetables", 
    "w": "water",
    "x": "x-ray",
    "y": "yell",
    "z": "zoo" }


# when the button is clicked by the mouse, python should display the letter that has been clicked and the corresponding word from the dictionary in the Python 3.8.1 Shell tab.  
#  On the main PyGame window, an image of the corresponding word should be displayed on the screen along with the written corresponding word below the image.


def print_on_press(letter):
    print ("")
    print(f'The letter "{letter}" has been pressed')
    print(f'The corresponding word is "{dictionary[letter]}"')
    print("")
    text = font.render((f"{dictionary[letter]}"), True, green)
    
    screen.fill(brown)
    try:

        img = pygame.image.load(f"{dictionary[letter]}.jpg")
        
    except:
        try:
            img = pygame.image.load(f"{dictionary[letter]}.png")
            
        except:
            img = pygame.image.load(f"{dictionary[letter]}.jfif")            
            
    screen.blit(img, (550,50))
    screen.blit(text,(700, 720))
    

# Code for the coloured triangles displayed on the right hand side of the PyGame window.


    y1=(1900,0)
    y2=(1700,200)
    y3=(1900,200)

    pygame.draw.polygon(screen, (red), [(y1), (y2), (y3)], filled)


    z1=(1700,200)
    z2=(1700,0)
    z3=(1900,0)

    pygame.draw.polygon(screen, (green), [(z1), (z2), (z3)], filled)


    q1=(1900,200)
    q2=(1700,400)
    q3=(1900,400)

    pygame.draw.polygon(screen, (white), [(q1), (q2), (q3)], filled)
    
    
    r1=(1700,200)
    r2=(1900,200)
    r3=(1700,400)

    pygame.draw.polygon(screen, (purple), [(r1), (r2), (r3)], filled)
    

    d1=(1900,600)
    d2=(1700,600)
    d3=(1900,400)

    pygame.draw.polygon(screen, (pink), [(d1), (d2), (d3)], filled)
    
    
    e1=(1700,600)
    e2=(1900,400)
    e3=(1700,400)

    pygame.draw.polygon(screen, (yellow), [(e1), (e2), (e3)], filled)
    

    b1=(1900,800)
    b2=(1700,800)
    b3=(1900,600)
    

    pygame.draw.polygon(screen, (grey), [(b1), (b2), (b3)], filled)


    c1=(1700,800)
    c2=(1900,600)
    c3=(1700,600)

    pygame.draw.polygon(screen, (aqua), [(c1), (c2), (c3)], filled)


    x1=(1900,1000)
    x2=(1900,800)
    x3=(1700,1000)

    pygame.draw.polygon(screen, (blue), [(x1), (x2), (x3)], filled)


    a1=(1900,800)
    a2=(1700,1000)
    a3=(1700,800)

    pygame.draw.polygon(screen, (orange), [(a1), (a2), (a3)], filled)


# Code for the coloured triangles displayed on the left hand side of the PyGame window.


    f1=(150,0)
    f2=(150,200)
    f3=(350,200)

    pygame.draw.polygon(screen, (orange), [(f1), (f2), (f3)], filled)


    g1=(350,200)
    g2=(150,0)
    g3=(350,0)

    pygame.draw.polygon(screen, (blue), [(g1), (g2), (g3)], filled)

    h1=(350,1000)
    h2=(150,800)
    h3=(150,1000)

    pygame.draw.polygon(screen, (green), [(h1), (h2), (h3)], filled)


    i1=(350,800)
    i2=(350,1000)
    i3=(150,800)

    pygame.draw.polygon(screen, (red), [(i1), (i2), (i3)], filled)


    j1=(350,800)
    j2=(150,800)
    j3=(150,600)

    pygame.draw.polygon(screen, (purple), [(j1), (j2), (j3)], filled)


    k1=(350,800)
    k2=(350,600)
    k3=(150,600)

    pygame.draw.polygon(screen, (white), [(k1), (k2), (k3)], filled)
    

    l1=(350,600)
    l2=(150,600)
    l3=(150,400)

    pygame.draw.polygon(screen, (yellow), [(l1), (l2), (l3)], filled)
    
    
    m1=(350,600)
    m2=(350,400)
    m3=(150,400)

    pygame.draw.polygon(screen, (pink), [(m1), (m2), (m3)], filled)
    

    n1=(350,200)
    n2=(150,200)
    n3=(350,400)

    pygame.draw.polygon(screen, (grey), [(n1), (n2), (n3)], filled)
    
    
    o1=(150,200)
    o2=(350,400)
    o3=(150,400)

    pygame.draw.polygon(screen, (aqua), [(o1), (o2), (o3)], filled)


    
   
settings = {}

btns = []
for position, letter in enumerate(string.ascii_lowercase):
    btn_height = 38
    spacer = 10
    top = position*btn_height + spacer
    b = buttons(rect=(10,top,105,btn_height), command=lambda l=letter:print_on_press(l), text=letter, **settings)
    btns.append(b)

while not done:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        for btn in btns:
            btn.position_buttons(event)
    for btn in btns:
        btn.draw(screen)
    pygame.display.update()





    



##
##import time
##time.sleep(2)
##print ("This is a quiz to test your knowlege of the alphabet.")
##print("")
##time.sleep(1.75)
##print("All answers must use the words that you have learnt from the alphabet game.")
##print("")
##time.sleep(1.75)
##print("Only write in lower case please. ")
##print("")
##time.sleep(1.75)
##print("Type your answer next to the question.")
##print("")
##time.sleep(2)
##print("Ready?")
##
##dictionary = {
##
##    "a": "apple",
##    "b": "ball",
##    "c": "cat",
##    "d": "dog", 
##    "e": "egg",
##    "f": "food",
##    "g": "garden",
##    "h": "happy",
##    "i": "ice",
##    "j": "juice", 
##    "k": "key",
##    "l": "leg",
##    "m": "milk",
##    "n": "night",
##    "o": "outside",
##    "p": "police",
##    "q": "quick",
##    "r": "rice",
##    "s": "sun", 
##    "t": "toys", 
##    "u": "up", 
##    "v": "vegetables", 
##    "w": "water",
##    "x": "x-ray",
##    "y": "yell",
##    "z": "zoo" }
##
##
##print ("")
##print ("")
##
##time.sleep(3)
##
##for letter in dictionary:
##    ans = input(f"What word starts with: '{letter}' ? ")
##    while ans != dictionary[letter]:
##        print ("")
##        print ("")
##        print("WRONG. Try again")
##        print ("")
##        print ("")
##        ans = input(f"What word starts with: '{letter}' ? ")
##    print ("")
##    print ("")
##    time.sleep(0.5)
##    print("CORRECT. Well Done!")
##    print ("")
##    print ("")
##    time.sleep(0.5)
##        




        
