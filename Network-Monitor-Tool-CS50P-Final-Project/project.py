# === Standard Library ==== #
import os
import sys
import platform
import threading
import socket
import subprocess
import re
import ssl
import time as TIME
from datetime import datetime, timedelta, timezone

# ==== Third-Party Libraries === #
from colorama import init, Fore, Style
import requests
from bs4 import BeautifulSoup
import speedtest
import whois
import schedule
import pyttsx3
import sqlite3
from prettytable import PrettyTable
from fpdf import FPDF
import pydoc
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import PIL.Image
import tempfile


# ====================== Main Application ===================== #
def main():
    # create the database for API token
    creat_token_table()
    # check if there is a valid API tooken
    valid_api_tooken()
    # create database fro test history
    creat_table()
    # lunch the app cli insterface 
    run_cli()

def run_cli():
    show_dashboard()

    while True:
        try:
            cmd = input(Fore.BLUE + "\nNetwork Monitor (For commands list, type help) >>> " + Style.RESET_ALL).strip().lower()
            
            if cmd == "exit" or cmd == "xt":
                print("\n👋 Exiting NetSage CLI. See you!\n")
                break
            elif cmd == "help":
                clear_terminal()
                command_list()

            elif cmd == "speed-test" or cmd == "st":
                clear_terminal()
                run_speed_cli()

            elif cmd == "auto-test" or cmd == "at":
                clear_terminal()
                run_auto_test()    

            elif cmd == "status" or cmd == "stts":
                clear_terminal()
                internet_stat()

            elif cmd == "compare-global" or cmd == "cg":
                clear_terminal()
                compare_global()

            elif cmd == "signal" or cmd == "sgnl":
                clear_terminal()
                signal_qulty()

            elif cmd == "isp":
                clear_terminal()
                isp_info() 

            elif cmd == "url-info" or cmd == "url":
                clear_terminal()
                url_info()

            elif cmd == "table-history" or cmd == "th":
                clear_terminal()
                show_table()

            elif cmd == "graph-history" or cmd == "gh": 
                clear_terminal()   
                show_graph()

            elif cmd == "export" or cmd == "xprt":
                clear_terminal()
                export_logs()

            elif cmd == "delet" or cmd == "dlt":
                clear_terminal()
                delet_data()

            else:
                print(Fore.RED + "❌ Unknown command." + Style.RESET_ALL + "Type 'help' to see available options.")
            
        except KeyboardInterrupt:
            print("\n👋 Exiting NetSage CLI. See you!\n")
            break

# +++++++++++++++ Utility Functions ++++++++++++++++++ #

# Check whether the value is a list or a datetime, and convert everything to a string for safe printing.
def format_date(value):

    if isinstance(value, list):
        for dt in value:        
            if isinstance(dt, datetime):
                return dt.strftime("%Y-%m-%d %H:%M:%S") 
            else:
                return str(dt)
    elif isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    elif value is None:
        return "N/A"
    else:
        return str(value)
     
# Running animation
def spinner(message, running_flag):
    i = 0
    dots = ["⏳", "⏳.", "⏳..", "⏳...", "⏳...."]
    while running_flag[0]:  # using list for mutability
        sys.stdout.write(f"\r-- {message} {dots[i % len(dots)]}")
        sys.stdout.flush()
        i += 1
        TIME.sleep(0.6)

# Clear the terminal
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Check if digit or float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Gives thye filter date range 
def filter_date():

    print(Fore.CYAN + "\n🕓 Choose the test history range:\n" + Style.RESET_ALL)
    print("  1️⃣  Last 24 Hours")
    print("  2️⃣  Last 7 Days")
    print("  3️⃣  Last 30 Days")
    print("  4️⃣  Show All Data\n")

    choice = input(Fore.YELLOW + "⏱️  Enter your choice (1–4) >> " + Style.RESET_ALL).strip()
    print("")  # Spacer line
    
    range_type = None

    if choice == "1":
        range_type = "24h"
    elif choice == "2":
        range_type = "7d"
    elif choice == "3":
        range_type = "30d"
    else:
        range_type = "all"
    
    return range_type

# Validate API tooken

TOKEN = None

def valid_api_tooken(gui=False):

    global TOKEN

    if TOKEN is None:
        token = get_token()
        if token:
            TOKEN = token
            
        else:
            while True:
                    if gui:
                        pass

                    else:
                        try:
                            print("In order to use the ISP and Location feature, you need to get a free API token from ipinfo.io")
                            user_token = input("Enter the API token (or press Enter to skip): ").strip()

                            if user_token:
                                # checking if the tooken is valid
                                print("🔄 Validating the API token...")
                                TOKEN = user_token
                                try:
                                    response = requests.get(f"https://ipinfo.io/json?token={TOKEN}")
                                    if response.status_code != 200:
                                        print(Fore.RED + "❌ Invalid API token." + Style.RESET_ALL)
                                        TOKEN = None
                                    else:
                                        print(Fore.GREEN + "✔ API token set successfully." + Style.RESET_ALL)
                                        service = "ipinfo.io"
                                        # Save it to db
                                        save_token_to_db((TOKEN, service))
                                        break
                                
                                except Exception as e:
                                    print(Fore.RED + f"❌ Error validating API token: {e}. The ISP and Location feature will be disabled." + Style.RESET_ALL)
                                    TOKEN = None
                            else:
                                print("⚠️  No API token provided. The ISP and Location feature will be disabled❗")
                                TOKEN = None
                                break
                        except KeyboardInterrupt:
                            print("The ISP and Location feature will be disabled.")
                            break

# ====================== Dashboard Components ================ #

def show_dashboard():
    now = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    hostname = socket.gethostname()
    version = "v1.0.0"

    print(Style.BRIGHT + Fore.CYAN + "\n" + "═" * 70)
    print(Fore.MAGENTA + "📡  NetSage CLI – Your Network Monitoring Assistant".center(70))
    print(Fore.CYAN + "═" * 70 + Style.RESET_ALL)

    print(Fore.LIGHTBLACK_EX + f"🖥️  Host: {hostname}    📅  {now}     🧩 Version: {version}" + Style.RESET_ALL)
    # show commands 
    command_list()
    
    print(Fore.CYAN + "\n💡 Tip: Type " + Style.BRIGHT + "'help'" + Style.NORMAL + " at any time to redisplay this dashboard.")
    print("════════════════════════════════════════════════════════════════════\n" + Style.RESET_ALL)

def command_list():
    print(Fore.YELLOW + "\n🧭  Available Commands:\n")

    print(Fore.GREEN + "  speed-test      / st   " + Fore.WHITE + "- Run network speed test")
    print(Fore.GREEN + "  auto-test       / at   " + Fore.WHITE + "- Run automatic speed tests every X seconds")
    print(Fore.GREEN + "  status          / stts " + Fore.WHITE + "- Live internet status")
    print(Fore.GREEN + "  compare-global  / cg   " + Fore.WHITE + "- Compare your speed to global average")
    print(Fore.GREEN + "  signal          / sgnl " + Fore.WHITE + "- Wi-Fi strength + troubleshooting tips")
    print(Fore.GREEN + "  isp                    " + Fore.WHITE + "- Show ISP & location info")
    print(Fore.GREEN + "  url-info        / url  " + Fore.WHITE + "- Get info about a website or URL")
    print(Fore.GREEN + "  table-history   / th   " + Fore.WHITE + "- Show past results in a table")
    print(Fore.GREEN + "  graph-history   / gh   " + Fore.WHITE + "- Show past results as graph")
    print(Fore.GREEN + "  export          / xprt " + Fore.WHITE + "- Export logs to PDF")
    print(Fore.GREEN + "  delet           / dlt  " + Fore.WHITE + "- Delete all saved test history")
    print(Fore.GREEN + "  exit or Ctrl+C  / xt   " + Fore.WHITE + "- Exit the application")

