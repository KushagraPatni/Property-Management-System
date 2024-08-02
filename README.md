It is a Blockchain-based application designed to manage property transactions using digital currency. This system facilitates secure and transparent property trading through blockchain technology, ensuring data integrity with cryptographic methods like HMAC , hash functions and Merkle trees and consensus algorithms like proof of work.



Steps to run

- default.py contains some default properties and users for the purpose of testing, more users and properties may be registered by choosing appropriate options in menu

- Menu has options for various operations that may be carried out as part of the functioning of a real estate management system.



Details About Contents of files


1. block.py: Blockchain Management

- Class BlockChain:
Manages the entire blockchain, maintaining a list of blocks and transactions.

- new_block(self, previous_hash=None, transaction=None):
Creates a new block with transactions, assigns a Merkle root, and computes the block's hash.
previous_hash: The hash of the previous block in the chain.
transaction: Optional transaction details to include in the block.

- hash(block):
Computes and returns a SHA-256 hash of the block.
block: The block data to hash.

- last_block(self):
Returns the most recent block in the blockchain.

- get_block(self, index):
Retrieves a block by its index in the chain.

- get_chain(self):
Returns the entire blockchain as a list of blocks.

- get_transaction_by_user(self, username):
Returns all transactions in which user with username was involved

- mine_block_POW(self , block):
Proof of work Consensus to verify the transaction block before adding it to the chain

- is_chain_valid(self):
Check if chain has been tampered by computing and comparing hashes of blocks with prev hash of next block



2. hmac_.py: Security

Contains utilities to implement HMAC for securing transactions. It provides functions to generate and verify HMACs ensuring the authenticity and integrity of messages.



3. main.py: Main Application Entry

Serves as the entry point for running the application.
Initializes the blockchain and handles user interactions such as registering users, adding properties, and processing transactions.



4. merkle_tree.py: Merkle Tree Implementation

- Class MerkleTree:
Implements a Merkle tree to summarize and verify transaction data efficiently.

- getRootHash():
Calculates and returns the root hash of the Merkle tree, representing a summary of all transactions.



5. models.py: Data Models

- Class User:
Represents a user in the system with attributes like username, password, assets, and digital wealth.

    - add_property(self, property):
    Registers a new property to the user's list of assets.

    - remove_property(self, property):
    Removes a property from the user's assets and adjusts their digital wealth accordingly.

    - register_property(self, property):
    List a property as a user and set name , price

    - addMoney(self, amount):
    Add money to wallet , check balance

- Class Transaction:
Handles the logic for buying and selling properties between users.

    - to_string(self):
    Returns a string representation of the transaction details.

- Class Property:
Represents a property with attributes like name, owner, and value.

    - viewProperties(self):
    View All Listed properties with details

    -getProperty
    get details of a specific property




GROUP DETAILS -

Aryan Saluja	            2021A7PS2947H
Kushagra Patni	            2021A3PS2985H
Shreya Kumar	            2021A7PS1508H
Varayuru Pranava Sukrutha	2020A8PS0695H
Divyank Shrivastav 	        2020A1PS2187H
