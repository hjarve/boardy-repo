from django.db import models
from django.db.models.deletion import CASCADE

class BoardGame(models.Model):
    """A board game the user can lend."""
    name = models.CharField(max_length = 200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    # add later who owns the game

    def __str__(self):
        """Return a string presentation of the model."""
        return self.name

class Loan(models.Model):
    """Data about who is borrowing a specific board game."""
    board_game = models.ForeignKey(BoardGame, on_delete=CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    # Add later who borrowed the game
    # Boolean value "borrowed"?

    def __str__(self):
        """Return a string presentation of the board game loan."""
        return f"{self.board_game} was borrowed {self.date_added}."