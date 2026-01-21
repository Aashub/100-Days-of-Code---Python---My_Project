# Day 37 – Habit tracker

## Project Overview

This project is a Habit Tracking built using Python and the Pixela API. The project allows users to track daily habits (such as cycling distance) by creating a Pixela user account, generating graphs, and posting daily progress data. In order to build this proejct i learned about how to interact with REST APIs using different HTTP methods like POST, PUT, and DELETE to create, update, and remove data on a server. This project mainly focuses on understanding HTTP requests, API authentication.

## What I Have Learned

* **HTTP Methods (POST, PUT, DELETE)**: Learned how POST is used to create data, PUT to update existing data, and DELETE to remove data from a server.

* **API Authentication**: Learned how to send API tokens securely using API authentication, where a unique API token is sent in the request header (X-USER-TOKEN). This allows the Pixela server to verify my identity, authorize the request, and permit actions such as creating, updating, or deleting habit-tracking data.

## How It Works

* **User Creation (POST Request)**: The program sends a POST request to the Pixela API to create a new user by providing a username, token, and agreement details.

* **Graph Creation (POST Request)**: A graph is created for tracking daily cycling distance by sending graph configuration data such as unit, type, and color.

* **Pixel Creation (POST Request)**: The user asked inputs how many km he has cycled for the current day. This data is sent as a POST request to record the daily habit entry on the graph.

* **Pixel Update (PUT Request)**: If required, an existing pixel (habit entry) can be updated using a PUT request by modifying the quantity for a specific date.

* **Pixel Deletion (DELETE Request)**: The program can also delete a previously added pixel using a DELETE request for a given date.

## Project Highlights

* Learned how to do advance authentification using request header.
* Learned how to create, update, and delete server-side data.