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
            font-family: -apple-system, BlinkMacSystemFont,
                         "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: #f0f2f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        .top-bar {
            width: 100%;
            background-color: #0056c6;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            color: white;
        }

        .logo-circle {
            border: 2px solid white;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 14px;
            margin-right: 10px;
        }

        .title {
            font-size: 22px;
            font-weight: 600;
        }

        .container {
            width: 100%;
            max-width: 400px;
            padding: 24px 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .demo-note {
            width: 100%;
            background: #fff3cd;
            border: 1px solid #ffe69c;
            color: #664d03;
            padding: 10px 12px;
            border-radius: 8px;
            font-size: 13px;
            margin-bottom: 18px;
            text-align: center;
        }

        .main-title {
            font-size: 32px;
            font-weight: bold;
            color: #1c1e21;
            margin-bottom: 12px;
        }

        .welcome-box {
            display: flex;
            align-items: center;
            margin-bottom: 24px;
        }

        .welcome-logo {
            background-color: #0056c6;
            color: white;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 14px;
            margin-right: 8px;
        }

        .welcome-text {
            font-size: 18px;
            color: #1c1e21;
            font-weight: 500;
        }

        form {
            width: 100%;
        }

        .input-group {
            margin-bottom: 12px;
            background: #ffffff;
            border: 1px solid #ccd0d5;
            border-radius: 8px;
            padding: 8px 12px;
        }

        .input-group label {
            display: block;
            font-size: 13px;
            color: #606770;
            margin-bottom: 2px;
        }

        .input-group input {
            width: 100%;
            border: none;
            outline: none;
            font-size: 16px;
            color: #1c1e21;
            background: transparent;
        }

        .password-wrapper {
            display: flex;
            align-items: center;
        }

        .btn-primary {
            width: 100%;
            padding: 12px;
            background-color: #0064e0;
            border: none;
            border-radius: 20px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 6px;
        }

        .footer {
            margin-top: 30px;
            text-align: center;
            color: #65676b;
            font-size: 13px;
        }
    </style>
</head>

<body>

    <div class="top-bar">
        <div class="logo-circle">CS.</div>
        <div class="title">Cyber Security</div>
    </div>

    <div class="container">

        <div class="demo-note">
            Cybersecurity training demo — please do not enter real passwords.
        </div>

        <h1 class="main-title">Log In</h1>

        <div class="welcome-box">
            <div class="welcome-logo">CS.</div>
            <span class="welcome-text">Welcome to Cyber Security</span>
        </div>

        <form action="/login" method="POST">

            <div class="input-group">
                <label for="username">Demo username or email</label>
                <input type="text" id="username" name="username" required>
            </div>

            <div class="input-group">
                <label for="password">Demo password</label>
                <div class="password-wrapper">
                    <input type="password" id="password" name="password" required>
                </div>
            </div>

            <button type="submit" class="btn-primary">
                Log In
            </button>

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
            self.end_headers()
            return

        content_length = int(self.headers.get("Content-Length", 0))

        # Read the request body but do not retain the actual values.
        post_data = self.rfile.read(content_length).decode("utf-8")

        parsed_data = parse_qs(post_data)

        username_filled = bool(parsed_data.get("username", [""])[0])
        password_filled = bool(parsed_data.get("password", [""])[0])

        # Only record whether fields were filled.
        # Actual credentials are never printed, stored, or logged.
        print(
            "Demo submission:",
            "username filled =", username_filled,
            "password filled =", password_filled
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
        # Prevent request URLs from being written to logs.
        return


port = int(os.environ.get("PORT", 8080))

server = HTTPServer(("0.0.0.0", port), LabHandler)

print(f"Server running on port {port}")

server.serve_forever()
