import tkinter as tk
from tkinter import messagebox
from UNO_GAME import Deck, Hand, Card, choose_first, win_check, single_card_check

# Initialize the game
def start_game():
    global deck, players, top_card, turn
    deck = Deck()
    deck.shuffle()
    players = [Hand() for _ in range(4)]
    for player in players:
        for _ in range(7):
            player.add_card(deck.deal())
    top_card = deck.deal()
    while top_card.cardtype != 'number':
        top_card = deck.deal()
    turn = choose_first()
    update_game_status()

# Draw a card
def draw_card(player_index):
    global turn
    if deck.deck:
        card = deck.deal()
        players[player_index].add_card(card)
        if win_check(players[player_index]):
            messagebox.showinfo("UNO Game", f"Player {player_index + 1} won!")
            return
        turn = (turn + 1) % 4
        update_game_status()
    else:
        messagebox.showinfo("UNO Game", "No more cards in the deck.")

# Play a card
def play_card(player_index, card_index):
    global turn, top_card
    card = players[player_index].single_card(card_index)
    if single_card_check(top_card, card):
        if card.cardtype == 'number':
            top_card = players[player_index].remove_card(card_index)
            if win_check(players[player_index]):
                messagebox.showinfo("UNO Game", f"Player {player_index + 1} won!")
                return
            turn = (turn + 1) % 4
        else:
            # Handle action cards
            # Code to handle action cards goes here
            pass
        update_game_status()
    else:
        messagebox.showinfo("UNO Game", "This card cannot be used.")

# Update game status
def update_game_status():
    game_status_label.config(text=f"Top card is: {top_card}\nPlayer 1's cards:\n{players[0].cards_in_hand()}")

# Initialize Tkinter window
root = tk.Tk()
root.title("UNO Game")

# Create game status label
game_status_label = tk.Label(root, text="")
game_status_label.pack()

# Create buttons for manual player
manual_player_button_frame = tk.Frame(root)
manual_player_button_frame.pack()

draw_card_button = tk.Button(manual_player_button_frame, text="Draw a Card", command=lambda: draw_card(0))
draw_card_button.grid(row=0, column=0)

play_card_buttons = []
for i in range(7):
    button = tk.Button(manual_player_button_frame, text=f"Play Card {i + 1}", command=lambda idx=i: play_card(0, idx))
    button.grid(row=0, column=i + 1)
    play_card_buttons.append(button)

# Start the game
start_game()

# Run the Tkinter event loop
root.mainloop()
