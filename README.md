# day_tracker
Web app for tracking time

## How this web app works
Everything goes through APIs. User performs post request containing task_name, current_time and status_of_task (completed or started) At the backend service will calculate how much time spent on each task and present infographics and suggestions about your time management.
Users POST request: `/tracker`
```json
{
    "current_datetime": "12:05:23 Dec 14 2023",
    "task_name": "Learning new words in english",
    "status": "Started"
}
```

User GET request: `/tracker`
```json
{
    ""
}
```