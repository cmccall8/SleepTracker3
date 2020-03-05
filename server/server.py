from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json
from dummydb import DummyDB

db = DummyDB("sleeplogs.db")

#DAYS = ["Monday","Tuesday","Wednesday","Thursday"]

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("It worked!")
        if self.path == "/sleeplogs":
            alllogs = db.readAllRecords()
            print(alllogs)
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(bytes(json.dumps(alllogs), "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes(json.dumps("Not Found"), "utf-8"))

    def do_POST(self):
        print("POST successful!")
        if self.path == "/sleeplogs":
            length = self.headers["Content-Length"]
            body = self.rfile.read(int(length)).decode("utf-8")
            print("RAW body:", body)
            parsed_body = parse_qs(body)
            print("Parsed data:", parsed_body)
            day = parsed_body["day"][0]
            hours = parsed_body["hours"][0]
            db.saveRecord({"day": day, "hours": hours})

            # save day, hours to dummy db
            self.send_response(201)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes(json.dumps("Not Found"), "utf-8"))



def run():
    listen = ("127.0.0.1",8080)
    server = HTTPServer(listen, MyRequestHandler)
    print("Listening...")
    server.serve_forever()

run()
