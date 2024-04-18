# UDP Client-Server Communication

This repository contains simple implementations of a UDP client and server in Python, developed as a part of the ICSR30 course. The aim of this project is to understand the basic functioning of the UDP protocol and compare it with the services that TCP provides to the application layer.

## Project Overview

The project involves creating a simplified UDP server based on a "Hello World" UDP server and client code. The server receives data, processes it (replaces HTTP with a custom protocol), and sends a requested file to the client. The file is divided into chunks of a specified buffer size. The client requests a file, receives it, assembles it, and checks it using checksums.

## Files

- `server.py`: This is the server script. It listens for incoming messages from clients, processes the requests, and sends the requested file data in chunks.
- `client.py`: This is the client script. It sends a user-input message to the server to request a file, receives the file data in chunks, assembles it, and checks it using checksums.

## Usage

1. Run the server script: `python server.py`
2. In a separate terminal, run the client script: `python client.py`
3. When prompted, enter a message in the client terminal. This message will be sent to the server.
4. The server will process the request, send the requested file data, and the client will receive and assemble the file data.

## Requirements

- Python 3.x
- A network connection between the client and server

## Note

This is a simple implementation meant for educational purposes. It is assumed that the client and server are running on the same machine (localhost). If they are on different machines, the IP address in the client script needs to be updated accordingly.
