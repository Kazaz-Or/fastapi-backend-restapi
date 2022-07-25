GET_ALL_TODOS_SCHEMA = {
    "type": ["object", "boolean"],
    "properties": {"id": {"type": "integer"},
                   "description": {"type": "string"},
                   "complete": {"type": "boolean"},
                   "priority": {"type": "integer"},
                   "title": {"type": "string"}},
    "required": ["id", "description", "complete", "priority", "title"]
}

GET_TODO_BY_ID_SCHEMA = {
    "type": ["object", "boolean"],
    "properties": {"id": {"type": "integer"},
                   "description": {"type": "string"},
                   "complete": {"type": "boolean"},
                   "priority": {"type": "integer"},
                   "title": {"type": "string"}},
    "required": ["id", "description", "complete", "priority", "title"]
}
