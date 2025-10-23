# Access patterns

## Get all recipes by user

| Partition key | Sort Key |
| ------------- | -------- |
| UserId        | N/A      |

## Get all recipes by tag

| Partition key | Sort key |
| ------------- | -------- |
| UserId        | Tag      |

# Design

## Primary key

| Partition key | Sort key |
| ------------- | -------- |
| UserId        | Tag      |

## Attributes

- Name
- Description
