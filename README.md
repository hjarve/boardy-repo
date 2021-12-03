# boardy-repo
An app where users can borrow each other's board games.  

boardy is the project folder.  
board_games is the app folder that contains the functionalities of board games and borrowing the games.  
 -Homepage: view: index(request), template: index.html  
 -Board games page: shows all board games. view: board_games(request), template: board_games.html  
 -Page of a specific board game and where the board game can be borrowed: view: board_game(request, board_game_id), template: board_game.html  
 -Page for adding a new board game: view: new_board_game(request), template: new_board_game.html 
 -Page for editing a board game: view: edit_board_game(request, board_game_id), template: edit_board_game.html   
 -User page; where user's board games and loans are shown: view: user_page(request): template: user_page.html  
  
users app contains the functionality related to users  
 -login and logout default urls and views,templates: login.html and logged_out.html  
 -Registration page: view: register(request), template: register.html  
