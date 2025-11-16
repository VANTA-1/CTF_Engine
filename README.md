# CTF Engine

A simple, functional web-based Capture The Flag (CTF) engine built with Flask. This application allows users to register, log in, view challenges, and track their score. It is designed as a foundational project for learning web development and security concepts.

## Features

- User Authentication (Register, Login, Logout)
- Challenge Listing Page
- User Profile with Score Tracking
- Session Management with Flask-Login
- Database Integration with Flask-SQLAlchemy
- Production-ready deployment with Gunicorn

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite (for development)
- **Authentication:** Flask-Login
- **ORM:** SQLAlchemy
- **WSGI Server:** Gunicorn

## Setup and Installation

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- 
Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the
                              main subroutine, instead of logging them to
                              stderr.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment;
                              exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be
                              used up to 3 times (corresponding to WARNING,
                              ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring
                              library if user input is allowed. Specify which
                              mechanism to use [auto, disabled, import,
                              subprocess]. (default: auto)
  --proxy <proxy>             Specify a proxy in the form
                              scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted,
                              even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If
                              provided, overrides the default. See 'SSL
                              Certificate Verification' in pip documentation
                              for more information.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming
                              unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward
                              incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be
                              removed in the future. (Python's package installer)
- usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

### 1. Clone the Repository

Clone the project to your local machine:
```bash
git clone https://github.com/VANTA-1/CTF_Engine.git
cd CTF_Engine
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies

Install all required Python packages from the  file:
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

The application uses a database to store user and challenge information. Before running the app for the first time, you need to create the database tables and seed it with initial data.

Run the initialization script:
```bash
python scripts/deploy/init_db.py
```
This command will create a  file in your project directory and populate it with a test user and a sample challenge.

### 5. Run the Application

You can run the application in two ways:

- **Development Server (for testing):**
  ```bash
  python run.py
  ```
  The application will be available at .

- **Production Server (with Gunicorn):**
  ```bash
  gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app
  ```
  The application will be available at .

## Usage

1.  Open your web browser and navigate to the application's URL (e.g., ).
2.  Click on the "Register" link to create a new account.
3.  After registering, you will be automatically logged in.
4.  Navigate to the "Challenges" page to see the available challenges.
5.  Click the "Logout" link to end your session.

You can also log in with the pre-seeded test account:
- **Username:** 
- **Password:** 

## Project Structure

```
CTF_Engine/
├── app/
│   ├── __init__.py          # Application Factory
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes (login, register, logout)
│   │   └── main.py          # Main routes (index, profile, challenges)
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py        # Database models (User, Challenge)
│   └── templates/           # HTML templates
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       └── challenges.html
├── scripts/deploy/
│   └── init_db.py           # Database initialization script
├── venv/                    # Virtual environment directory (ignored by Git)
├── instance/                # Instance folder for database (ignored by Git)
├── ctf.db                   # SQLite database file (created by init_db.py)
├── requirements.txt         # Project dependencies
├── run.py                   # Development server runner
├── wsgi.py                  # Production WSGI entry point
└── README.md                # This file
```

## License

This project is open-source and available under the [MIT License](LICENSE).

## Future Improvements

- Implement challenge submission logic and flag verification.
- Add an admin panel for managing challenges and users.
- Integrate a more robust database like PostgreSQL.
- Add Docker support for containerized deployment.
