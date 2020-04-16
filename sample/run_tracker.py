import config
from spotify_controller_repo.sample import gsheets_tool
from furtherpy.sample import date_conv_tool
import datetime


# sets the run log sheet to be used
current_sheet_id = config.run_log_google_sheet_id


def log_run(service, run_dist):
    date = datetime.datetime.now().strftime("%D")
    gsheets_tool.write_data_list_to_sheet(service, current_sheet_id, "A:C", [run_dist, date,
                                                                             date_conv_tool.get_readable_time()])


def main():
    # Google Sheets Authentication
    service = gsheets_tool.authenticate_sheets_api()

    run_dist = 5
    log_run(service, run_dist)


if __name__ == '__main__':
    main()
