import requests
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)

class OJClient:
    def __init__(self, base_url=""):
        self.session = requests.Session()
        self.base_url = base_url
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json, text/plain, */*",
        })
        self._csrf_token = None

    def _get_url(self, endpoint: str) -> str:
        return urljoin(self.base_url, endpoint)

    def _update_csrf_token(self):
        try:
            self.session.get(self._get_url("/api/profile"), timeout=10)
            if 'csrftoken' in self.session.cookies:
                self._csrf_token = self.session.cookies['csrftoken']
                self.session.headers['X-CSRFToken'] = self._csrf_token
        except Exception as e:
            logger.error(f"Error updating CSRF token: {e}")

    def login(self, username, password):
        self._update_csrf_token()
        payload = {"username": username, "password": password}
        resp = self.session.post(self._get_url("/api/login"), json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if data.get("error"):
            raise Exception(f"Login failed: {data.get('data')}")
        if 'csrftoken' in self.session.cookies:
            self._csrf_token = self.session.cookies['csrftoken']
            self.session.headers['X-CSRFToken'] = self._csrf_token
        return data

    def get_problems(self, offset=0, limit=50):
        params = {'paging': 'true', 'offset': offset, 'limit': limit}
        resp = self.session.get(self._get_url("/api/problem"), params=params, timeout=20)
        resp.raise_for_status()
        return resp.json()

    def get_submissions(self, offset=0, limit=20, myself=1):
        params = {'limit': limit, 'offset': offset, 'myself': myself}
        resp = self.session.get(self._get_url("/api/submissions"), params=params, timeout=20)
        resp.raise_for_status()
        return resp.json()

    def get_problem(self, problem_id):
        params = {"problem_id": problem_id}
        resp = self.session.get(self._get_url("/api/problem"), params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()

    def submit_code(self, code, language, problem_id):
        self._update_csrf_token()
        payload = {
            "code": code,
            "language": language,
            "problem_id": int(problem_id)
        }
        # OJ API expect form data for submission
        resp = self.session.post(self._get_url("/api/submission"), data=payload, timeout=15)
        resp.raise_for_status()
        return resp.json()

    def get_submission(self, submission_id):
        params = {"id": submission_id}
        resp = self.session.get(self._get_url("/api/submission"), params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
