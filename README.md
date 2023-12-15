# day_tracker
Web app for tracking time

## Lifecycle
Users interact with service through API. List of endpoints:
- `api/v1/tracker`
- `api/v1/tracker/edit`
- `api/v1/tracker/start`
- `api/v1/tracker/stop`
- `api/v1/tracker/day`, `week`, `month`

1. User performs `GET` request to check if there running task. If `True` api returns: 
    ```json
    // GET : api/v1/tracker
    {
        "id": 1231
        "task_name": "Playing_chess",
        "status": "Active",
        "spent_time": "1:23",
    }
    ```
    else service returns list of tasks:
    ```json
    // GET : api/v1/tracker
    {
        "tasks": [
            {"id": 1231, "task_name": "playing chess"},
            {"id": 1231, "task_name": "computer playing"},
            {"id": 1231, "task_name": "reading chess"}
            ]
    }
    ```
2. User can add or remove tasks with `POST` request: 
    ```json
    // POST: api/v1/tracker/edit
    {
        "task_name": "New Task",
    }

    // get request to remove

    // GET: api/tracker/edit/{task_id}
    ```
3. To start and stop tracking task:
    ```json
    // to start
    GET: api/v1/tracker/start/{id}

    // to stop
    GET: api/v1/tracker/stop/{id}
    ```
To request reports user performs `GET` request with params of which report to request: `api/v1/tracker/report/{day, week, month}`

```json
// GET: api/v1/tracker/report/day
{
   "tasks": [
    {"tasks_name": "playing_chess", "spent_time": "2h"},
    {"tasks_name": "reading", "spent_time": "1h"},
    {"tasks_name": "playing computer", "spent_time": "2h"}
   ]
   "free_time": 12h
}
```
```json
// GET: api/v1/tracker/report/week
{
    "week_days": {
        "Mon": {
            "tasks": [
                {"tasks_name": "", "spent_time": 0}
            ]
            "free_time": 3
            
        },
        "Tue": {},
        "Wed": {},
        "Thu": {},
        "Fri": {},
        "Sat": {},
        "Sun": {}
    }
}
```

```json
// GET: api/v1/tracker/report/month
{
    "weeks" : [
        {
            "tasks": [
                {"task_name": "", "sum": 12},
                {"task_name": "", "sum": 4}
            ]
            "free_time": 23
        }
    ]
}
```