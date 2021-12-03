from django.db import models
from django.contrib.auth.models import User

class BoardGame(models.Model):
    """A board game the user can lend."""
    name = models.CharField(max_length = 200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    date_edited = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string presentation of the model."""
        return self.name

class Loan(models.Model):
    """Data about who is borrowing a specific board game."""
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow = models.BooleanField()

    def __str__(self):
        """Return a string presentation of the board game loan."""
        return f"{self.board_game} was borrowed {self.date_added}."