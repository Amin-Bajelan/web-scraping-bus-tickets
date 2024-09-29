import mysql.connector
import database_info

mydb = mysql.connector.connect(
    host=str(database_info.host),
    user=str(database_info.user),
    passwd=str(database_info.passwd),
    database=str(database_info.database),
)


def add_data(id, bus_company_name, bus_description_time, empty_seat, payable, model):
    cursor = mydb.cursor()

    ticket_id_info = int(id)
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
