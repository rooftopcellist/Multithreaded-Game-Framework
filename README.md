# Multithreaded-Game-Framework
This provides a multithreaded server, client, and game logic programs.  
The next iteration of this should include a GUI for the server's text output to each client.  
This will be included in the client program.  



1. gameServer.py listens for, accepts, starts a thread for, and stores the name and class of each client.  Each client thread then listens for input from each client, then sends that input to the gameLogic.py.  The output of gameLogic.py is sent to all clients by cycling through a global clientList.  The server can also send messages to individual clients by indexing the client in clientList.  
2. gameClient.py connects to the server, prompts the user for a name and to choose a class.  It also starts two threads: One to listen for messages for the gameServer and the other is waiting for input from the client to send to the server.  
3. gameLogic.py contains all of the relevant game logic.  
4. gameLog.py is a small module for packaging the message to be sent to the clients from gameServer.
5. fighter.py contains all the user classes (Wizard, Archer, Knight, Rat, etc.) and is imported into gameLogic.py as a module. 