# ===================================== Feature Callers =============================================== #

def run_speed_cli():
    print(Fore.MAGENTA + "\n🚀 NetSage: Internet Speed Test.\n" \
                        "═════════════════════════════════════════════\n" + Style.RESET_ALL)
    
    running = [True]
    thread = threading.Thread(target=spinner, args=("⚡ Testing Internet Speed", running))

    results = None
    try:
        thread.start()
        results = check_speed()
    finally:
        running[0] = False
        thread.join()

        print()  # Add spacing

        if results is not None:
            if "Error" in results:
                print(Fore.RED + "\n❌ Failed to run the speed test!" + Style.RESET_ALL)
                print(Fore.YELLOW + f"\nError: {results['Error']}\n" + Style.RESET_ALL)
            else:
                print(Fore.MAGENTA + "\n📡 NetSage Speed Report\n" \
                                "════════════════════════════════════" + Style.RESET_ALL)
                print(f"📥  Download Speed : {Fore.GREEN}{results['Download']} Mbps{Style.RESET_ALL}")
                print(f"📤  Upload Speed   : {Fore.GREEN}{results['Upload']} Mbps{Style.RESET_ALL}")
                print(f"📶  Ping           : {Fore.GREEN}{results['Ping']} ms{Style.RESET_ALL}")
                print(Fore.MAGENTA + "════════════════════════════════════" + Style.RESET_ALL)

                # Add helpful tip
                print(Fore.BLUE + "\n💡 Tip: Type 'compare-global' to check how your speed compares to the global average." + Style.RESET_ALL)
        else:
            print(Fore.RED + "\n❌ Speed test failed due to an unexpected error." + Style.RESET_ALL)

def run_auto_test():
    print(Fore.MAGENTA + "\n📡 NetSage: Auto Speed Testing & Alerts\n" \
          "══════════════════════════════════════════════════════════════\n" + Style.RESET_ALL)
    print(Fore.CYAN + "⚙️  Configure thresholds and test interval below:\n" + Style.RESET_ALL)

    download_threshold = input("⬇️  Download Threshold (Mbps): ")
    upload_threshold = input("⬆️  Upload Threshold (Mbps): ")
    ping_threshold = input("📶 Ping Threshold (ms): ")
    time_interval = input("⏲️  Test Every (Seconds): ")

    print(Fore.CYAN + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
          "ℹ Press Ctrl+C anytime to stop Auto Testing." + Style.RESET_ALL)

    # Validate input
    if not time_interval.isdigit():
        print(Fore.RED + "\n❌ Invalid ⏲ Time Interval! Please enter a number." + Style.RESET_ALL)
        return

    if not is_float(download_threshold):
        print(Fore.RED + "\n❌ Invalid ⬇ Download Threshold! Must be a number." + Style.RESET_ALL)
        return

    if not is_float(upload_threshold):
        print(Fore.RED + "\n❌ Invalid ⬆ Upload Threshold! Must be a number." + Style.RESET_ALL)
        return

    if not is_float(ping_threshold):
        print(Fore.RED + "\n❌ Invalid 📶 Ping Threshold! Must be a number." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "\n✅ Auto Speed Test Started! Monitoring Every " + time_interval + "s 🔄" + Style.RESET_ALL)
    auto_tst_alert(
                    int(time_interval),
                    float(download_threshold),
                    float(upload_threshold),
                    float(ping_threshold)
                    )

def internet_stat():
    try:
        while True:
            internet_data = check_internet()
            if "internet_status" not in internet_data:
                print(Fore.RED + "\n❌ Failed to retrieve internet status." + Style.RESET_ALL)
                return
            internet_status = internet_data["net_status"]
            trblshoting_suggs = internet_data["suggests"]

            clear_terminal()  # clears the terminal before updating 

            print(Fore.MAGENTA + "\n🌐 NetSage: Live Internet Monitor")
            print("════════════════════════════════════" + Style.RESET_ALL)

            print(f"{Fore.CYAN}📶 Internet Status: {Style.RESET_ALL}{internet_status}")

            print("\n" + Fore.YELLOW + "🛠️  Troubleshooting Suggestions:" + Style.RESET_ALL)
            print(f"\n{Fore.LIGHTWHITE_EX}{trblshoting_suggs}{Style.RESET_ALL}")

            print(Fore.MAGENTA + "\n════════════════════════════════════" + Style.RESET_ALL)
            print(Fore.CYAN + "ℹ Press Ctrl+C to quit this live view.\n" + Style.RESET_ALL)

            TIME.sleep(10)

    except KeyboardInterrupt:
        print(Fore.RED + "\n\n↩ Exiting Live Internet Monitor.\n" + Style.RESET_ALL)

def compare_global():
    print(Fore.MAGENTA + "\n🌍 NetSage: Compare to Global Average\n" \
                        "═════════════════════════════════════════════" + Style.RESET_ALL)

    try:
        running = [True]
        thread = threading.Thread(target=spinner, args=("Comparing Your Speed to Global Averages", running))
        thread.start()

        results = check_speed()
        TIME.sleep(2)  

        global_comparison = get_compareson()

        if "No Speed Test Data Was Given" in global_comparison:
            print(Fore.RED + "\n⚠️  Failed to retrieve your speed data." + Style.RESET_ALL)
            return
        elif "No Global Speed Data Was Given!" in global_comparison:
            print(Fore.RED + "\n⚠️  Failed to retrieve global average data." + Style.RESET_ALL)
            return
        else:
            down_compare, avg_down_sped, up_compare, avg_up_sped, ping_compare, avg_ping = global_comparison

    finally:
        running[0] = False
        thread.join()

        if "Error" in results:
            print(Fore.RED + "\n❌ Speed Test Failed!\n" + Style.RESET_ALL, results["Error"])
        else:
            print(Fore.CYAN + "\n\n📊 Results Summary\n" \
                  "────────────────────────────────────────────" + Style.RESET_ALL)

            print(f"📥 Your Download: {Fore.MAGENTA}{results['Download']} Mbps{Style.RESET_ALL}")
            print(f"🌍 Country Avg  : {Fore.YELLOW}{avg_down_sped} Mbps{Style.RESET_ALL}")
            print(f"📌 Comparison   : {Fore.LIGHTWHITE_EX}{down_compare}{Style.RESET_ALL}\n")

            print(f"📤 Your Upload  : {Fore.MAGENTA}{results['Upload']} Mbps{Style.RESET_ALL}")
            print(f"🌍 Country Avg  : {Fore.YELLOW}{avg_up_sped} Mbps{Style.RESET_ALL}")
            print(f"📌 Comparison   : {Fore.LIGHTWHITE_EX}{up_compare}{Style.RESET_ALL}\n")

            print(f"📶 Your Ping    : {Fore.MAGENTA}{results['Ping']} ms{Style.RESET_ALL}")
            print(f"🌍 Country Avg  : {Fore.YELLOW}{avg_ping} ms{Style.RESET_ALL}")
            print(f"📌 Comparison   : {Fore.LIGHTWHITE_EX}{ping_compare}{Style.RESET_ALL}\n")

            print(Fore.MAGENTA + "\n═════════════════════════════════════════════\n" + Style.RESET_ALL)

