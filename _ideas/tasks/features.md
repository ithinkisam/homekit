# Features

## Recurring task

- Description
- Importance (ASAP, high, average, low)
- Priority (ASAP, hard deadline, soft deadline, no deadline)
- Duration
- Custom time windows (complete any time between start and end)
- Frequency (every week on Sunday, every 6 months, etc.)
- Notifications
  - Event reminder
  - Event start
  - Event due
- Sub-tasks
- Notes / metadata
  - Goals (why do I want to do this)
- Active (=true when cancelled/deleted and instances exist)
- History / versions

## Task instance

- Description
- Importance (modifiable\*)
- Priority (modifiable\*)
- Duration (modifiable\*)
- Time window
  - Start date
  - End date
- Previous instance
- Next instance (estimate)
- Sub-tasks [list]
  - Description [string]
  - Order [number]
  - Prerequisite [bool]
- Notes [list]
- Completion date (determines active vs complete) [string:datetime]
- Completion type (complete, cancelled)
- Type (recurring vs one-time-only)
- History / versions

## Task notification

- Task identifier [string]
- Notification date [string:datetime]
- Acknowledged [bool]
- Type (email, app, SMS, web, etc.) [string]

\* "modifiable" allows option to changing only a specific instance or updating the recurring task on which the active task was based
