import pytest
import logging

logger = logging.getLogger(__name__)

# logging.basicConfig(filename='RestAPItest.log', level=logging.INFO)

@pytest.mark.django_db
def test_create_task(api_client) -> None:
    """
    Test the create task API
    :param api_client:
    :return: None
    """
    payload = {
        "title": "Wash Ajit's Clothes 2",
        "content": "Wash clothes in the washing machine",
    }

    # Create a task
    response_create = api_client.post("http://127.0.0.1:8000/api/tasks/", data=payload, format="json")
    print(response_create.data)
    task_id = response_create.data["task"]["id"]
    logger.info(f"Created task with id: {task_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["task"]["title"] == payload["title"]

    # Read the task
    response_read = api_client.get(f"http://127.0.0.1:8000/api/tasks/{task_id}", format="json")
    logger.info(f"Read task with id: {task_id}")
    logger.info(f"Response: {response_read.data}")
    assert response_read.status_code == 200
    assert response_read.data["task"]["title"] == payload["title"]


@pytest.mark.django_db
def test_patch_task(api_client) -> None:
    """
    Test the update task API
    :param api_client:
    :return: None
    """
    payload = {
        "title": "Trim the Lawn 2",
        "content": "Trim the lawn with the lawnmower",
    }

    # Create a task
    response_create = api_client.post("http://127.0.0.1:8000/api/tasks/", data=payload, format="json")
    print(response_create.data)
    task_id = response_create.data["task"]["id"]
    logger.info(f"Created task with id: {task_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["task"]["title"] == payload["title"]

    # Update the task
    payload["title"] = "Cut the grass 2"
    response_update = api_client.patch(
        f"http://127.0.0.1:8000/api/tasks/{task_id}", data=payload, format="json"
    )
    logger.info(f"Updated task with id: {task_id}")
    logger.info(f"Response: {response_update.data}")
    assert response_update.status_code == 200
    assert response_update.data["task"]["title"] == payload["title"]

    # Task doesn't exist
    response_update = api_client.patch(
        f"http://127.0.0.1:8000/api/tasks/{task_id + '1'}", data=payload, format="json"
    )
    logger.info(f"Updated task with id: {task_id + '1'}")
    logger.info(f"Response: {response_update.data}")
    assert response_update.status_code == 404

@pytest.mark.django_db
def test_delete_task(api_client) -> None:
    """
    Test the delete task API
    :param api_client:
    :return: None
    """
    payload = {
        "title": "Cook healthy food 2",
        "content": "Cook healthy food for the family with high protein and low fat",
    }

    # Create a task
    response_create = api_client.post("http://127.0.0.1:8000/api/tasks/", data=payload, format="json")
    task_id = response_create.data["task"]["id"]
    logger.info(f"Created task with id: {task_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["task"]["title"] == payload["title"]

    # Delete the task
    response_delete = api_client.delete(f"http://127.0.0.1:8000/api/tasks/{task_id}", format="json")
    assert response_delete.status_code == 204

    # Read the task
    response_read = api_client.get(f"http://127.0.0.1:8000/api/tasks/{task_id}", format="json")
    assert response_read.status_code == 404

    # Task doesn't exist
    response_delete = api_client.delete(f"http://127.0.0.1:8000/api/tasks/{task_id + '1'}", format="json")
    assert response_delete.status_code == 404


