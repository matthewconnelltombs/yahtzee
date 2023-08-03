import numpy as np
import pygame
import sys
import random


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.board = np.full((ROW_COUNT, COLUMN_COUNT), None)
        self.turn = 0
        self.roll_counter = 1
        self.dice = [1, 1, 1, 1, 1]
        self.choice = [1, 1, 1, 1, 1]
        self.ses_score = None

    # Rolls the selected dice
    def roll_dice(self, rolls=5, delay=50):
        for rolling in range(rolls):

            for dice_num in range(5):
                if self.choice[dice_num] == 1:
                    self.dice[dice_num] = random.randint(1, 6)

            self.draw_dice()
            pygame.time.wait(delay * (rolling + 1))
            pygame.display.update()

    # Draws the dice on the board
    def draw_dice(self):
        dice_spot = [[685, 150], [685 + 180, 150], [625, 300], [625 + 150, 300], [625 + 300, 300]]

        for dice_num in range(5):

            # Draws dice with no pips
            pygame.draw.rect(self.screen, BLACK, (dice_spot[dice_num][0], dice_spot[dice_num][1] + 15, 100, 70))
            pygame.draw.rect(self.screen, BLACK, (dice_spot[dice_num][0] + 15, dice_spot[dice_num][1], 70, 100))
            pygame.draw.circle(self.screen, BLACK, (dice_spot[dice_num][0] + 15, dice_spot[dice_num][1] + 15), 15)
            pygame.draw.circle(self.screen, BLACK, (dice_spot[dice_num][0] + 15, dice_spot[dice_num][1] + 85), 15)
            pygame.draw.circle(self.screen, BLACK, (dice_spot[dice_num][0] + 85, dice_spot[dice_num][1] + 15), 15)
            pygame.draw.circle(self.screen, BLACK, (dice_spot[dice_num][0] + 85, dice_spot[dice_num][1] + 85), 15)

            # Draws pips
            if self.dice[dice_num] == 1:
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 50, dice_spot[dice_num][1] + 50), 10)
            elif self.dice[dice_num] == 2:
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 75), 10)
            elif self.dice[dice_num] == 3:
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 50, dice_spot[dice_num][1] + 50), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 75), 10)
            elif self.dice[dice_num] == 4:
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 75), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 75), 10)
            elif self.dice[dice_num] == 5:
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 75), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 50, dice_spot[dice_num][1] + 50), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 75), 10)
            elif self.dice[dice_num] == 6:
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 25, dice_spot[dice_num][1] + 75), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 50, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 50, dice_spot[dice_num][1] + 75), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 25), 10)
                pygame.draw.circle(self.screen, WHITE, (dice_spot[dice_num][0] + 75, dice_spot[dice_num][1] + 75), 10)

        pygame.display.update()

    # Draws the red/green buttons to pick dice to hold/roll
    def draw_dice_button(self):
        dice_button_spot = [[715, 425], [715 + 150, 425], [640, 525], [640 + 150, 525], [640 + 300, 525]]

        for dice_num in range(5):
            if self.choice[dice_num] == 1:
                pygame.draw.rect(self.screen, GREEN,
                                 (dice_button_spot[dice_num][0], dice_button_spot[dice_num][1], 70, 70))
            else:
                pygame.draw.rect(self.screen, RED,
                                 (dice_button_spot[dice_num][0], dice_button_spot[dice_num][1], 70, 70))
        pygame.display.update()

    # Calculates the possibles scores for the current dice
    def calc_board(self):
        # Upper section scoring
        for dice_pos in range(1, 7):
            total = 0
            for d in self.dice:
                if d == dice_pos:
                    total += d
            self.board[dice_pos][1] = total

        # Three of a kind
        values = [0, 0, 0, 0, 0, 0]
        for d in self.dice:
            values[d - 1] += 1
        if sorted(values)[5] >= 3:
            self.board[10][1] = sum(self.dice)
        else:
            self.board[10][1] = 0

        # Four of a kind
        values = [0, 0, 0, 0, 0, 0]
        for d in self.dice:
            values[d - 1] += 1
        if sorted(values)[5] >= 4:
            self.board[11][1] = sum(self.dice)
        else:
            self.board[11][1] = 0

        # Full House
        values = [0, 0, 0, 0, 0, 0]
        for d in self.dice:
            values[d - 1] += 1
        if sorted(values)[4:6] == [2, 3]:
            self.board[12][1] = 25
        else:
            self.board[12][1] = 0

        # Small Straight
        sm_straight = False
        values = [0, 0, 0, 0, 0, 0]
        for d in self.dice:
            values[d - 1] = 1
        for i in range(3):
            if values[0 + i:4 + i] == [1, 1, 1, 1]:
                sm_straight = True
        if sm_straight:
            self.board[13][1] = 30
        else:
            self.board[13][1] = 0

        # Large Straight
        lg_straight = False
        values = [0, 0, 0, 0, 0, 0]
        for d in self.dice:
            values[d - 1] += 1
        for i in range(2):
            if values[0 + i:5 + i] == [1, 1, 1, 1, 1]:
                lg_straight = True
        if lg_straight:
            self.board[14][1] = 40
        else:
            self.board[14][1] = 0

        # Chance
        self.board[15][1] = sum(self.dice)

        # Five of a kind
        values = [0, 0, 0, 0, 0, 0]
        for d in self.dice:
            values[d - 1] += 1
        if sorted(values)[5] == 5:
            if self.board[16][0] is None:
                self.board[16][1] = 50
            elif self.board[16][0] > 0:
                self.board[16][1] = 100
            else:
                self.board[16][1] = 0
        else:
            self.board[16][1] = 0

    def draw_grid(self):
        for r in range(ROW_COUNT):
            pygame.draw.rect(self.screen, BLACK,
                             (0, r * RECTANGLE_HEIGHT,
                              2 * RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
            pygame.draw.rect(self.screen, WHITE,
                             (5, r * RECTANGLE_HEIGHT + 5,
                              2 * RECTANGLE_WIDTH - 5, RECTANGLE_HEIGHT - 5))
        for r in range(ROW_COUNT):
            pygame.draw.rect(self.screen, BLACK,
                             (2 * RECTANGLE_WIDTH, r * RECTANGLE_HEIGHT,
                              RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
            pygame.draw.rect(self.screen, WHITE,
                             (2 * RECTANGLE_WIDTH + 5, r * RECTANGLE_HEIGHT + 5,
                              RECTANGLE_WIDTH - 5, RECTANGLE_HEIGHT - 5))

            pygame.draw.rect(self.screen, BLACK,
                             (3 * RECTANGLE_WIDTH, r * RECTANGLE_HEIGHT,
                              RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
            pygame.draw.rect(self.screen, WHITE,
                             (3 * RECTANGLE_WIDTH + 5, r * RECTANGLE_HEIGHT + 5,
                              RECTANGLE_WIDTH - 10, RECTANGLE_HEIGHT - 5))

        pygame.draw.rect(self.screen, GREY, (5, 5, 4 * RECTANGLE_WIDTH - 10, RECTANGLE_HEIGHT - 5))
        pygame.draw.rect(self.screen, GREY, (5, 365, 4 * RECTANGLE_WIDTH - 10, RECTANGLE_HEIGHT - 5))

        pygame.draw.rect(self.screen, WHITE, (4 * RECTANGLE_WIDTH, 0, RECTANGLE_WIDTH * 3, height))

        label = font1.render("UPPER SECTION", True, BLACK)
        self.screen.blit(label, (15, 5))
        label = font1.render("LOWER SECTION", True, BLACK)
        self.screen.blit(label, (15, 365))
        label = font1.render("BONUS (>=63)", True, BLACK)
        self.screen.blit(label, (15, 325))

        label = font1.render("TOTAL", True, BLACK)
        self.screen.blit(label, (15, 285))
        label = font1.render("UPPER TOTAL", True, BLACK)
        self.screen.blit(label, (15, 685))
        label = font1.render("LOWER TOTAL", True, BLACK)
        self.screen.blit(label, (15, 725))
        label = font1.render("GRAND TOTAL", True, BLACK)
        self.screen.blit(label, (15, 765))

        for l in range(len(uplabels)):
            label = font2.render(uplabels[l], True, BLACK)
            self.screen.blit(label, (30, 50 + l * 40))

        for l in range(len(downlabels)):
            label = font2.render(downlabels[l], True, BLACK)
            self.screen.blit(label, (30, 410 + l * 40))

        pygame.draw.rect(self.screen, BLACK, (625, 650, 405, 125))
        label = font3.render("ROLL", True, WHITE)
        self.screen.blit(label, (750, 675))

        pygame.draw.rect(self.screen, BLACK, (930, 0, 120, 50))
        label = font1.render("Reset", True, WHITE)
        self.screen.blit(label, (945, 10))

        # Draw high score
        with open("score.txt", "r") as file:
            ov_score = file.read()

        label = font1.render("Overall High", True, BLACK)
        self.screen.blit(label, (610, 5))
        label = font1.render("Score: " + ov_score, True, BLACK)
        self.screen.blit(label, (610, 30))
        label = font1.render("Session High", True, BLACK)
        self.screen.blit(label, (610, 60))
        if self.ses_score is None:
            label = font1.render("Score: ", True, BLACK)
        else:
            label = font1.render("Score: " + str(self.ses_score), True, BLACK)
        self.screen.blit(label, (610, 85))

    # Draws the points for available options
    def draw_point_button(self, yahtzee=False):
        for row in range(ROW_COUNT):
            if self.board[row][1] is not None:
                if self.board[row][0] is not None:
                    pygame.draw.rect(self.screen, RED, (455, 5 + row * 40, 140, 35))
                else:
                    pygame.draw.rect(self.screen, GREEN, (455, 5 + row * 40, 140, 35))
                    label = font2.render(str(self.board[row][1]), True, BLACK)
                    self.screen.blit(label, (455 + 57, 10 + row * 40))

        if self.board[16][1] == 100:
            pygame.draw.rect(screen, GREEN, (455, 5 + 16 * 40, 140, 35))
            label = font2.render(str(self.board[16][1]), True, BLACK)
            self.screen.blit(label, (455+47, 10 + 16 * 40))

        if yahtzee:
            if self.board[self.dice[0]][0] is not None:
                check_rows = [12, 13, 14]
                updated_points = [25, 30, 40]
                for row, points in zip(check_rows, updated_points):
                    if self.board[row][0] is None:
                        self.board[row][1] = points
                        pygame.draw.rect(self.screen, GREEN, (455, 5 + row * 40, 140, 35))
                        label = font2.render(str(self.board[row][1]), True, BLACK)
                        self.screen.blit(label, (455 + 57, 10 + row * 40))

    # Draw current scores
    def draw_current_score(self):
        top_six_score = 0
        upper_score = 0
        lower_score = 0
        upper_count = 0
        lower_count = 0

        for l in range(1, 7):
            if self.board[l][0] is not None:
                top_six_score += self.board[l][0]
                upper_count += 1

        if upper_count > 0:
            self.board[7][0] = top_six_score

        if upper_count == 6:
            if top_six_score >= 63:
                self.board[8][0] = 35
                upper_score = top_six_score + 35
            else:
                self.board[8][0] = 0
                upper_score = top_six_score

            self.board[17][0] = upper_score

        for l in range(10, 17):
            if self.board[l][0] is not None:
                lower_score += self.board[l][0]
                lower_count += 1

        if lower_count > 0:
            self.board[18][0] = lower_score

        if (upper_count + lower_count) == 13:
            self.board[19][0] = upper_score + lower_score

        for l in range(ROW_COUNT):
            if self.board[l][0] is not None:
                label = font2.render(str(self.board[l][0]), True, BLACK)
                screen.blit(label, (362, 10 + l * 40))

    # Draw the game
    def draw_game(self):
        self.calc_board()
        self.draw_grid()
        self.draw_dice()

        pygame.display.update()

    # Update the game
    def update_game(self):
        self.calc_board()
        self.draw_point_button()
        self.draw_dice()
        if self.roll_counter != 4:
            self.draw_dice_button()

        pygame.display.update()

    # Clean game
    def clean_game(self):
        self.draw_grid()
        self.calc_board()
        self.draw_dice()
        self.draw_current_score()

        pygame.display.update()

    # Reset game
    def reset_game(self):
        self.board = np.full((ROW_COUNT, COLUMN_COUNT), None)
        self.turn = 0
        self.roll_counter = 1
        self.choice = [1, 1, 1, 1, 1]
        self.draw_game()


# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Labels
uplabels = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
downlabels = ["3 of a Kind", "4 of a Kind", "Full House", "Small Straight", "Large Straight", "Chance", "YAHTZEE"]


# Fonts
pygame.font.init()
font1 = pygame.font.SysFont("monospace", 30)
font2 = pygame.font.SysFont("monospace", 24)
font3 = pygame.font.SysFont("monospace", 60)


# Initialize Pygame
pygame.init()


# Set up the screen
ROW_COUNT = 20
COLUMN_COUNT = 7

RECTANGLE_HEIGHT = 40
RECTANGLE_WIDTH = 150

width = COLUMN_COUNT * RECTANGLE_WIDTH
height = ROW_COUNT * RECTANGLE_HEIGHT + 5

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yahtzee")


# Create an instance of the Game class
game = Game(screen)
game.draw_game()


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Counter for # of turns played
        counter = 0
        for row in range(ROW_COUNT):
            if game.board[row][0] is not None:
                counter = counter + 1

        # For each click
        if event.type == pygame.MOUSEBUTTONDOWN and counter < 18:
            posx = event.pos[0]
            posy = event.pos[1]

            # If roll counter is 2/3, draw the dice choices
            if game.roll_counter in [2, 3]:
                if 715 <= posx <= 785 and 425 <= posy <= 495:
                    game.choice[0] = (game.choice[0] + 1) % 2
                    game.draw_dice_button()
                elif 865 <= posx <= 935 and 425 <= posy <= 495:
                    game.choice[1] = (game.choice[1] + 1) % 2
                    game.draw_dice_button()
                elif 640 <= posx <= 710 and 525 <= posy <= 595:
                    game.choice[2] = (game.choice[2] + 1) % 2
                    game.draw_dice_button()
                elif 790 <= posx <= 860 and 525 <= posy <= 595:
                    game.choice[3] = (game.choice[3] + 1) % 2
                    game.draw_dice_button()
                elif 940 <= posx <= 1010 and 525 <= posy <= 595:
                    game.choice[4] = (game.choice[4] + 1) % 2
                    game.draw_dice_button()

            # Roll dice (if rolls remaining)
            if 625 <= posx <= 1030 and 650 <= posy <= 775 and game.roll_counter <= 3:
                if game.roll_counter == 3:
                    pygame.draw.rect(game.screen, WHITE, (640, 425, 370, 220))
                    pygame.draw.rect(game.screen, BLACK, (625, 650, 405, 125))
                game.roll_dice()
                game.roll_counter += 1
                game.update_game()

            # Selection for upper board
            for i in range(6):
                if 445 <= posx <= (445+140) and (45 + i * 40) <= posy <= (75 + i * 40) and game.board[i + 1][0] is None:
                    game.board[i + 1][0] = game.board[i + 1][1]
                    game.choice = [1, 1, 1, 1, 1]
                    game.roll_counter = 1
                    game.clean_game()

            # For scoring more than one yahtzee
            if 445 <= posx <= (445+140) and (405 + 6 * 40) <= posy <= (440 + 6 * 40) and game.board[16][1] == 100:
                game.board[16][0] += game.board[16][1]
                game.board[16][1] = 0
                game.roll_counter = 4

                game.draw_grid()
                pygame.draw.rect(screen, BLACK, (625, 650, 405, 125))
                game.draw_dice()
                game.draw_current_score()
                game.draw_point_button(yahtzee=True)
                pygame.display.update()

            # Selection for lower board
            for i in range(7):
                if 445 <= posx <= (445+140) and (405 + i * 40) <= posy <= (440 + i * 40) and game.board[i + 10][0] is None:
                    game.board[i + 10][0] = game.board[i + 10][1]
                    game.choice = [1, 1, 1, 1, 1]
                    game.roll_counter = 1
                    game.clean_game()

            # Reset game
            if 930 <= posx <= 1050 and 0 <= posy <= 50:
                game.reset_game()

        # End of Game
        if counter == 18:

            # Update session high score
            if (game.ses_score is None) or (game.ses_score < game.board[19][0]):
                game.ses_score = game.board[19][0]

            # Read in all-time high score
            with open("score.txt", "r") as file:
                highscore = int(file.read())

            # Update all-time high score
            if game.board[19][0] > highscore:
                with open("score.txt", "w") as file:
                    file.write(str(game.board[19][0]))

            game.clean_game()

            game_over = True

            while game_over:
                pygame.draw.rect(screen, BLACK, (625, 650, 405, 125))
                label = font3.render("Play Again", True, WHITE)
                screen.blit(label, (650, 675))
                pygame.display.update()

                event = pygame.event.wait()

                # Checks for playing again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    if 625 <= posx <= 1030 and 650 <= posy <= 775:
                        game_over = False
                        game.reset_game()
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()


pygame.time.wait(300)
pygame.display.quit()
sys.exit()
