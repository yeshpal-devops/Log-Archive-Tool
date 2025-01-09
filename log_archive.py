#!/usr/bin/env python3

import os
import sys
import tarfile
from datetime import datetime

def compress_logs(log_directory, archive_directory):
    """
    Compress the logs in the given directory into a tar.gz file 
    and save it in the archive directory.
    """
    # Ensure the log directory exists
    if not os.path.isdir(log_directory):
        print(f"Error: The directory {log_directory} does not exist.")
        sys.exit(1)
    
    # Ensure the archive directory exists, create if not
    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)

    # Generate the archive name with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_directory, archive_name)

    try:
        # Create tar.gz archive
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(log_directory, arcname=os.path.basename(log_directory))
        print(f"Logs have been archived to {archive_path}")
        
        # Log the archive creation
        log_metadata(archive_directory, archive_name)

    except Exception as e:
        print(f"Error occurred while archiving logs: {e}")
        sys.exit(1)

def log_metadata(archive_directory, archive_name):
    """
    Log the creation date, time, and archive name in a metadata file.
    """
    log_file = os.path.join(archive_directory, "archive_log.txt")
    with open(log_file, "a") as log:
        log.write(f"{datetime.now().isoformat()} - Created archive: {archive_name}\n")
    print(f"Archive metadata logged in {log_file}")

def main():
    """
    Entry point for the script. Handles command-line arguments and starts the process.
    """
    if len(sys.argv) != 2:
        print("Usage: log-archive <log-directory>")
        sys.exit(1)

    log_directory = sys.argv[1]
    archive_directory = os.path.join(os.getcwd(), "log_archives")  # Default archive directory

    compress_logs(log_directory, archive_directory)

if __name__ == "__main__":
    main()
