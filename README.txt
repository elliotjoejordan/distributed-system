READ ME

To run, the programs require pyro4. Use 'pip3 install Pyro4' or equivalent.

To run the system, first launch in terminal the frontEnd.py in python 3.
Subsequently launch the servers, running in separate terminal windows 'python3 server.py'.
It is required that each server be ran from the separate directories, as each server.py file is unique.

Once the back end and frontend are running, launch client.py in a separate terminal. 

Client is prompted for commands, and cannot progress unless 'CONN' is entered.

Once connected, commands are requested from the client and processed by the frontend, utilising one or many of the back end servers. This process continues even when a server fails.

One server at least must be running.

'QUIT' closes the client and breaks the connection.

Relaunching the client and entering 'CONN' re-establishes the connection.