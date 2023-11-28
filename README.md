# Team Members

A simple team-member management application that allows the user to view, edit, add, and delete team members.

## Getting Started

Follow these steps to set up and run the project locally.

### Installation

1. **Install Virtualenv:**

    ```bash
    pip3 install virtualenv
    ```

2. **Clone the Repository:**

    ```bash
    git clone https://github.com/GaganRajSingh/Team-member.git
    ```

3. **Navigate Inside the Folder:**

    ```bash
    cd Team-member
    ```

4. **Create a Virtual Environment:**

    ```bash
    virtualenv venv
    ```

5. **Activate the Virtual Environment:**

    On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

6. **Install Dependencies:**

    ```bash
    pip3 install -r requirements.txt
    ```

### Running the Server

7. **Run Migrations:**
    
    ```bash
    python3 manage.py migrate
    ```

8. **Run the Server:**

    ```bash
    python3 manage.py runserver
    ```

    Your server should now be running. Navigate to [http://127.0.0.1:8000/member](http://127.0.0.1:8000/member) to use the application.

### Deactivate the Virtual Environment

9. **Deactivate the Virtual Environment:**

    ```bash
    deactivate
    ```
