
# SysDataHarvester 

## Introduction
SysDataHarvester is a Python-based tool designed for harvesting system data on Windows platforms. It gathers a variety of information, including Windows Event Logs, recent documents, browser history, NirSoft LastActivityView data, Sysinternals Process Monitor data, PowerShell command output, and Task Scheduler data.

## Installation

### Prerequisites
- Python 3.x
- `browserhistory` Python package
- Access to Windows system tools and NirSoft's LastActivityView

### Steps
1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install the `browserhistory` package using pip:
   ```
   pip install browserhistory
   ```
3. Ensure that NirSoft's LastActivityView and Sysinternals Process Monitor are available on the system.

## Running SysDataHarvester

### Steps
1. Clone or download the SysDataHarvester script from the repository.
2. Open a command prompt or terminal.
3. Navigate to the directory containing the script.
4. Run the script:
   ```
   python SysDataHarvester.py
   ```

## Functionality

### Export Event Logs
Extracts Windows Event Logs and saves them as text files.

### Export Recent Documents
Lists recent documents accessed on the system.

### Export Browser History
Collects browsing history from installed browsers.

### Export LastActivityView Data
Gathers system activity data using NirSoft's LastActivityView.

### Export Process Monitor Data
Extracts data from Sysinternals Process Monitor.

### Run PowerShell Commands
Executes specified PowerShell commands and captures their output.

### Export Task Scheduler Data
Exports data from the Windows Task Scheduler.

## Logging
SysDataHarvester logs its operation details in `data_export.log`, providing timestamps and status information for each operation.

---

Note: Ensure proper permissions and system access for the tool to function effectively.
