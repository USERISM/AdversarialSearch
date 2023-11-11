import pygame
import time

MAX = 1
MIN = 2

class Node:
    def __init__(self, parent=None, side=None, depth=0, value=None):
        self.parent = parent
        self.value = value
        self.path = None        
        self.leftChild = None
        self.rightChild = None

        if self.parent is None:
            self.position = (500, 50)  # The position of the root node           
        else:
            if side == "L":
                self.position = (parent.position[0] - 150 // depth, parent.position[1] + 150)  # Left child position        
            else:
                self.position = (parent.position[0] + 150 // depth, parent.position[1] + 150)  # Right child position

class Tree:
    def __init__(self):
        self.root_node = Node(parent=None)
                      
    def createEmptyTree(self, node, depth, values):
        if depth == 0 or not values:
            return
        else:
            node.leftChild = Node(parent=node, side="L", depth=depth, value=values.pop(0))
            node.rightChild = Node(parent=node, side="R", depth=depth, value=values.pop(0))
            self.createEmptyTree(node.leftChild, depth - 1, values)
            self.createEmptyTree(node.rightChild, depth - 1, values)

    @staticmethod
    def draw_triangle(surface, x, y):
        points = [(x, y - 20), (x + 20, y + 20), (x - 20, y + 20)]
        pygame.draw.polygon(surface, (255, 0, 0), points)

    def drawTree(self, node, depth, player):
        if node:
            self.draw_triangle(screen, node.position[0], node.position[1])
            font = pygame.font.Font(None, 24)
            text = font.render(str(node.value), True, (255, 255, 255))
            screen.blit(text, (node.position[0] - 10, node.position[1] - 10))
            self.drawTree(node.leftChild, depth - 1, player)
            self.drawTree(node.rightChild, depth - 1, player)

def main():
    # Initialize pygame
    pygame.init()

    # Create the screen
    global screen
    w = 1000  # The width of the window
    h = 800   # The height of the window 
    screen = pygame.display.set_mode(((w, h)))

    # Title
    pygame.display.set_caption("MINIMAX")

    tree = Tree()
    values = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
    depth = 4

    # Game loop
    running = True   
    draw = True    
    
    while running:

        # RGB coloring of the screen
        screen.fill((192, 192, 192))
        
        # Add the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   

        if draw == True:   
            tree.createEmptyTree(tree.root_node, depth, values)
            tree.drawTree(tree.root_node, depth, player=MAX)
            pygame.display.update()
            time.sleep(1.5)            
            draw = False         

if __name__ == "__main__":
    main()
