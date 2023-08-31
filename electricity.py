from flask import Blueprint,make_response
from flask import request
import json
from utility.sqlUtility import SqlUtility as ut
from utility.commonClass import MyCustomException as ex
from utility.commonClass import JsonData as js
electric = Blueprint("electric",__name__)

@electric.route("/insertElectric", methods = ["POST"])
def insert_electric():

    if request.method == "POST":
        try:
            import_data = json.loads(request.get_data())
            print(import_data)
            if "user_id" not in import_data:
                raise ex("userdata is not availabe")
            if "date" not in import_data:
                raise ex("date is not available")
            if "reading" not in import_data:
                raise ex("reading not available")

            elect_date = import_data["date"]
            elect_read = import_data["reading"]
            user_id = import_data["user_id"]
            insert_data = (elect_date, elect_read,user_id)
            insert_query = "insert into electric_data (date,reading,user_id) values (%s,%s,%s)"
            insert_result = ut.insertQuery(insert_query, insert_data)
            out_data = js.out_response
            single_data = {"id": insert_result}
            out_data["status"] = 1
            out_data["data"].append(single_data)
            out_data["Message"] = "Data added successfully"
            return json.dumps(out_data)
        except Exception as e:
            json_data = js.method_error_message
            json_data["message"] = str(e)
            return json.dumps(json_data)
    else:
        return json.dumps(js.method_error_message)
@electric.route("/fetchElectric",methods = ["POST"])
def fetch_electric():
    if request.method == "POST":
        try:
            input_data = json.loads(request.get_data())
            if "user_id" not in input_data:
                raise ex("user data not available")
            user_id = str(input_data["user_id"])
            fetch_query = "select date,reading from electric_data where user_id = %s"
            result = ut.selectQuery(fetch_query, user_id)
            if result is not None:
                out_data = {"status":0,"data":[],"message":""}
                for items in result:
                    single_data = {"date": str(items[0]), "reading": int(items[1])}
                    out_data["data"].append(single_data)
                return json.dumps(out_data)
            else:
                raise ex("Something went wrong,Not able to fetch Data")

        except Exception as e:
            json_data = js.method_error_message
            json_data["message"] = str(e)
            return json.dumps(json_data)

    else:
        return json.dumps(js.method_error_message)
