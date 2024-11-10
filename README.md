# Django API + Flet - Book Registration and Review System

This project is a web application developed with Django and Flet to manage a book registration and review system. The application includes a **Django-built API** and a graphical interface created with **Flet** to interact with the API data.

## Project Structure

- **Django API**: Backend developed with Django, responsible for providing a REST API for book registration, listing, and review.
- **Flet**: Graphical frontend that consumes the API, allowing users to register new books and submit reviews through a user-friendly interface.

## Features

- **Book Registration**: Allows adding new books, specifying the name and type (Amazon Kindle or Physical).
- **Book Listing**: Displays all registered books and enables navigation to each book's review page.
- **Book Review**: Allows users to give a rating and write a comment for each book.

## Technologies Used

- **Django**: Backend framework for building the API.
- **Django Ninja**: Library for quick and easy API creation in Django.
- **Flet**: Library for building graphical interfaces with Python.
- **Requests**: Library for making HTTP requests and consuming the API.
