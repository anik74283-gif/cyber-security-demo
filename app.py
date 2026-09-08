from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os


HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Security Demo</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f0f2f5;
            min-height: 100vh;
        }

        .top-bar {
            background: #0056c6;
            color: white;
            padding: 12px 16px;
            font-size: 22px;
            font-weight: bold;
        }

        .container {
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
            padding: 24px 16px;
        }

        .demo-note {
            background: #fff3cd;
            border: 1px solid #ffe69c;
            color: #664d03;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 13px;
            margin-bottom: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        .welcome {
            text-align: center;
            margin-bottom: 24px;
            font-size: 18px;
        }

        .input-group {
            background: white;
            border: 1px solid #ccd0d5;
            border-radius: 8px;
            padding: 8px 12px;
            margin-bottom: 12px;
        }

        label {
            display: block;
            font-size: 13px;
            color: #606770;
            margin-bottom: 3px;
        }

        input {
            width: 100%;
            border: none;
            outline: none;
            font-size: 16px;
            padding: 4px 0;
        }

        button {
            width: 100%;
            padding: 12px;
            background: #0064e0;
            border: none;
            border-radius: 20px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }

        .footer {
            text-align: center;
            color: #65676b;
            font-size: 13px;
            margin-top: 30px;
        }
    </style>
</head>

<body>

    <div class="top-bar">CS. Cyber Security</div>

    <div class="container">

        <div class="demo-note">
            Cybersecurity training demo — please do not enter real passwords.
        </div>

        <h1>Log In</h1>

        <div class="welcome">
            Welcome to Cyber Security
        </div>

        <form action="/login" method="POST">

            <div class="input-group">
                <label for="username">Demo username or email</label>
                <input type="text" id="username" name="username" required>
            </div>

            <div class="input-group">
                <label for="password">Demo password</label>
                <input type="password" id="password" name="password" required>
            </div>

            <button type="submit">Log In</button>

        </form>

        <div class="footer">
            <p>This is a cybersecurity demonstration.</p>
            <p>No credentials are stored or logged.</p>
        </div>

    </div>

</body>
</html>
"""


class LabHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(HTML_FORM.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

    def do_POST(self):
        if self.path != "/login":
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404 - Not Found")
            return

        content_length = int(self.headers.get("Content-Length", 0))

        post_data = self.rfile.read(content_length).decode("utf-8")
        parsed_data = parse_qs(post_data)

        # Only record whether fields were filled.
        # Actual values are never printed or stored.
        username_filled = bool(parsed_data.get("username", [""])[0])
        password_filled = bool(parsed_data.get("password", [""])[0])

        print(
            "Demo submission:",
            "username filled =", username_filled,
            "password filled =", password_filled,
            flush=True
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

        response = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Demo Result</title>
        </head>
        <body style="font-family:Arial;text-align:center;padding:40px;">
            <h2>Demo submission received</h2>
            <p>No credentials were collected or stored.</p>
            <a href="/">Back to demo</a>
        </body>
        </html>
        """

        self.wfile.write(response.encode("utf-8"))

    def log_message(self, format, *args):
        # Do not log request URLs or other request details.
        return


port = int(os.environ.get("PORT", 8080))

server = HTTPServer(("0.0.0.0", port), LabHandler)

print(f"Server running on port {port}", flush=True)

server.serve_forever()
