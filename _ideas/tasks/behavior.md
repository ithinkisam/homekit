# Behavior

## Recurring tasks

### Create a recurring task

- Create task shell
- Select first occurrence

### Update a recurring task

- Modify all fields
- Option to update existing/active tasks

### Cancel a recurring task

- Address active tasks (complete or cancel)

## Task instances

### Create one-time-only task (non-recurring)

- Create a single task with all metadata

### Complete a task

- Mark task complete
- Option to select a specific date/time (assume completion = `now()`)
- Complete = true
- Completion type = Completed

### Interact with sub-tasks

- Insert new sub-task (option to modify recurring task)
- Rearrange sub-tasks (option to modify recurring task)
- Remove sub-task (option to modify recurring task)
- Update sub-task (option to modify recurring task)

### Cancel a task

- Indicate task was not completed and will no longer be completed
- Save instance for reporting/metrics/learning
- Complete = true
- Completion type = Cancelled
- Gather info on why task is being cancelled

### Delay a task

- End of time window has been reached
- Extend time window by X units (1 week, 3 days, etc.)
- Option to modify the recurring task (if exists)
  - Extend duration
  - Update frequency
- Store history (e.g. task was delayed 3 times, 2 weeks)
- Gather info on why task is being delayed

## Reporting / insights

- Recurring tasks with frequent modifications
  - Suggest using one-time-only tasks instead
- Frequently delayed task instances
  - Suggest extending duration and/or time window or decreasing frequency
- Frequently cancelled task instances
  - Suggest updating priority/importance
  - Suggest breaking the task into smaller chunks
  - Suggest making a new task with clearer goals
