import config
import sheets
import datetime
import date_convert


current_sheet_id = config.run_log_google_sheet_id


def log_run(service, run_dist):
    date = datetime.datetime.now().strftime("%D")
    sheets.write_data_list_to_sheet(service, current_sheet_id, "A:C", [run_dist, date,
                                                                       date_convert.get_readable_time()])


def main():
    # Google Sheets Authentication
    service = sheets.authenticate_sheets_api()

    run_dist = 5
    log_run(service, run_dist)


if __name__ == '__main__':
    main()
