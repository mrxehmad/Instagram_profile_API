# Instagram Profile Picture API

## Overview
This Python API enables users to retrieve an Instagram profile picture URL by providing a username. It is designed for simplicity and ease of integration into various applications. The API can be hosted for free on platforms like Heroku, making it accessible for developers seeking a lightweight solution.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/mrxehmad/Instagram_profile_API.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Instagram_profile_API
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```bash
    python app.py
    ```
2. Access the API at http://localhost:80/get_profile_pic with the following query parameter:
    - `username`: The Instagram username for which you want to retrieve the profile picture.
   
    Example:
    ```bash
    http://localhost:80/get_profile_pic?username=example_user
    ```

## Deployment on Heroku
1. Create a Heroku account and install the Heroku CLI.
2. Login to Heroku in the terminal:
    ```bash
    heroku login
    ```
3. Create a new Heroku app:
    ```bash
    heroku create
    ```
4. Deploy the application to Heroku:
    ```bash
    git push heroku master
    ```
5. Open the deployed app in the browser:
    ```bash
    heroku open
    ```

## Contributing
Contributions are welcome! Feel free to open issues or pull requests for improvements or additional features.

## License
This project is licensed under the MIT License.
