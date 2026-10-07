#!/usr/bin/env python3
"""
Competitive Companion Listener
Automatically commits and pushes Codeforces solutions to GitHub
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import subprocess
import os
import sys


class CompetitiveCompanionHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Handle POST requests from Competitive Companion"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            # Extract problem and code information
            problem = data.get('problem', {})
            source = data.get('source', {})
            code = data.get('code', '')

            contest_id = problem.get('contestId', 'unknown')
            problem_index = problem.get('index', 'unknown')
            problem_name = problem.get('name', f'Problem {problem_index}')

            language = source.get('programming_language', 'python').lower()
            if 'cpp' in language or 'c++' in language:
                ext = 'cpp'
            elif 'python' in language:
                ext = 'py'
            elif 'java' in language:
                ext = 'java'
            elif 'javascript' in language:
                ext = 'js'
            else:
                ext = 'txt'

            folder = os.path.join(str(contest_id), str(problem_index))
            os.makedirs(folder, exist_ok=True)

            filename = f"{problem_index}.{ext}"
            filepath = os.path.join(folder, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)

            print(f"✓ Saved: {filepath}")

            repo_dir = os.getcwd()
            subprocess.run(['git', 'add', filepath], cwd=repo_dir, check=True)

            commit_msg = f"Add {contest_id}/{problem_index} - {problem_name}"
            subprocess.run(['git', 'commit', '-m', commit_msg], cwd=repo_dir, check=True)
            subprocess.run(['git', 'push'], cwd=repo_dir, check=True)

            print(f"✓ Committed and pushed: {commit_msg}")

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'success': True, 'message': f'Saved and pushed {problem_index}'}
            self.wfile.write(json.dumps(response).encode())

        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
        except subprocess.CalledProcessError as e:
            print(f"✗ Git Error: {e}")
            self.send_response(500)
            self.end_headers()
        except Exception as e:
            print(f"✗ Error: {e}")
            self.send_response(500)
            self.end_headers()

    def log_message(self, format, *args):
        return


def main():
    HOST = 'localhost'
    PORT = 10042

    server = HTTPServer((HOST, PORT), CompetitiveCompanionHandler)
    print(f"\n🚀 Competitive Companion Listener Started")
    print(f"📡 Listening on http://{HOST}:{PORT}")
    print(f"✅ Ready to receive Codeforces submissions")
    print(f"⚠️  Press Ctrl+C to stop\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n❌ Server stopped")
        sys.exit(0)


if __name__ == '__main__':
    main()
