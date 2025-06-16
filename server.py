
#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import unquote

PORT = 5000
SLIDES_DIR = "./cold_email_presentation"

class SlideHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SLIDES_DIR, **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

if __name__ == "__main__":
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if slides directory exists
    if not os.path.exists(SLIDES_DIR):
        print(f"Error: {SLIDES_DIR} directory not found!")
        exit(1)
    
    print(f"Starting slide server...")
    print(f"Serving files from: {os.path.abspath(SLIDES_DIR)}")
    
    with socketserver.TCPServer(("0.0.0.0", PORT), SlideHandler) as httpd:
        print(f"✅ Slide server running on port {PORT}")
        print(f"🚀 Open your slide presentation at the preview URL")
        print(f"📁 Serving {len(os.listdir(SLIDES_DIR))} slide files")
        httpd.serve_forever()
