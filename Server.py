"""Server Script for multithreaded chat application for two clients"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import asyncio
import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import sqlite3

app = FastAPI()

clients = []  # Store connected clients
public_keys = {}  # Store client public keys
messages = []  # Store chat messages

# Generate RSA key pair (for the server)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Convert public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        # Send server's public key to client
        await websocket.send_text(json.dumps({"type": "public_key", "data": public_pem}))

        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            if message["type"] == "public_key":
                public_keys[websocket] = message["data"]

            elif message["type"] == "message":
                encrypted_msg = message["data"]
                sender = message["sender"]

                messages.append({"sender": sender, "message": encrypted_msg})

                # Broadcast encrypted message
                for client in clients:
                    if client != websocket:
                        await client.send_text(json.dumps({
                            "type": "message",
                            "sender": sender,
                            "data": encrypted_msg
                        }))
    except WebSocketDisconnect:
        clients.remove(websocket)


