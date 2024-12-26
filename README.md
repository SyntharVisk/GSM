
# Green Shield Media

Green Shield Media project is a platform that allows users to track game developers, writers, directors, and other key contributors in the gaming industry, empowering users to discover trends in their gaming preferences and stay updated on projects by developers they admire.

## Features
- **Game History Integration**: Import game history from platforms like Steam or manually input games.
- **Developer Insights**: Explore profiles of game developers, writers, and directors.
- **Recommendations**: Receive game recommendations based on user preferences and developer trends.
- **Visualizations**: View trends and contributions through dynamic graphs and timelines.

## Tech Stack
- **Backend**: Python, Flask, Flask-SQLAlchemy
- **Frontend**: HTML (Templates for now, to be expanded with modern JS frameworks)
- **Database**: SQLite (for development, expandable to other DBMS)
- **Containerization**: Docker

## Cloning or Pulling the Repository

### Clone the Repository
To get a copy of the project on your local machine, use the following command:
    ```
    git clone https://github.com/your-username/GreenShieldMedia.git
    ```

## Setup Instructions

### Prerequisites
- Install Docker:
  - Visit [Docker's official website](https://www.docker.com/products/docker-desktop/) to download and install Docker Desktop for your platform (Windows, macOS, or Linux).
  - Alternatively, if you're using a Linux-based system, you can install Docker using the following commands:

    **For Ubuntu:**
    ```bash
    sudo apt-get update
    sudo apt-get install -y docker.io
    ```

    After installation, verify that Docker is installed by running:
    ```bash
    docker --version
    ```


### Directory Structure
```plaintext
GreenShieldMedia/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── main.py
│   ├── templates/
│   │   └── index.html
├── requirements.txt
├── Dockerfile
└── README.md
```

### Build and Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t greenshieldmedia .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 greenshieldmedia
   ```

3. Open your browser and navigate to `http://localhost:5000` to view the application.

## Application Overview
- **Flask Framework**: Backend framework used for serving web pages and managing API endpoints.
- **SQLite Database**: Stores data about games, developers, and user preferences.
- **Gunicorn**: Production WSGI server for running the Flask app.

## TODO / Future Implementation

### 1. User Accounts
- Implement a user authentication system to allow users to create accounts and securely log in.
- Enable users to save and manage their gaming preferences, tracked developers, and personalized recommendations.
- Include options for users to customize their dashboards and track progress across different devices.

### 2. Integration with Steam and Other Platforms
- Add functionality to link user accounts with gaming platforms like Steam, PlayStation, Xbox, and GOG.
- Automate the import of gaming history and achievements directly from linked platforms.
- Provide users with options to manually add games for unsupported platforms.

### 3. Web Page Design Enhancements
- Redesign the web pages for a more modern and interactive user experience.
- Incorporate:
  - Dark mode for better accessibility.
  - Dynamic elements, such as hover effects, sliders for preference weighting, and expandable sections.
- Include visualizations like graphs, timelines, and tiles for better insights into user preferences and developer trends.

### 4. Notifications and Updates
- Develop a notification system to inform users about:
  - New or upcoming games by developers they follow.
  - Updates to developer profiles or collaborations.

### 5. Community Features
- Enable users to contribute by updating developer profiles or flagging inaccuracies.
- Introduce community badges or rewards for active contributions.

---

These features are planned for future versions of the platform to enhance user engagement and broaden the functionality of Green Shield Media.


## Contributing
Feel free to fork this repository and submit pull requests for new features, bug fixes, or enhancements.

## License
This project is licensed under the MIT License.