def signal_qulty():

    print(Fore.MAGENTA + "\n📡 NetSage: Wi-Fi Signal Strength Detector\n" \
                            "═════════════════════════════════════════════" + Style.RESET_ALL)
    
    try:
        while True:
            check = check_Wifi_quality()  

            clear_terminal()  

            print(Fore.CYAN + "\n📶 Live Wi-Fi Signal Quality Monitor\n" \
                  "────────────────────────────────────────────" + Style.RESET_ALL)

            print(Fore.LIGHTWHITE_EX + check + Style.RESET_ALL)

            print(Fore.CYAN + "\n────────────────────────────────────────────\n" \
                  "ℹ Press Ctrl+C to stop monitoring." + Style.RESET_ALL)

            TIME.sleep(20)

    except KeyboardInterrupt:
        print(Fore.RED + "\n\n↩ Exited Wi-Fi Signal Quality Monitoring.\n" + Style.RESET_ALL)

def isp_info():
    print(Fore.MAGENTA + "\n🌍 NetSage: ISP & Location Information\n" \
                        "════════════════════════════════════════════════" + Style.RESET_ALL)

    running = [True]
    thread = threading.Thread(target=spinner, args=("Fetching ISP & Location Data", running))
    error = None
    try:
        thread.start()
        info = get_ISPndLoc_info()
        if "Error" in info:
            error = info["Error"]
            message = info["Message"]
            print(Fore.RED + f"\n❌ {message}\n {error}" + Style.RESET_ALL)

    finally:
        running[0] = False
        thread.join()

        # if there is an error, stop with return 
        if error:
            return

        print(Fore.CYAN + "\n\n📍 Your Current Network Location & ISP Info\n" \
                             "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + Style.RESET_ALL)

        print(f"{Fore.YELLOW}🔸 Public IP Address:       {Style.RESET_ALL}{Fore.GREEN}{info['IP']}")
        print(f"{Fore.YELLOW}🏙️  City:                   {Style.RESET_ALL}{Fore.GREEN}{info['City']}")
        print(f"{Fore.YELLOW}🗺️  Region:                 {Style.RESET_ALL}{Fore.GREEN}{info['Region']}")
        print(f"{Fore.YELLOW}🌐 Country:                {Style.RESET_ALL}{Fore.GREEN}{info['Country_cli']}")
        print(f"{Fore.YELLOW}🏣 Postal Code:            {Style.RESET_ALL}{Fore.GREEN}{info['Postal']}")
        print(f"{Fore.YELLOW}🕓 Time Zone:              {Style.RESET_ALL}{Fore.GREEN}{info['TimeZone']}")
        print(f"{Fore.YELLOW}📡 ISP Provider:           {Style.RESET_ALL}{Fore.MAGENTA}{info['ISP']}")

        print(Fore.CYAN + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" + Style.RESET_ALL)

def url_info():
    print(Fore.CYAN + "\n🌐🔍 NetSage: WEBSITE CHECKER TOOL\n" \
                "═════════════════════════════════════════════" + Style.RESET_ALL)

    while True:

        print(Fore.CYAN + "ℹ Enter a full URL like https://example.com\n" \
                        "🟦 Type 'q' and press Enter to quit.\n\n" + Style.RESET_ALL)
        
        url = input(Fore.YELLOW + "Enter the Website/URL >> " + Style.RESET_ALL).lower().strip()
        
        url_data = {}
        
        if url == "q":
            print(Fore.RED + "\n↩ Exiting Website Checker!\n" + Style.RESET_ALL)
            break

        else:
            try:            
                running = [True]
                thread = threading.Thread(target=spinner, args=("Checking URL Status", running)) 
                thread.start()

                url_data = check_website_stat(url) 


            except KeyboardInterrupt:
                print(Fore.RED + "\n↩ Exiting Website Checker!\n" + Style.RESET_ALL)
                break
            except Exception as er:
                print(Fore.RED + f"⚠️  An error occurred: {er}\n" + Style.RESET_ALL)
                continue       

            finally:
                running[0] = False       
                thread.join()

                # Defensive: ensure check_website_stat returned the expected dict
                if not isinstance(url_data, dict):
                    # If an error string or unexpected type was returned, show it and exit
                    print(Fore.RED + f"\n⚠️  Unexpected response: {url_data}\n" + Style.RESET_ALL)
                    return

                print(Fore.CYAN + "\n\n🔎 Website Report\n" \
                    "──────────────────────────────────────────────\n" + Style.RESET_ALL)
                # Use .get to avoid KeyError if the key is missing
                if url_data.get("domain_info") is None: # Check if there was an error getting domain info
                        print(f"{Fore.GREEN}📶 Status: {Style.RESET_ALL}\n{url_data.get('status')}")
                else:
                    # Status
                    print(f"{Fore.GREEN}📶 Status: {Style.RESET_ALL}\n{url_data.get('status')}")
                    print(f"{Fore.BLUE}⏱️  Response Time: {Style.RESET_ALL}{round(url_data.get('response_time', 0), 2)} seconds\n")

                    # Meta Info
                    print(f"{Fore.YELLOW}📄 Title: {Style.RESET_ALL}\n{url_data.get('meta_title')}\n")
                    print(f"{Fore.YELLOW}📝 Meta Description: {Style.RESET_ALL}\n{url_data.get('meta_description')}\n")
                    print(f"{Fore.YELLOW}🔷 Domain Info: {Style.RESET_ALL}\n")
                    print(f"{Fore.LIGHTWHITE_EX}{url_data.get('domain_info')}{Style.RESET_ALL}\n")

                    # SSL
                    print(f"{Fore.MAGENTA}🔐 SSL Status: {Style.RESET_ALL}{url_data['ssl_status']}")

                    # IP Info
                    print(f"{Fore.CYAN}🌐 Server IP: {Style.RESET_ALL}{url_data['server_ip']}")

                    # Ping Info
                    print(Fore.GREEN + "\n📡 Ping Results:" + Style.RESET_ALL)
                    for line in url_data["ping"]:
                        print(f"   {Fore.LIGHTWHITE_EX}{line}{Style.RESET_ALL}")
                        TIME.sleep(0.4)  # nice delay

                print(Fore.CYAN + "═════════════════════════════════════════════\n" + Style.RESET_ALL)

def show_table():
    print(Fore.MAGENTA + "\n📅 NetSage: View Past Speed Test Logs in Table\n" \
                "══════════════════════════════════════════════════════════════" + Style.RESET_ALL)

    range_type = filter_date()
    
    # Call backend table rendering function
    tst_hstry_table(range_type)

    print(Fore.CYAN + "\n💡 Additional Options:\n" \
            "  📥 Type 'export' or 'xprt' to export logs as a PDF report\n" \
            "  ❌ Type 'delet' or 'dlt' to delete stored history\n" + Style.RESET_ALL)

def show_graph():
    print(Fore.MAGENTA + "\n📈 NetSage: View Past Speed Test Logs in Graph\n" \
                    "══════════════════════════════════════════════════════════════" + Style.RESET_ALL)

    range_type = filter_date()

    # Call backend graph rendering function
    tst_hstry_graph(range_type)

    print(Fore.CYAN + "\n💡 Additional Options:\n" \
            "  📥 Type 'export' or 'xprt' to export logs as a PDF report\n" \
            "  ❌ Type 'delet' or 'dlt' to delete stored history\n" + Style.RESET_ALL)

def export_logs():

    range_type = filter_date()
    filename = input(Fore.YELLOW + "⬜ Enter a Name for this PDF >> " + Style.RESET_ALL).strip()
    print("")
    if not filename:
        result = export_tst_logs(range_type)
    else:
        result = export_tst_logs(range_type, filename + '.pdf')
    print(Fore.GREEN + result + Style.RESET_ALL)

def delet_data():
    print (Fore.YELLOW + "⚠ Warnig All Your Speed tests History Will Be Deleted❗" + Style.RESET_ALL)
    while True:
        ask = input(Fore.CYAN + "🔶 Do you Confirm Deleting❓ y = Yes / n = No ---> " + Style.RESET_ALL).lower().strip()
        if ask == "y" or ask == "yes":
            delet_rsults()
            print(Fore.MAGENTA + "\nHistory Data is Deleted❗\n" + Style.RESET_ALL)
            break
        elif ask == "n" or ask == "no":
            print(Fore.GREEN + "\nData is Alive✅\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\n❎ Invalid Command❕\n" + Style.RESET_ALL)    

# ======================================= Backend Feature Functions ================================================ #

# === Initialization === #
# render the graphs in the browser
pio.renderers.default = "browser"
os_name = platform.system()
init(autoreset=True)

# === Global Variables === #
user_country = None
user_download_speed = None
user_upload_speed = None
user_ping = None

# Get the download/upload speed and Ping 
def check_speed():
    
    global user_country
    global user_download_speed
    global user_upload_speed
    global user_ping

    try:
        sped_tst = speedtest.Speedtest()
        
        download_speed = sped_tst.download() / 1_000_000
        upload_speed = sped_tst.upload(pre_allocate=False) / 1_000_000
        sped_tst.results.share()

        results_dict = sped_tst.results.dict()

        ping = results_dict['ping']
        timestamp = results_dict['timestamp']
        bytes_sent = int(results_dict['bytes_sent']) / 1_000_000
        bytes_received = int(results_dict['bytes_received']) / 1_000_000

        user_country = results_dict['server']["country"]
        user_download_speed = float(download_speed)
        user_upload_speed = float(upload_speed)
        user_ping = float(ping)

        results = {'Download' : round(download_speed, 2), 
                'Upload' : round(upload_speed, 2), 
                'Ping' : round(ping, 2), 
                'Date_Time' : timestamp, 
                'byts_S' : bytes_sent, 
                'byts_R' : bytes_received, 
                "Country_gui": user_country,
                }
        
        # Save the test results in the Database
        data = (results["Date_Time"], results["Download"], results["Upload"], results["Ping"])
        sav_tst_rsults(data)

    except speedtest.ConfigRetrievalError:
        results = {"Error": "Speedtest config retrieval failed. 💡Check your connection."}
    except speedtest.SpeedtestException as e:
        results = {"Error": str(e)}
    
    return results

# Get ISP and Location info 
def get_ISPndLoc_info():

    # Check for valid token
    if TOKEN is None:
        # Retrive the token from db
        token_key = get_token()
        if token_key is None:
            return {"api_Error": "No API token provided. ISP and Location feature is disabled."}
    else:
        token_key = TOKEN

    api = f"https://ipinfo.io/json?token={token_key}"
    try:
        respons = requests.get(api)
        data = respons.json()
        return {
            "IP": data["ip"],
            "City": data["city"],
            "Region": data["region"],
            "ISP": data["org"],
            "Postal": data["postal"],
            "TimeZone": data["timezone"],
            "Country_cli" : data["country"]
        }
        
    except Exception as er:
        return {"Error" : er,
                "Message" : "🔴 Faild to get the ISP and Location info"
                }

# Get Speed test comapareson with the averge
def get_compareson():

    averge_down_sped = None
    averge_up_sped = None
    averge_ping = None
    down_compare = None
    up_compare = None
    ping_compare = None

    if user_country == None:
        return "⭕ No Speed Test Data Was Given❗"
    
    else:
        try:
            while True:
                respons = requests.get(f'https://www.speedtest.net/global-index/{user_country.lower()}#fixed')
                if respons and respons.status_code == 200:
                    soup = BeautifulSoup(respons.text, "html.parser")
                    break
                elif respons and respons.status_code != 200:
                    print(f"Error: Received status code {respons.status_code}")
                    return f"❌No Global Speed Data Was Given❗"
                elif not respons:
                    print("No response received, retrying...")
                    TIME.sleep(3)  # Wait before retrying
            
            # Scraping the net speed data of countries from the Speedtest site
            down_data = soup.find("div", {"class": "pure-u-1 pure-u-lg-1-2 results-column fixedMedian-results"}) 
            down_data1 = down_data.find("div", {"class": "headings display-flex-md"})  
            down_data2 = down_data1.find("div", {"class": "result-group result-group-icon download display-table display-block-md"})
            down_data3 = down_data2.find("span", {"class": "number"})
            averge_down_sped = float(down_data3.text.strip())

            up_data = soup.find("div", {"class": "pure-u-1 pure-u-lg-1-2 results-column fixedMedian-results"})
            up_data1 = up_data.find("div", {"class": "headings display-flex-md"})  
            up_data2 = up_data1.find("div", {"class": "result-group result-group-icon upload display-table display-block-md"})
            up_data3 = up_data2.find("span", {"class": "number"})
            averge_up_sped = float(up_data3.text.strip())

            ping_data = soup.find("div", {"class": "pure-u-1 pure-u-lg-1-2 results-column fixedMedian-results"})
            ping_data1 = ping_data.find("div", {"class": "headings display-flex-md"})  
            ping_data2 = ping_data1.find("div", {"class": "result-group result-group-icon latency display-table display-block-md"})
            ping_data3 = ping_data2.find("span", {"class": "number"})
            averge_ping = float(ping_data3.text.strip())

            if user_download_speed > averge_down_sped:
                down_compare = "🟢 Your Internet Download Speed is Above the National Average Download Speed. Great! :)"
            elif user_download_speed < averge_down_sped:
                down_compare = "🔴 Your Internet Download Speed is Below the National Average Download Speed. Not Good! :("
            elif user_download_speed == averge_down_sped:
                down_compare = "🟡 Your Internet Download Speed is Equal to the National Average Download Speed. Good! :|"
            
            if user_upload_speed > averge_up_sped:
                up_compare = "🟢 Your Internet Upload Speed is Above the National Average Upload Speed. Great! :)"
            elif user_upload_speed < averge_up_sped:
                up_compare = "🔴 Your Internet Upload Speed is Below the National Average Upload Speed. Not Good! :("
            elif user_upload_speed == averge_up_sped:
                up_compare = "🟡 Your Internet Upload Speed is Equal to the National Average Upload Speed. Good! :|"
            
            if user_ping < averge_ping:
                ping_compare = "🟢 Your Internet latency (Ping) is Below the National Average latency (Ping). Great! :)"
            elif user_ping > averge_ping:
                ping_compare = "🔴 Your Internet latency (Ping) is higher than the National Average latency (Ping). Not Good! :("
            elif user_ping == averge_ping:
                ping_compare = "🟡 Your Internet latency (Ping) is Equal to the National Average latency (Ping). Good! :|"
            

            return (down_compare, averge_down_sped, up_compare, averge_up_sped, ping_compare, averge_ping) 
        except Exception as er:
            return f"❌No Global Speed Data Was Given❗\nError:\n{er}"

# Get the Internet Status and Trubleshooting
def check_internet():

    # Set colors for displayed text
    green = Fore.GREEN
    yellow = Fore.YELLOW
    red = Fore.RED
    reset = Style.RESET_ALL

    local_ip = "192.168.1.1"
    google_adres = "google.com"
    google_ip = "8.8.8.8"

    conect_router = None
    internet_access = None
    ping_ip_dns = None

    internet_status = None
    ping_value = None
    ping_data = []
    trblshoting_suggs = None
    error = None

    # Retrieves the local IP address of the machine.
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        error = "Unable to resolve local IP address."
    
    try:
        result = subprocess.run(["ping", "-n", "1", local_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
        conect_router = result.returncode == 0

        try:
            result = subprocess.run(["ping", "-n", "1", google_adres], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
            internet_access = result.returncode == 0
        except Exception as e:
            error = red + f"❌ Getting the Internet Status failed!\n\nError:\n" + reset + str(e)
            internet_access = False

            try:
                result = subprocess.run(["ping", "-n", "1", google_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
                ping_ip_dns = result.returncode == 0
            except Exception as e:
                error = f"Ping failed: {e}"
                ping_ip_dns = False

    except Exception as e:
        error = f"Ping failed: {e}"
        print(f"Ping failed: {e}")
        conect_router = False

    if conect_router:
        if internet_access:
            process = subprocess.Popen(["ping", google_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in process.stdout:
                if "Average" in line:
                    ping_value = re.match(r".+Average = (?P<value>.+)ms", line).group("value")
                    continue
                ping_data.append(line.strip())
            if ping_value == None:
                error = "Connection issue: No Ping Value!"
                pass 
            if float(ping_value) < 100:
                internet_status = green + f"✅ Good Connection\n📶 Ping is {ping_value}ms" + reset
                trblshoting_suggs = "The connection is above average.\n Everything is good 👌"
            elif float(ping_value) > 200:
                internet_status = yellow + f"🟡 Weak Connection\n📶 Ping is {ping_value}ms, which is high!" + reset
                trblshoting_suggs = (
                    "Weak Connection Detected! \n\n"
                    "💡 Here is how to improve that:\n "
                    "  📌 Move closer to the Wi-Fi router.\n"
                    "  📌 Disconnect unused devices that may be consuming bandwidth.\n"
                    "  📌 Restart your modem/router.\n"
                )
            else:
                internet_status = f"🟢 Online\n📶 Ping is {ping_value}ms"
                trblshoting_suggs = "The connection is stable. \n Everything is fine 👍"
        else:
            if ping_ip_dns:
                internet_status = red + "🔴 DNS Issues" + reset
                trblshoting_suggs = (
                    "- Pages don’t load, but the network is fine.\n\n "
                    "💡 Here is how to deal with that:\n "
                    "  📌 Change DNS settings to Google DNS (8.8.8.8, 8.8.4.4)"
                )
            else:
                internet_status = red + "🔴 No internet Access (Still Connected to The Router/Wi-Fi)" + reset
                trblshoting_suggs = (
                    "- Router is working, but no internet access!\n\n "
                    "💡 Here is How to Fix That:\n "
                    "  📌 Restart your router and check the cables.\n"
                    "  📌 Try connecting to another Wi-Fi or mobile hotspot.\n"
                    "  📌 Run the Windows Network Troubleshooter (for Windows users).\n"
                    "  📌 Check if your ISP has reported any outages.\n"
                    "  📌 If using a VPN, disable it and test again.\n "
                    "🧠 Advanced Fix:\n"
                    "  + Restart the modem, check ISP outage, change DNS"
                )
    else:
        internet_status = red + "🔴 Completely Disconnected From The Router!" + reset
        trblshoting_suggs = (
            "- No connection at all!\n\n "
            "💡 Here is how to deal with that:\n "
            "  📌 Check if Wi-Fi is turned on, reconnect to network.\n"
            "  📌 Check your router if it's on."
        )

    return {"error": error, 
            "net_status": internet_status,
            "suggests": trblshoting_suggs
            }

# Get website Status
def check_website_stat(url):
    
    website_statue = None
    rspn_time = None
    ssl_statu = None
    servr_ip = None
    domain_info = None
    ping_sever = []
    meta_titl = None
    meta_description = None

    try:
        valid = r"^https?://(www\.)?(?P<domain>[^/]+)"
        if re.match(valid, url):
            respns = requests.get(url, verify=True)
        else:
            url = "https://"+url
            respns = requests.get(url, verify=True)

        url_domain = re.search(valid, url).group("domain")
        
        try:
            match respns.status_code:
                case 200:
                    website_statue = "🟢 The website is online and working fine!\n🔶 Status Code: 200 ✅ OK"

                    servr_ip = socket.gethostbyname(url_domain)

                    # getting Ping to the web Server data
                    process = subprocess.Popen(["ping", servr_ip],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
                    for line in process.stdout:
                        ping_sever.append(line.strip())
                    
                    # Getting the Server and domain info
                    try:    
                    
                        servr_info = whois.whois(url_domain)

                        domain_name = servr_info["domain_name"]
                        registrar = servr_info["registrar"]
                        updated_date = format_date(servr_info["updated_date"])
                        creation_date = format_date(servr_info["creation_date"])
                        expiration_date = format_date(servr_info["expiration_date"])
                        name_servers = servr_info["name_servers"]
                        org_name = servr_info["name"]
                        org_address = servr_info["address"]
                        org_city = servr_info["city"]
                        org_state = servr_info["state"]
                        reg_pstl_cd = servr_info["registrant_postal_code"]
                        org_country = servr_info["country"]

                        domain_info = (
                            f"🔹  Domain: {domain_name} | Registrar: {registrar}\n"
                            f"📅  Updated: {updated_date} | Created: {creation_date} | Expires: {expiration_date}\n"
                            f"🌍  Organisation: {org_name}, {org_address}, {org_city}, {org_state}, {org_country} ({reg_pstl_cd})\n"
                            f"🖥️  Name Servers: {', '.join(name_servers)}"
                        )
                    except Exception as er:
                        domain_info = f"Somthing went wrong while getting Server & domain info. Error: {er}"

                    # Getting the SSL Statue 
                    try:
                        sock = socket.create_connection((url_domain, 443))
                        context = ssl.create_default_context()
                        ssl_sock = context.wrap_socket(sock, server_hostname=url_domain)
                        ssl_stat = ssl_sock.getpeercert()
                        ssl_expir_date = datetime.strptime(ssl_stat['notAfter'], "%b %d %H:%M:%S %Y %Z")
                        days_until_expir = (ssl_expir_date - datetime.utcnow()).days

                        if days_until_expir > 30 :
                            ssl_statu = f"✔ SSL is valid. This site is secure. Days until it expires: {days_until_expir}"
                        elif days_until_expir <= 30 :
                            ssl_statu = f"⚠️ Warning: SSL expires soon! in {days_until_expir} days, this site will not be secure"
                        elif days_until_expir < 0 : 
                            ssl_statu = "🚨 SSL has expired! This site is NOT secure!"
                    except Exception as er:
                        ssl_statu = f"Somthing went wrong while getting SSL statue. Error: {er}"

                    # getting the Meta Title & Description
                    try:
                        meta_data = BeautifulSoup(respns.text, "html.parser")
                        # Title
                        meta_titl = meta_data.find("title").text if meta_data.find("title") else "No Title Found"
                        
                        web_meta = meta_data.find("meta", attrs={"name": "description"})
                        # Description
                        meta_description= web_meta["content"] if web_meta else "No Description Found"

                    except Exception as er:
                        meta_titl = f"Somthing went wrong while getting Meta Tag & Title. Error: {er}"

                case 301:
                    website_statue = "🟡 The website has moved. Redirecting...\n🔶 Status Code: 301 🔄 Redirect"
                case 302:
                    website_statue = "🟡 The website has moved. Redirecting...\n🔶 Status Code: 302 🔄 Redirect"
                case 400:
                    website_statue = "🔴 The request was invalid. Check the URL and try again.\n🔶 Status Code: 400 ⚠️ Bad Request"
                case 403:
                    website_statue = "⛔ Access to this website is denied (403 Forbidden).\n🔶 Status Code: 403 🚫 Forbidden"
                case 404:
                    website_statue = "⭕ Error 404: The page does not exist.\n🔶 Status Code: 404 ❌ Not Found"
                case 408:
                    website_statue = "🟠 The website took too long to respond. Try again later.\n🔶 Status Code: 408 ⏳ Request Timeout"
                case 429:
                    website_statue = "🛑 You're making too many requests. Try again later.\n🔶 Status Code: 429 🚦 Too Many Requests"
                case 500:
                    website_statue = "🟤 The website’s server is experiencing issues (Error 500).\n🔶 Status Code: 500 🔥 Internal Server Error"
                case 503:
                    website_statue = "⚫ The website is temporarily down. Try again later.\n🔶 Status Code: 503 🛠 Service Unavailable"
                case _:
                    website_statue = f"🔴 Unexpected Error:\n❗ {respns.status_code} ❗"
            
            rspn_time = respns.elapsed.total_seconds()

        except requests.exceptions.InvalidURL:
            website_statue = "🔴 Badly Formatted URL\nThe URL format is incorrect.\n🔃 Please check it and try again."
        
        except requests.exceptions.ConnectionError:
            website_statue = "🔴 No Internet or Website Down\n💬 The website may be down OR you have no internet connection."
        
        except requests.exceptions.Timeout:
            website_statue = "🔴 Website Too Slow\n💬 The website is taking too long to respond.🔃 Try again later."
        
        except requests.exceptions.TooManyRedirects:
            website_statue = "🔴 Infinite Redirect Loop\n💬 Too many redirects detected. The website may have an issue."
        
        except requests.exceptions.SSLError:
            website_statue = "⚠ Warning: This site does not have a valid SSL certificate.\n💬 Your connection may not be secure!"

    except Exception:
        website_statue = f"❌ The URL doesn't exist or URL format is incorrect.\n🔃 Please check and try again."
    
    return {
            "status": website_statue,
            "response_time": rspn_time,
            "meta_title": meta_titl,
            'meta_description': meta_description,
            "domain_info": domain_info,
            "ssl_status": ssl_statu,
            "server_ip": servr_ip,
            "ping": ping_sever
        }

# Get Wifi signal Quality 
def check_Wifi_quality():
    
    # getting the OS name to run the apropreate cmds
    if os_name == "Windows":
        wf_info_cmnd = "netsh wlan show interfaces"

    elif os_name == "Linux":
        wf_info_cmnd = "iwconfig"

    elif os_name == "Darwin": 
        wf_info_cmnd = "airport -I"
    else:
        print("Unable to get the full Wi-Fi, Unknown OS:", os_name)
    
    process = subprocess.Popen(wf_info_cmnd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True
                               )
    output, error = process.communicate()
    try:
        if not error: 

            ssid_val = re.search(r"SSID\s*:\s*(\S+)\s*B", output).group(1)

            sgnl_qlty = re.search(r"Signal\s*:\s*(\S+)%", output).group(1)

            rssi_value = (float(sgnl_qlty) / 2) - 100
            strngth_statu = None
            if -50 <= rssi_value <= -30:
                strngth_statu = "🔵 Excellent"
            elif -65 <= rssi_value <= -51:
                strngth_statu = "🟢 Good"
            elif -75 <= rssi_value <= -66:
                strngth_statu = "🟡 Fair"
            elif -90 <= rssi_value <= -76:
                strngth_statu = "🔴 Weak"
            elif rssi_value < -90:
                strngth_statu = "❌ Unstable/Disconnected"

            bssid_val = re.search(r"BSSID\s*:\s*(\S+)\s*N", output).group(1)

            receive_rate = re.search(r"Receive rate\s*\(Mbps\)\s*:\s*(\S+)\s*T", output).group(1)

            transmit_rate = re.search(r"Transmit rate\s*\(Mbps\)\s*:\s*(\S+)\s*S", output).group(1)

            Channel = re.search(r"Channel\s*:\s*(\S+)\s*R", output).group(1)
            freq_band = None
            if 1 <= int(Channel) <= 14:
                freq_band = "2.4 GHz"
            if 36 <= int(Channel) <= 165:
                freq_band = "5 GHz"

            return (f"📡 Wi-Fi: {ssid_val}\n" \
                f"📶 Signal Strength: {rssi_value} dBm ({strngth_statu})\n" \
                f"✅ Signal Quality: {sgnl_qlty}%\n" \
                f"⬇ Receive rate: {receive_rate} Mbps | ⬆ Transmit rate: {transmit_rate} Mbps\n" \
                f"🌍 BSSID: {bssid_val}\n" \
                f"🔷 Channel: {Channel} | Frequency Band: {freq_band}"
                )

        else:
            return f"Error: {error}"
    except AttributeError:
        return output  

# ==== Auto testing & Alerting ===== #

# Init For speacking out the alerts
engine = pyttsx3.init()
        
def give_tst(down_threshold, up_threshold, ping_threshold):

    try:

        # Changing the voice to be english
        voices = engine.getProperty('voices')
        # Making sure it's english
        for voice in voices:
            if "english (united states)" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break 

        # Get Speed Test Results
        test = check_speed()

        if "Error" in test:
            err = test['Error']
            print (Fore.RED + "⚠ Warning! Connection Lost ❌ " + Fore.RESET 
                   + Fore.CYAN + f"Time: {datetime.now()}\n" + Fore.RESET
                   + f"Check Your Connection..\nError:\n{err}\n"
                   )
            engine.say("Warning Connection Lost")       
            engine.runAndWait()
            engine.stop()
            return
        
        time = test["Date_Time"]
        # Parse ISO 8601 format
        timestamp = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
        # Format as 'month day, year at hour:min:sec PM/AM'
        date_time = timestamp.strftime('%B %d, %Y at %I:%M:%S %p')

        download = test["Download"]
        upload = test["Upload"]
        ping = test["Ping"]

        dwn_stat = Fore.GREEN +  "✔ Fine"  + Fore.RESET
        up_stat = Fore.GREEN +  "✔ Fine"  + Fore.RESET
        png_stat = Fore.GREEN +  "✔ Fine"  + Fore.RESET

        if  download < down_threshold:
            # trigger an alert
            dwn_stat = Fore.RED + "⚠ Warning! Download Speed is Below the Threshold ⚠" + Fore.RESET
            engine.say("Warning Download Speed is Below the Threshold")
        
        if  upload < up_threshold:
            # trigger an alert
            up_stat = Fore.RED + "⚠ Warning! Upload Speed is Below the Threshold ⚠" + Fore.RESET
            engine.say("Warning Upload Speed is Below the Threshold")   
        
        if  ping > ping_threshold:
            # trigger an alert
            png_stat = Fore.RED + "⚠ Warning! High latency detected! ⚠" + Fore.RESET 
            engine.say("Warning High latency detected!")       

        print(f"""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ 📡 Internet Speed Test Results        ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃     
        ┃ 🕒 Time: {Fore.CYAN + date_time + Fore.RESET}
        ┃     
        ┃ ⬇ Download Speed: {download:.2f} Mbps {dwn_stat} 
        ┃
        ┃ ⬆ Upload Speed: {upload:.2f} Mbps {up_stat} 
        ┃
        ┃ 📶 Ping: {ping:.2f} ms {png_stat}
        ┃ 
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        
        engine.runAndWait()
        engine.stop()

        # Save the test results in the Database
        data = (time, download, upload, ping)
        sav_tst_rsults(data)
        # Delay to not overlap the speach
        TIME.sleep(2)
        return
    
    except speedtest.ConfigRetrievalError:
        print(f"❌ {Fore.RED} You Are Disconnected From the Router!{Fore.RESET} "
             + Fore.CYAN + f"Time: {datetime.now()}\n" + Fore.RESET
        )
        engine.say("You Are Disconnected")       
        engine.runAndWait()
        engine.stop()
        return

def auto_tst_alert(X, down_threshold, up_threshold, ping_threshold):

    schedule.every(X).seconds.do(lambda: give_tst(down_threshold, up_threshold, ping_threshold))

    active = True
    while active:
        try:
            for remaining in range(X, 0, -1):
                sys.stdout.write(f"\r⏳ Next test in {remaining} seconds... ")
                sys.stdout.flush()           
                TIME.sleep(1)
            print("\n🔄 Testing Internet Speed...")
            schedule.run_pending()

        except KeyboardInterrupt:
            ask = input("\nDo you want to disactivate the Auto Test? y = Yes / n = No: --- ").strip().lower()
            if ask == "y" or ask == "yes":
                print("The Auto Test is Disactivated! ❌")
                active = False
            else:
                print("✔ The Auto Test will continue functioning...")
                continue

# ============== End of Auto testing & Alerting ======================= #

# =================== DataBase & Data Visualisation ================= #

# Always create the database in the same folder as this script
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NetSageitorDB.db")

# Create a Database for user API Tokens
def creat_token_table():
    crt_db = sqlite3.connect(DB_PATH)
    crs_db = crt_db.cursor()
    crs_db.execute(""" 
                    CREATE TABLE IF NOt EXISTS "user_tokens" (
                        "service" REAL,
                        "token"	REAL
                        )
                    """)
    crt_db.commit()
    crt_db.close()

# Create a Database For Speed Test history
def creat_table():
    crt_db = sqlite3.connect(DB_PATH)
    crs_db = crt_db.cursor()
    crs_db.execute(""" 
                    CREATE TABLE IF NOt EXISTS "test_results_history" (
                        "timestamp"	REAL,
                        "download"	REAL,
                        "upload"	REAL,
                        "ping"	REAL
                        )
                    """)
    crt_db.commit()
    crt_db.close()

# Retrive API Tokens
def get_token():
    crt_db = sqlite3.connect(DB_PATH)
    crs_db = crt_db.cursor()
    crs_db.execute("SELECT * FROM user_tokens")
    data =  crs_db.fetchall()
    crt_db.commit()
    crt_db.close()
    if data:
        return data[-1][1]  # Return the last saved token
    else:
        return None

def save_token_to_db(token):
    crt_db = sqlite3.connect(DB_PATH)
    crs_db = crt_db.cursor()
    crs_db.execute("INSERT INTO user_tokens VALUES (?,?)", token)
    crt_db.commit()
    crt_db.close()

# Save test data to the database
def sav_tst_rsults(test_data):

    #Save test results to the database/CSV.
    crt_db = sqlite3.connect(DB_PATH)
    crs_db = crt_db.cursor()
    crs_db.execute(f"INSERT INTO test_results_history VALUES (?,?,?,?)", test_data)
    crt_db.commit()
    crt_db.close()

# Fetches test results from the database
def ftch_tst_rsults():

    # fetches test results from the database
    crt_db = sqlite3.connect(DB_PATH)
    crs_db = crt_db.cursor()
    crs_db.execute("SELECT * FROM test_results_history")
    data =  crs_db.fetchall()
    crt_db.commit()
    crt_db.close()
    return data

# Delete History
def delet_rsults():

    crt_db = sqlite3.connect(DB_PATH)
    crs_db = crt_db.cursor()
    crs_db.execute("DELETE FROM test_results_history ")
    crt_db.commit()
    crt_db.close()

# Format the data and generate a graph 
def tst_hstry_graph(range_type="all"):
    results = ftch_tst_rsults()
    if range_type != "all":
        now = datetime.now()
        filtered = []
        for row in results:
            ts = datetime.fromisoformat(row[0].replace("Z", ""))
            if range_type == "24h" and ts > now - timedelta(days=1):
                filtered.append(row)
            elif range_type == "7d" and ts > now - timedelta(days=7):
                filtered.append(row)
            elif range_type == "30d" and ts > now - timedelta(days=30):
                filtered.append(row)
        results = filtered

    if not results:
        print("❗ No test history found ❗")
        ts = f"{datetime.now()}Z"
        results = [(ts.replace(" ", "T"), 0, 0, 0)]

    timestamps = [datetime.fromisoformat(row[0].replace('Z', '')) for row in results]
    downloads = [row[1] for row in results]
    uploads = [row[2] for row in results]
    pings = [row[3] for row in results]

    # Format timestamps for hover text
    hover_times = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in timestamps]

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, subplot_titles=("Download (Mbps)", "Upload (Mbps)", "Ping (ms)"))

    fig.add_trace(go.Scatter(
        x=timestamps, y=downloads, mode='lines+markers', name='Download (Mbps)', line=dict(color='blue'),
        hovertemplate='<b>Date & Time:</b> %{customdata}<br><b>Download:</b> %{y:.2f} Mbps',
        customdata=hover_times
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=timestamps, y=uploads, mode='lines+markers', name='Upload (Mbps)', line=dict(color='green'),
        hovertemplate='<b>Date & Time:</b> %{customdata}<br><b>Upload:</b> %{y:.2f} Mbps',
        customdata=hover_times
    ), row=2, col=1)
    fig.add_trace(go.Scatter(
        x=timestamps, y=pings, mode='lines+markers', name='Ping (ms)', line=dict(color='red'),
        hovertemplate='<b>Date & Time:</b> %{customdata}<br><b>Ping:</b> %{y:.2f} ms',
        customdata=hover_times
    ), row=3, col=1)

    fig.update_layout(
        height=900,
        title_text="Network Speed Test History",
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    fig.update_xaxes(title_text="Date & Time", row=3, col=1)
    fig.update_yaxes(title_text="Mbps", row=1, col=1)
    fig.update_yaxes(title_text="Mbps", row=2, col=1)
    fig.update_yaxes(title_text="ms", row=3, col=1)

    fig.show()

# Show the history as Table in CLI only
def tst_hstry_table(range_type="all"):
    results = ftch_tst_rsults()

    if range_type != "all":
        now = datetime.now()
        filtered = []

        for row in results:
            ts = datetime.fromisoformat(row[0].replace("Z", ""))
            if range_type == "24h" and ts > now - timedelta(days=1):
                filtered.append(row)
            elif range_type == "7d" and ts > now - timedelta(days=7):
                filtered.append(row)
            elif range_type == "30d" and ts > now - timedelta(days=30):
                filtered.append(row)

        results = filtered

    if not results:
        print("❗ No test history found for the selected range ❗")
        return

    table = PrettyTable(["Timestamp", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])
    for row in results:
        tim = datetime.fromisoformat(row[0].replace('Z', '')).strftime("%Y-%m-%d %H:%M:%S")
        table.add_row((tim, row[1], row[2], row[3]))

    pydoc.pager(str(table))

# Export Network Logs as PDF
def export_tst_logs(range_type="all", filename="network_logs.pdf"):

    print(Fore.YELLOW + "Collecting Speed Test History Data ..." + Style.RESET_ALL)
    data = ftch_tst_rsults()
    if not data:
        return "❗ No data to export ❗"

    # Optional filtering
    if range_type != "all":
        now = datetime.now()
        filtered = []
        for row in data:
            ts = row[0]
            try:
                ts = datetime.fromisoformat(ts.replace("Z", ""))
            except:
                ts = datetime.fromtimestamp(ts)
            if range_type == "24h" and ts > now - timedelta(days=1):
                filtered.append(row)
            elif range_type == "7d" and ts > now - timedelta(days=7):
                filtered.append(row)
            elif range_type == "30d" and ts > now - timedelta(days=30):
                filtered.append(row)
        data = filtered

    if not data:
        return "❗ No data available for the selected range ❗"
    print(Fore.BLUE + "Speed Tests History Data Was Collected ✔\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "🔄 Geenerating Your Report, Please Wait ..." + Style.RESET_ALL)

    # If filename is not an absolute path, save to current working directory
    if not os.path.isabs(filename):
        filename = os.path.abspath(filename)

    # Prepare summary statistics
    downloads = [row[1] for row in data]
    uploads = [row[2] for row in data]
    pings = [row[3] for row in data]
    timestamps = [datetime.fromisoformat(row[0].replace('Z', '')) for row in data]
    min_time = min(timestamps).strftime('%Y-%m-%d %H:%M:%S')
    max_time = max(timestamps).strftime('%Y-%m-%d %H:%M:%S')
    avg_download = sum(downloads) / len(downloads)
    avg_upload = sum(uploads) / len(uploads)
    avg_ping = sum(pings) / len(pings)
    max_download = max(downloads)
    min_download = min(downloads)
    max_upload = max(uploads)
    min_upload = min(uploads)
    max_ping = max(pings)
    min_ping = min(pings)

    # Generate and save the graph as an image

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, subplot_titles=("Download (Mbps)", "Upload (Mbps)", "Ping (ms)"))
    hover_times = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in timestamps]
    fig.add_trace(go.Scatter(x=timestamps, y=downloads, mode='lines+markers', name='Download (Mbps)', line=dict(color='blue'), hovertemplate='<b>Date & Time:</b> %{customdata}<br><b>Download:</b> %{y:.2f} Mbps', customdata=hover_times), row=1, col=1)
    fig.add_trace(go.Scatter(x=timestamps, y=uploads, mode='lines+markers', name='Upload (Mbps)', line=dict(color='green'), hovertemplate='<b>Date & Time:</b> %{customdata}<br><b>Upload:</b> %{y:.2f} Mbps', customdata=hover_times), row=2, col=1)
    fig.add_trace(go.Scatter(x=timestamps, y=pings, mode='lines+markers', name='Ping (ms)', line=dict(color='red'), hovertemplate='<b>Date & Time:</b> %{customdata}<br><b>Ping:</b> %{y:.2f} ms', customdata=hover_times), row=3, col=1)
    fig.update_layout(height=900, title_text="Network Speed Test History", showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    fig.update_xaxes(title_text="Date & Time", row=3, col=1)
    fig.update_yaxes(title_text="Mbps", row=1, col=1)
    fig.update_yaxes(title_text="Mbps", row=2, col=1)
    fig.update_yaxes(title_text="ms", row=3, col=1)

    # Save the figure as a temporary PNG
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmpfile:
        fig.write_image(tmpfile.name, width=1200, height=900, scale=2)
        graph_img_path = tmpfile.name

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_title("Network Speed Test Report")

    # Title
    pdf.set_font("Arial", 'B', 20)
    pdf.set_text_color(40, 40, 120)
    pdf.cell(0, 15, "Network Speed Test Report", ln=True, align="C")
    pdf.ln(2)

    # Date range
    pdf.set_font("Arial", '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f"Report Range: {min_time}  to  {max_time}", ln=True, align="C")
    pdf.ln(2)

    # Summary Table
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Summary Statistics", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 8, f"Average Download: {avg_download:.2f} Mbps (Min: {min_download:.2f}, Max: {max_download:.2f})", ln=True)
    pdf.cell(0, 8, f"Average Upload: {avg_upload:.2f} Mbps (Min: {min_upload:.2f}, Max: {max_upload:.2f})", ln=True)
    pdf.cell(0, 8, f"Average Ping: {avg_ping:.2f} ms (Min: {min_ping:.2f}, Max: {max_ping:.2f})", ln=True)
    pdf.ln(4)

    # Embed the graph image
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Speed Test History Graph", ln=True)
    pdf.ln(2)
    # Resize image to fit page width
    img = PIL.Image.open(graph_img_path)
    page_width = pdf.w - 2 * pdf.l_margin
    img_width, img_height = img.size
    aspect = img_height / img_width
    img_display_width = page_width
    img_display_height = img_display_width * aspect
    pdf.image(graph_img_path, x=pdf.l_margin, y=pdf.get_y(), w=img_display_width, h=img_display_height)
    pdf.ln(int(img_display_height) + 4)

    # Detailed Table
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Detailed Speed Test Results", ln=True)
    pdf.set_font("Arial", '', 10)
    pdf.ln(2)
    # Table header
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(45, 8, "Time", border=1, fill=True)
    pdf.cell(35, 8, "Download (Mbps)", border=1, fill=True)
    pdf.cell(35, 8, "Upload (Mbps)", border=1, fill=True)
    pdf.cell(25, 8, "Ping (ms)", border=1, fill=True)
    pdf.ln()
    pdf.set_fill_color(255, 255, 255)
    # Table rows
    for row in data:
        tm = datetime.fromisoformat(row[0].replace('Z', '')).strftime("%Y-%m-%d %H:%M:%S")
        pdf.cell(45, 8, tm, border=1)
        pdf.cell(35, 8, f"{row[1]:.2f}", border=1)
        pdf.cell(35, 8, f"{row[2]:.2f}", border=1)
        pdf.cell(25, 8, f"{row[3]:.2f}", border=1)
        pdf.ln()

    pdf.output(filename)

    # Clean up temp image
    try:
        os.remove(graph_img_path)
    except Exception:
        pass

    return f"✅ Stunning report exported to: {filename}"

# =================== End Data Base & Data Visualisation ================= #

if __name__ == "__main__":
    main()
    
