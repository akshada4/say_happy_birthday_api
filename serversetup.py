from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
from twilioAPI import sendMessage

class RequestHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		content_type, p_dict = cgi.parse_header(self.headers.get('content-type'))
		p_dict['boundary'] = bytes(p_dict['boundary'], "utf-8")
		if content_type == 'multipart/form-data':
			fields = cgi.parse_multipart(self.rfile, p_dict)
			sender_name = fields.get('sender-name')
			celebrant_name = fields.get('celebrant-name')
			celebrant_number = fields.get('celebrant-number')
			sendMessage(sender_name[0],celebrant_name[0],celebrant_number[0])

def main():
	PORT = 8006
	server = HTTPServer(('',PORT), RequestHandler)
	server.serve_forever()

if __name__ == '__main__':
	main()