from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs
import os # 파일 존재 여부 확인을 위해 os 모듈 추가

class SimpleHandler(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "86400") # Preflight 요청 캐싱 시간

    def do_OPTIONS(self):
        self.send_response(204)  # No Content
        self._set_cors_headers()
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/login":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            
            try:
                content_type = self.headers.get('Content-Type', '')
                username = ""
                password = ""

                if 'application/x-www-form-urlencoded' in content_type:
                    form_data = parse_qs(body.decode('utf-8'))
                    username = form_data.get('username', [''])[0]
                    password = form_data.get('password', [''])[0]
                elif 'application/json' in content_type:
                    data = json.loads(body)
                    username = data.get("username")
                    password = data.get("password")
                else:
                    # Content-Type이 명확하지 않을 경우, JSON 파싱을 먼저 시도
                    # 실패하면 form-urlencoded로 시도 (더 유연하게 처리)
                    try:
                        data = json.loads(body)
                        username = data.get("username")
                        password = data.get("password")
                    except json.JSONDecodeError:
                        form_data = parse_qs(body.decode('utf-8'))
                        username = form_data.get('username', [''])[0]
                        password = form_data.get('password', [''])[0]

                print(f"로그인 시도 - 아이디: {username}, 비밀번호: {password}")

                if username == "admin" and password == "1234":
                    self.send_response(200)
                    self._set_cors_headers()
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"message": "로그인 성공"}).encode('utf-8'))
                else:
                    self.send_response(401)
                    self._set_cors_headers()
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"message": "로그인 실패", "error_code": "INVALID_CREDENTIALS"}).encode('utf-8'))
                    
            except json.JSONDecodeError:
                self.send_response(400)
                self._set_cors_headers()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "유효하지 않은 JSON 형식입니다."}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self._set_cors_headers()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": f"서버 내부 오류: {str(e)}"}).encode('utf-8'))

    def do_GET(self):
        if self.path == "/":
            # login-form.html 파일이 현재 디렉토리에 있는지 확인
            html_file_path = os.path.join(os.getcwd(), 'login-form.html')
            if os.path.exists(html_file_path):
                try:
                    with open(html_file_path, 'rb') as file:
                        self.send_response(200)
                        self._set_cors_headers()
                        self.send_header('Content-type', 'text/html; charset=utf-8')
                        self.end_headers()
                        self.wfile.write(file.read())
                except Exception as e:
                    self.send_error(500, f"파일을 읽는 중 오류 발생: {str(e)}")
            else:
                self.send_error(404, "login-form.html 파일을 찾을 수 없습니다.")
        elif self.path == "/favicon.ico":
            self.send_response(204) # No Content for favicon
            self._set_cors_headers()
            self.end_headers()
        else:
            self.send_error(404, "Not Found")


def run(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"서버가 포트 {port}에서 실행 중입니다...")
    print(f"브라우저에서 http://localhost:{port}/ 에 접속하여 테스트하세요.")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
