import csv
import os
import signal
import sys

'''
    Copyright Timothy Miller
    NetId: tjmille2
    Email: tjmille2@illinois.edu
    University of Illinois at Urbana-Champaign

'''

signal.signal(signal.SIGINT, signal.SIG_DFL)

path_to_csv = "./PlayStore_Full_2016_06_CSV.csv"

'''

Format:
    1st row = schema for csv

    Name;Url;AppId;RelatedUrls;ReferenceDate;Developer;IsTopDeveloper;DeveloperURL;DeveloperNormalizedDomain;Category;IsFree;Price;Screenshots;
    Reviewers;Score.Total;Score.Count;Score.FiveStars;Score.FourStars;Score.ThreeStars;Score.TwoStars;Score.OneStars;Instalations;CurrentVersion;
    AppSize;MinimumOSVersion;ContentRating;HaveInAppPurchases;DeveloperEmail;DeveloperWebsite;PhysicalAddress;LastUpdateDate;CoverImgUrl;
    InteractiveElements;Permissions;PermissionDescriptions;Description;WhatsNew


'''


def file_exists(file_path):
    if not file_path:
        return False
    elif not os.path.isfile(file_path):
        return False
    else:
        return True


def update_paid_count(content):
    if content == "True":
        global num_free
        num_free += 1
    else:
        global num_paid
        num_paid += 1


def process_line(content):
    global num_camera
    global num_mic
    global num_draw_top
    global num_startup
    global num_camera_mic
    global num_camera_mic_draw_top
    global num_camera_draw_top
    global num_camera_startup
    global num_camera_mic_startup
    global num_camera_mic_draw_top_startup
    global num_camera_draw_top_startup
    global num_apps_with_permission_data
    global num_internet
    global num_internet_mic
    global num_internet_mic_startup
    global num_internet_camera_startup
    global num_internet_camera_startup_mic
    global num_internet_camera_startup_mic_draw_top
    global num_internet_camera_startup_draw_top

    declares_camera_permission = PERMISSION_CAMERA in content
    declares_mic_permission = PERMISSION_MIC in content
    declares_startup_permission = PERMISSION_STARTUP in content
    declares_draw_top_permission = PERMISSION_DRAW_TOP in content
    declares_internet_permission = PERMISSION_INTERNET in content

    if declares_camera_permission:
        num_camera += 1
    if declares_mic_permission:
        num_mic += 1
    if (declares_startup_permission):
        num_startup += 1
    if declares_draw_top_permission:
        num_draw_top += 1
    if declares_camera_permission and declares_mic_permission:
        num_camera_mic += 1
    if declares_camera_permission and declares_mic_permission and declares_draw_top_permission:
        num_camera_mic_draw_top += 1
    if declares_camera_permission and declares_draw_top_permission:
        num_camera_draw_top += 1
    if declares_camera_permission and declares_startup_permission:
        num_camera_startup += 1
    if declares_camera_permission and declares_startup_permission and declares_mic_permission:
        num_camera_mic_startup += 1
    if declares_camera_permission and declares_startup_permission and declares_mic_permission and declares_draw_top_permission:
        num_camera_mic_draw_top_startup += 1
    if declares_camera_permission and declares_startup_permission and declares_draw_top_permission:
        num_camera_draw_top_startup += 1
    if declares_internet_permission:
        num_internet += 1
    if declares_internet_permission and declares_mic_permission:
        num_internet_mic += 1
    if declares_internet_permission and declares_mic_permission and declares_startup_permission:
        num_internet_mic_startup += 1
    if declares_internet_permission and declares_camera_permission and declares_startup_permission:
        num_internet_camera_startup += 1
    if declares_internet_permission and declares_camera_permission and declares_startup_permission and declares_mic_permission:
        num_internet_camera_startup_mic += 1
    if declares_internet_permission and declares_camera_permission and declares_startup_permission and declares_mic_permission and declares_draw_top_permission:
        num_internet_camera_startup_mic_draw_top += 1
    if declares_internet_permission and declares_camera_permission and declares_startup_permission and declares_draw_top_permission:
        num_internet_camera_startup_draw_top += 1

    num_apps_with_permission_data += 1


