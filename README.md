Animal Tracking System

This project is a desktop application that enables the management and tracking of animals using QR codes. Built with the PyQt5 library, it uses an SQLite database and offers functionalities such as generating and reading QR codes, adding, updating, and listing animal information.

Features

Add and Update Animals: Easily add and update animal details (species, gender, birth date, weight, health status, etc.).

Generate QR Codes: Create unique QR codes for each animal.

Read QR Codes: Update location by reading QR codes from a camera or file.

Animal Listing: List animals with filters like indoor/outdoor or male/female.

Graphical Interface: Perform actions quickly and easily with a user-friendly interface.

Required Libraries

The following Python libraries are needed to run the project:

PyQt5

sqlite3 (comes with Python)

numpy

opencv-python

pyzbar

qrcode

Install the libraries using:

pip install PyQt5 numpy opencv-python pyzbar qrcode

Project Structure

HomePage: Main interface where animals are listed and filtered.

AddAnimal: Window for adding new animals.

AnimalDetails: Window for viewing animal details and handling QR code operations.

Database: SQLite database used for storing animal information.

QR Code Operations: Functions for generating and reading QR codes.

Usage

1. Start the Application

Run the following command to start the application:

python main.py

2. Using the Main Interface

Add New Animal: Click the "Add Animal" button to add a new animal.

View Animal Details: Select an animal from the list to view and update its details.

Read QR Codes: Update the animal's location by reading a QR code from the camera or a file.

3. Filtering

List indoor or outdoor animals using the relevant filter options.

Use the filter options to view male or female animals separately.

Contribution

This is an open-source project. To contribute:

Fork this repository.

Make your changes and commit them.

Create a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more information.
