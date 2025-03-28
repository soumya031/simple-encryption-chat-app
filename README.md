# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)


**Title: Creating encrypted chat between two clients.**

## 1. Introduction
In the modern digital era, secure communication is a critical requirement. This project implements an encrypted chat system that ensures confidentiality, integrity, and authenticity between two clients. The chat uses a hybrid encryption mechanism combining RSA for key exchange and AES for message encryption.

## 2. Objectives
- To develop a real-time chat application with end-to-end encryption.
- To implement RSA for secure key exchange.
- To use AES for encrypting and decrypting chat messages.
- To ensure seamless and secure communication between two clients over a server.

## 3. System Architecture
The system comprises three main components:
1. **Server (Server.py)**: Handles client connections and message forwarding.
2. **Client 1 (client_1.py)**: First user participating in encrypted chat.
3. **Client 2 (client_2.py)**: Second user participating in encrypted chat.
4. **Encryption Module (RSA.py)**: Manages key generation, encryption, and decryption.

## 4. Encryption Mechanism
### **4.1 RSA (Rivest-Shamir-Adleman) for Key Exchange**
- Each client generates a pair of RSA keys (public and private).
- The public key is shared with the other client through the server.
- The private key remains confidential and is used for decrypting exchanged keys.

### **4.2 AES (Advanced Encryption Standard) for Message Encryption**
- A symmetric AES key is generated and encrypted using RSA.
- Messages are encrypted using AES before transmission.
- The recipient decrypts the AES-encrypted message using the shared AES key.

## 5. Implementation
### **5.1 Server Implementation**
- The server runs a multi-client socket-based application.
- It listens for connections, receives messages, and forwards them securely.

### **5.2 Client Implementation**
- Each client connects to the server and exchanges RSA keys.
- Messages are encrypted using AES before transmission.
- Upon receiving a message, the client decrypts it using AES.

## 6. Code Files
- **Server.py**: Handles client connections and message forwarding.
- **client_1.py & client_2.py**: Implement encrypted messaging logic.
- **RSA.py**: Manages RSA key generation, encryption, and decryption.

## 7. Results
- Successfully established a secure chat channel between two clients.
- Messages exchanged were encrypted, preventing unauthorized access.
- The hybrid encryption approach ensured high security without compromising performance.

## 8. Future Enhancements
- Implement a **Graphical User Interface (GUI)** for improved user experience.
- Add support for **multiple users** with individual encryption keys.
- Integrate **end-to-end authentication** using digital signatures.
- Deploy the chat application over **a secure cloud environment**.

## 9. Conclusion
This project successfully demonstrates a secure chat application using hybrid encryption. By integrating RSA for key exchange and AES for secure message transmission, the system ensures encrypted communication between two users.

---
**Project Developed By: [Soumyadip Saha]**


