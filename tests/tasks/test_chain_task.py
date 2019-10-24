from unittest import mock
from app.tasks.chain_task import run_chain_tasks


class TestChainTask():

    @mock.patch('app.tasks.chain_task.chain')
    @mock.patch('app.tasks.chain_task.chain_second_task')
    @mock.patch('app.tasks.chain_task.chain_first_task')
    def test_run_chain_tasks(
        self,
        mock_chain_first_task,
        mock_chain_second_task,
        mock_chain
    ):
        run_chain_tasks.s().apply()

        mock_chain.assert_called_once_with(
            mock_chain_first_task.s(),
            mock_chain_second_task.s(),
        )
