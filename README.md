# FlatMates

FlatMates is a web application designed to help flatmates manage shared living spaces efficiently. It provides features for organizing tasks, managing expenses, and enhancing communication among flatmates.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Node.js and npm installed
- Git installed
- SQLite or another database system (if not using SQLite)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/PrettyNeet/FlatMates.git
   ```

2. Change directory to the project folder:

   ```bash
   cd FlatMates
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Change directory to the frontend folder:

   ```bash
   cd flatmates-frontend
   ```

7. Install frontend dependencies:

   ```bash
   npm install
   ```

## Usage

### Running the Application

To run the application locally, follow these steps:

1. In the `flatmates-frontend` directory, start the React development server:

   ```bash
   npm start
   ```

2. In the root directory (where `mainapp.py` is located), start the Flask application:

   ```bash
   python mainapp.py
   ```

3. Access the application in your web browser at `http://localhost:3000`.

### Features

- **User Registration and Login**: Users can create accounts and log in securely.

- **Task Management**: Flatmates can create and assign tasks, helping to distribute responsibilities.

- **Expense Tracking**: Keep track of shared expenses and who owes what to whom.

- **Communication**: Built-in messaging for easy communication between flatmates.

## Contributing

We welcome contributions from the community. If you would like to contribute to the project, please follow our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the open-source community for providing valuable tools and libraries.
- Inspired by the need for efficient flatmate management.
```

Feel free to replace the placeholders like `https://github.com/PrettyNeet/FlatMates.git` with the actual URLs and customize the content to match your project's specific details. Additionally, consider adding a "Contributing" section with guidelines for contributors if you plan to have an open-source project.