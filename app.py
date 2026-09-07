from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
class LabHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            html_form = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Log In - Cyber Security</title>
                <style>
                    * {
                        box-sizing: border-box;
                        margin: 0;
                        padding: 0;
                        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
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
                    .top-bar .logo-circle {
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
                    .top-bar .title {
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
                    .main-title {
                        font-size: 32px;
                        font-weight: bold;
                        color: #1c1e21;
                        margin-top: 10px;
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
                        position: relative;
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
                        justify-content: space-between;
                    }
                    .eye-icon {
                        color: #606770;
                        cursor: pointer;
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
                    .forgot-password {
                        text-align: center;
                        margin-top: 16px;
                    }
                    .forgot-password a {
                        color: #0064e0;
                        text-decoration: none;
                        font-size: 15px;
                        font-weight: 500;
                    }
                    .divider {
                        display: flex;
                        align-items: center;
                        text-align: center;
                        margin: 20px 0;
                        color: #8a8d91;
                        width: 100%;
                        font-size: 14px;
                    }
                    .divider::before, .divider::after {
                        content: '';
                        flex: 1;
                        border-bottom: 1px solid #ccd0d5;
                    }
                    .divider:not(:empty)::before {
                        margin-right: .5em;
                    }
                    .divider:not(:empty)::after {
                        margin-left: .5em;
                    }
                    .btn-secondary {
                        width: 100%;
                        padding: 10px;
                        background-color: #e4e6eb;
                        border: none;
                        border-radius: 20px;
                        color: #050505;
                        font-size: 15px;
                        font-weight: 600;
                        cursor: pointer;
                        margin-bottom: 10px;
                        text-align: center;
                    }
                    .btn-green {
                        width: 100%;
                        padding: 10px;
                        background-color: #008037;
                        border: none;
                        border-radius: 20px;
                        color: white;
                        font-size: 15px;
                        font-weight: 600;
                        cursor: pointer;
                        text-align: center;
                    }
                    .footer {
                        margin-top: 30px;
                        text-align: center;
                        color: #65676b;
                        font-size: 13px;
                    }
                    .footer p {
                        margin-bottom: 8px;
                    }
                    .footer a {
                        color: #0064e0;
                        text-decoration: none;
                    }
                </style>
            </head>
            <body>
                <div class="top-bar">
                    <div class="logo-circle">CS.</div>
                    <div class="title">Cyber Security</div>
                </div>
                <div class="container">
                    <h1 class="main-title">Log In</h1>
                    
                    <div class="welcome-box">
                        <div class="welcome-logo">CS.</div>
                        <span class="welcome-text">Welcome to Cyber Security</span>
                    </div>
                    <form action="/login" method="POST">
                        <div class="input-group">
                            <label for="username">Mobile number or email</label>
                            <input type="text" id="username" name="username" required>
                        </div>
                        
                        <div class="input-group">
                            <label for="password">Password</label>
                            <div class="password-wrapper">
                                <input type="password" id="password" name="password" required>
                                <span class="eye-icon">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
                                </span>
                            </div>
                        </div>
                        <button type="submit" class="btn-primary">Log In</button>
                    </form>
                    <div class="forgot-password">
                        <a href="#">Forgot password?</a>
                    </div>
                    <div class="divider">or</div>
                    <button class="btn-secondary">Find your account</button>
                    <button class="btn-green">Create new account</button>
                    <div class="footer">
                        <p style="font-weight: 600; color: #4b4f56; margin-bottom: 16px;">Other options</p>
                        <p>Language: English (US)</p>
                        <p><a href="#">Help Center</a> · <a href="#">Cyber Security Inc.</a></p>
                    </div>
                </div>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_form.encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            parsed_data = parse_qs(post_data)

            # Only detect whether the fields contain something.
            # The actual values are intentionally discarded.
            username_filled = bool(parsed_data.get("username", [""])[0])
            password_filled = bool(parsed_data.get("password", [""])[0])

            print("\n--- Safe Demo Submission ---")
            print("Username field filled:", username_filled)
            print("Password field filled:", password_filled)
            print("----------------------------\n")

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Demo submission received. No credentials were collected.".encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8080), LabHandler)
print("Server running at: http://127.0.0.1:8080")
server.serve_forever()
