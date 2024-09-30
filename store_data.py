import mysql.connector
import database_info

Done = bool(False)
def add_data(id_ti, bus_company_name, bus_description_time, empty_seat, payable, model):
    global Done
    mydb = mysql.connector.connect(
        host=str(database_info.host),
        user=str(database_info.user),
        passwd=str(database_info.passwd),
        database=str(database_info.database),
    )
    cursor = mydb.cursor()

    if not Done:
        cursor.execute('TRUNCATE TABLE ticket_info')
        mydb.commit()
        Done = True

    ticket_id_info = int(id_ti)
    company_name_info = str(bus_company_name)
    bus_description_time_info = str(bus_description_time)
    empty_seat_info = str(empty_seat)
    payable_info = str(payable)
    model_info = str(model)

    ticketss = (ticket_id_info, company_name_info, bus_description_time_info, empty_seat_info, payable_info, model_info)
    formula = 'insert into ticket_info(ticketID,company_name,Bus_departure_time,number_empty_seat,amount_payable,bus_model) values (%s,%s,%s,%s,%s,%s)'
    cursor.execute(formula, ticketss)
    result = cursor.fetchall()

    mydb.commit()
