# science2service-management-workshop
Science2Service week, Data Management training


## Usage

Kickstart your own Python environment with the following commands.

1. Install `python3-venv` package if you don't have it from before.
    ```bash
    sudo apt-get install -y python3-venv
    ```
0. Create your Python virtual environment.
    ```bash
    python3 -m venv ~/v/dataman
    ```
0. Source your Python virtual environment. **PS!** Do this in every new terminal window you want to use this virtual environment.
    ```bash
    source ~/v/dataman/bin/activate
    ```
0. Install Python wheel package for downloading python pre-compiled libraries.
   ```bash
   pip3 install wheel
   ```
0. Clone this Git-repository.
    ```bash
    git clone https://github.com/metno/science2service-data-management.git
    ```
0. Enter the Git-repository.
    ```bash
    cd science2service-data-management
    ```
0. Install this workshops Python requirements in your own environment.
    ```bash
    pip3 install -r requirements.txt
    ```

<!---
vim: set spell spelllang=en:
-->
