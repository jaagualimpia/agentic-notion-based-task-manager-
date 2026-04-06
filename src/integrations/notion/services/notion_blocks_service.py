from src.integrations.notion.core import notion_client

def travel_activities_root_block(root_block_data, path = []) -> list[dict[str, any]]:
    starting_point = notion_client.blocks.children.list(block_id=root_block_data["id"])
    sub_blocks_data = starting_point["results"]
    todo_elements_at_this_level = []

    for sub_block_data in sub_blocks_data:
        if sub_block_data["type"] == "to_do":
            todo_elements_at_this_level.append(
                {
                    "task": sub_block_data["to_do"]["rich_text"][-1]["plain_text"],
                    "path": [point for point in path]
                }
                
            )

        if sub_block_data["has_children"]:
            aux_path = [point for point in path]
            aux_path.append(sub_block_data[sub_block_data["type"]]["rich_text"][-1]["plain_text"])
            todo_elements_at_this_level.extend(travel_activities_root_block(sub_block_data, aux_path))

    return todo_elements_at_this_level