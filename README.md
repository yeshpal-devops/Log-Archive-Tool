# Log Archive Tool

A simple command-line tool to archive logs by compressing them into a `.tar.gz` file and storing them in a specified directory. The tool also logs metadata for each archive creation.

## Features
- Accepts log directory as input.
- Compresses logs into `.tar.gz` files.
- Stores archives in a new directory (`log_archives` by default).
- Logs archive metadata (date, time, archive name) in `archive_log.txt`.

## Usage

### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yeshpal-devops/Log-Archive-Tool.git
   cd log-archive
   
2. Install dependencies (if required):
   
    ```bash
    pip install -r requirements.txt
    ```

2. Running the Tool Run the script with the following command:

    ```bash
    python log_archive.py <log-directory>
    ```
    
Example:
   ```bash
    python log_archive.py <log-directory>
    ``

Steps to Use
Make the Script Executable:```bash
chmod +x log_archive.py
   ```
 
 Make the Script Executable:
   ```bash
 chmod +x log_archive.py
     
Run the Script:
   ```bash
    ./log_archive.py <log-directory>
```


Output

Archive files will be saved in the log_archives directory.

Metadata will be logged in log_archives/archive_log.txt.


Advanced Usage

You can customize the tool to:

Send email notifications.
Upload archives to a remote server or cloud storage.
Automate the process using schedulers like cron.


Contributing
Contributions are welcome! Please open an issue or submit a pull request.
