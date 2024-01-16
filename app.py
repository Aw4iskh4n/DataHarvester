import subprocess
import os
import json
import shutil
import logging
from browserhistory import get_browserhistory

# Setup logging
logging.basicConfig(filename='data_export.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directory for exported data
output_dir = "exported_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to export Windows Event Logs
def export_event_logs():
    try:
        log_names = subprocess.check_output(["wevtutil", "el"]).decode().split('\n')
        for log_name in log_names:
            filename = os.path.join(output_dir, f"{log_name}.txt").replace(' ', '_').replace('\\', '_')
            with open(filename, 'w') as f:
                subprocess.call(["wevtutil", "qe", log_name, "/f:text"], stdout=f)
        logging.info("Windows Event Logs exported successfully.")
    except Exception as e:
        logging.error(f"Error exporting Windows Event Logs: {e}")




# Function to get Recent Documents
def export_recent_documents():
    try:
        recent_path = os.path.expandvars(r'%AppData%\Microsoft\Windows\Recent')
        with open(os.path.join(output_dir, 'recent_documents.txt'), 'w') as f:
            for file in os.listdir(recent_path):
                f.write(file + '\n')
        logging.info("Recent documents exported successfully.")
    except Exception as e:
        logging.error(f"Error exporting recent documents: {e}")

# Function to get Browser History
def export_browser_history():
    try:
        history_dict = get_browserhistory()
        with open(os.path.join(output_dir, 'browser_history.txt'), 'w') as f:
            json.dump(history_dict, f, indent=4)
        logging.info("Browser history exported successfully.")
    except Exception as e:
        logging.error(f"Error exporting browser history: {e}")

# Function to get NirSoft LastActivityView data
def export_lastactivityview():
    try:
        subprocess.call(['LastActivityView.exe', '/sjson', os.path.join(output_dir, 'lastactivityview_data.txt')])
        logging.info("NirSoft LastActivityView data exported successfully.")
    except Exception as e:
        logging.error(f"Error exporting NirSoft LastActivityView data: {e}")

# Function to get Sysinternals Process Monitor data
def export_process_monitor_data():
    try:
        subprocess.call(['Procmon.exe', '/OpenLog', 'ProcessMonitor.pml', '/SaveAs', os.path.join(output_dir, 'process_monitor_data.txt')])
        logging.info("Sysinternals Process Monitor data exported successfully.")
    except Exception as e:
        logging.error(f"Error exporting Sysinternals Process Monitor data: {e}")

# Function to run PowerShell commands
def run_powershell_commands():
    try:
        powershell_commands = [
            'Get-WinEvent -ListLog * | Format-Table -AutoSize',
            'Get-Process | Format-Table -AutoSize',
            # Add more PowerShell commands as needed
        ]
        for cmd in powershell_commands:
            output_file = cmd.split()[0] + '.txt'
            subprocess.call(["powershell", "-Command", cmd], stdout=open(os.path.join(output_dir, output_file), 'w'))
        logging.info("PowerShell commands executed successfully.")
    except Exception as e:
        logging.error(f"Error running PowerShell commands: {e}")

# Function to export Task Scheduler data
def export_task_scheduler():
    try:
        subprocess.call(['schtasks', '/query', '/fo', 'LIST'], stdout=open(os.path.join(output_dir, 'task_scheduler.txt'), 'w'))
        logging.info("Task Scheduler data exported successfully.")
    except Exception as e:
        logging.error(f"Error exporting Task Scheduler data: {e}")

# Main function to execute all exports
def main():
    logging.info("Starting data export process.")
    export_event_logs()
    export_recent_documents()
    export_browser_history()
    export_lastactivityview()
    export_process_monitor_data()
    run_powershell_commands()
    export_task_scheduler()
    logging.info("Data export process completed.")

if __name__ == "__main__":
    main()
