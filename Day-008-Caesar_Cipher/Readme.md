# Day 8 - Caesar Cipher Project

## Project Overview
The Caesar Cipher is a simple encryption program that shifts letters in a message based on user input shift number. It works by moving each letter forward or backward in the alphabet by a set number of places as per user input direction(encode or decode) and encrypt and decrypt a message,This project helps me understand the basic understanding of encryption concepts by using pythong.

## What I have learned
- functions with input: Functions with input allow you to pass data (called parameters or arguments) into a function. This helps the function perform tasks using dynamic values instead of fixed ones.
- Positional arguement: A positional argument is an argument passed to a function in the correct order. The position of the value determines which parameter it is assigned to which parameter.
-  Keyword arguement: A keyword argument is an argument passed to a function using the parameter name, so the order does not matter. You specify which parameter the value belongs to.

## How It Works
- The user provides three inputs: **Direction** (encode or decode), **Shift** (number of positions to move), and **Text** (the message to encrypt or decrypt).
- If "encode" is selected, the program shifts letters forward; if "decode" is selected, it shifts letters backward.
- The program keeps running until the user decides to exit.
- After each encryption or decryption, the user gets a prompt: *The user is prompted to decide whether to continue or exit the program.*

## Code Highlights
- Used Python’s `index()` function to find a letter’s position in the alphabet.
- Explored **positional arguments** and **keyword arguments** to improve function flexibility.
- Learned how to use the **modulo operator** to shift a letter after it reaches the last index in a list.

This project was a great way to practice working with functions, loops, and string manipulation while learning how simple ciphers work!

