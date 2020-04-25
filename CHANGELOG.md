# Changelog

## 0.3.2
### Added
- New workflow file, namely, `build.yml` for building and publishing docker image.

## 0.2.0
### Added
- `Dockerfile` that serves the app using `gunicorn`
### Changed
- Workflow name changed to **Code Quality & Build**
- `requirements.txt` updated to include `gunicorn`

## 0.1.0
### Added:
- Improved exception handling.
- Automated Unit tests for:
    - Parser
    - API endpoints
- Workflow file with:
    - Linting checks
    - Pytest testing.
    - Test coverage reporting.
- `README.md` with basic description, codecov badge and setup instructions.
### Fixed:
- Linting fixes.
- Form submission now sends a post request.