def print_results():
    print("----------------------------------------------")
    print(str(num_apps) + " apps total on Google Play as of 06/2016")
    print(str(num_apps_with_permission_data) + " apps processed")
    print(str(num_free) + " free apps")
    print(str(num_paid) + " paid apps")
    print(str(100.0 *(num_free + num_paid)) + " apps considered")
    print(str(100.0 * (num_free / num_apps)) + "% are free")
    print(str(100.0 * (num_paid / num_apps)) + "% are paid")
    print("----------------------------------------------")
    print("Absolute values (number of apps found to declare permission)")
    print("- For example, num_camera_mic means number of apps that request permission for camera & microphone")
    print("- Whereas num_camera means number of apps that request permission for camera.")
    print("num_internet " + str(num_internet))
    print("num_internet_mic " + str(num_internet_mic))
    print("num_internet_mic_startup " + str(num_internet_mic_startup))
    print("num_internet_camera_startup " + str(num_internet_camera_startup))
    print("num_internet_camera_startup_mic " + str(num_internet_camera_startup_mic))
    print("num_internet_camera_startup_mic_draw_top " + str(num_internet_camera_startup_mic_draw_top))
    print("num_internet_camera_startup_draw_top " + str(num_internet_camera_startup_draw_top))
    print("num_camera " + str(num_camera))
    print("num_mic " + str(num_mic))
    print("num_draw_top " + str(num_draw_top))
    print("num_startup " + str(num_startup))
    print("num_camera_mic " + str(num_camera_mic))
    print("num_camera_mic_draw_top " + str(num_camera_mic_draw_top))
    print("num_camera_draw_top " + str(num_camera_draw_top))
    print("num_camera_startup " + str(num_camera_startup))
    print("num_camera_mic_draw_top_startup " + str(num_camera_mic_draw_top_startup))
    print("num_camera_mic_startup " + str(num_camera_mic_startup))
    print("num_camera_draw_top_startup " + str(num_camera_draw_top_startup))
    print("----------------------------------------------")
    print("Percentages")
    print("num_internet " + str(100.0 * (num_internet / num_apps_with_permission_data)))
    print("num_internet_mic " + str(100.0 * (num_internet_mic / num_apps_with_permission_data)))
    print("num_internet_mic_startup " + str(100.0 * (num_internet_mic_startup / num_apps_with_permission_data)))
    print("num_internet_camera_startup " + str(100.0 * (num_internet_camera_startup / num_apps_with_permission_data)))
    print("num_internet_camera_startup_mic " + str(
        100.0 * (num_internet_camera_startup_mic / num_apps_with_permission_data)))
    print("num_internet_camera_startup_mic_draw_top " + str(
        100.0 * (num_internet_camera_startup_mic_draw_top / num_apps_with_permission_data)))
    print("num_internet_camera_startup_draw_top " + str(
        100.0 * (num_internet_camera_startup_draw_top / num_apps_with_permission_data)))
    print("num_camera " + str(100.0 * (num_camera / num_apps_with_permission_data)))
    print("num_mic " + str(100.0 * (num_mic / num_apps_with_permission_data)))
    print("num_draw_top " + str(100.0 * (num_draw_top / num_apps_with_permission_data)))
    print("num_startup " + str(100.0 * (num_startup / num_apps_with_permission_data)))
    print("num_camera_mic " + str(100.0 * (num_camera_mic / num_apps_with_permission_data)))
    print("num_camera_mic_draw_top " + str(100.0 * (num_camera_mic_draw_top / num_apps_with_permission_data)))
    print("num_camera_draw_top " + str(100.0 * (num_camera_draw_top / num_apps_with_permission_data)))
    print("num_camera_startup " + str(100.0 * (num_camera_startup / num_apps_with_permission_data)))
    print("num_camera_mic_draw_top_startup " + str(
        100.0 * (num_camera_mic_draw_top_startup / num_apps_with_permission_data)))
    print("num_camera_mic_startup " + str(100.0 * (num_camera_mic_startup / num_apps_with_permission_data)))
    print("num_camera_draw_top_startup " + str(100.0 * (num_camera_draw_top_startup / num_apps_with_permission_data)))

    print("End Process")


if __name__ == "__main__":

    # to avoid "field larger than field limit (131072)" exceptions
    csv.field_size_limit(sys.maxsize)

    ifile = open(path_to_csv, "r")
    read = csv.reader(ifile)
    count = 0
    column_names = []

    PERMISSION_CAMERA = "TAKE PICTURES AND VIDEOS"
    PERMISSION_MIC = "RECORD AUDIO"
    PERMISSION_DRAW_TOP = "DRAW OVER OTHER APPS"
    PERMISSION_STARTUP = "RUN AT STARTUP"
    PERMISSION_INTERNET = "FULL NETWORK ACCESS"

    global num_internet
    num_internet = 0
    global num_internet_mic
    num_internet_mic = 0
    global num_internet_mic_startup
    num_internet_mic_startup = 0
    global num_internet_camera_startup
    num_internet_camera_startup = 0
    global num_internet_camera_startup_mic
    num_internet_camera_startup_mic = 0
    global num_internet_camera_startup_mic_draw_top
    num_internet_camera_startup_mic_draw_top = 0
    global num_internet_camera_startup_draw_top
    num_internet_camera_startup_draw_top = 0
    global num_camera
    num_camera = 0
    global num_mic
    num_mic = 0
    global num_draw_top
    num_draw_top = 0
    global num_startup
    num_startup = 0
    global num_camera_mic
    num_camera_mic = 0
    global num_camera_mic_draw_top
    num_camera_mic_draw_top = 0
    global num_camera_draw_top
    num_camera_draw_top = 0
    global num_camera_startup
    num_camera_startup = 0
    global num_camera_mic_draw_top_startup
    num_camera_mic_draw_top_startup = 0
    global num_camera_mic_startup
    num_camera_mic_startup = 0
    global num_camera_draw_top_startup
    num_camera_draw_top_startup = 0
    global num_apps_with_permission_data
    num_apps_with_permission_data = 0

    num_apps = 0

    global num_free
    num_free = 0
    global num_paid
    num_paid = 0

    print("Starting data analysis")
    ### Data is semicolon separated per row. Some data is malformed so we skip this data to continue processing.
    for row in read:
        split_row = ''.join(row).split(";")
        if count == 0:
            column_names = split_row
        else:
            num_apps += 1
            if len(split_row) != 37:
                pass
            else:
                process_line(split_row[33])
                update_paid_count(split_row[10])
        if count == 0:
            count += 1

    print_results()
