import unittest
from pool import ConnectionPoolImpl


class ConnectionPoolImplTest(unittest.TestCase):

    def setUp(self):
        self.max_connections = 10
        self.pool = ConnectionPoolImpl.get_instance(self.max_connections)

    def tearDown(self):
        ConnectionPoolImpl.reset_instance()

    def test_get_instance_method(self):
        instance = ConnectionPoolImpl.get_instance(self.max_connections)
        self.assertIsNotNone(
            instance, "If getInstance() is called, it should return a non-null instance"
        )

    def test_singleton_behavior(self):
        instance1 = ConnectionPoolImpl.get_instance(self.max_connections)
        self.assertIsNotNone(
            instance1,
            "If getInstance() is called, it should return a non-null instance",
        )
        instance2 = ConnectionPoolImpl.get_instance(self.max_connections)
        self.assertIs(
            instance1,
            instance2,
            "If getInstance() is called multiple times, it should return the same instance",
        )

    def test_reset_instance_method(self):
        instance1 = ConnectionPoolImpl.get_instance(self.max_connections)
        self.assertIsNotNone(
            instance1,
            "If getInstance() is called, it should return a non-null instance",
        )
        ConnectionPoolImpl.reset_instance()
        instance2 = ConnectionPoolImpl.get_instance(self.max_connections)
        self.assertIsNot(
            instance1,
            instance2,
            "If resetInstance() is called, getInstance() should return a new instance",
        )

    def test_initialize_pool(self):
        available_connections = self.pool.get_available_connections_count()
        self.assertEqual(
            available_connections,
            self.max_connections,
            "Number of available connections should be equal to max_connections after initialization",
        )

    def test_get_connection(self):
        connection = self.pool.get_connection()
        self.assertIsNotNone(
            connection,
            "If a connection is requested, it should not be None",
        )
        available_connections = self.pool.get_available_connections_count()
        self.assertEqual(
            available_connections,
            self.max_connections - 1,
            "Number of available connections should decrease after getting a connection",
        )

    def test_release_connection(self):
        connection = self.pool.get_connection()
        self.pool.release_connection(connection)
        available_connections = self.pool.get_available_connections_count()
        self.assertEqual(
            available_connections,
            self.max_connections,
            "Number of available connections should increase after releasing a connection",
        )

    def test_get_available_connections_count(self):
        available_connections = self.pool.get_available_connections_count()
        self.assertEqual(
            available_connections,
            self.max_connections,
            "Number of available connections should be equal to max_connections",
        )

    def test_get_total_connections_count(self):
        total_connections = self.pool.get_total_connections_count()
        self.assertEqual(
            total_connections,
            self.max_connections,
            "Total connections count should be equal to max_connections",
        )


if __name__ == "__main__":
    unittest.main()
