from unittest import mock
from app.tasks.group_task import run_group_tasks


class TestGroupTask():

    @mock.patch('app.tasks.group_task.chain')
    @mock.patch('app.tasks.group_task.second_task')
    @mock.patch('app.tasks.group_task.first_task')
    def test_run_group_tasks(
        self,
        mock_first_task,
        mock_second_task,
        mock_chain
    ):
        object_ids = [1, 3, 5]
        run_group_tasks.s().apply()

        assert mock_chain.call_count == len(object_ids)

        for object_id in object_ids:
            mock_chain.assert_called_with(
                mock_first_task.si(object_id),
                mock_second_task.si(object_id),
            )
