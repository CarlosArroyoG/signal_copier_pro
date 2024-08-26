import React, { useState, useEffect } from 'react';
import api from '../services/api';

function AdminPanel() {
  const [users, setUsers] = useState([]);
  const [mt5Accounts, setMT5Accounts] = useState([]);

  useEffect(() => {
    fetchUsers();
    fetchMT5Accounts();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await api.getAllUsers();
      setUsers(response.data);
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  const fetchMT5Accounts = async () => {
    try {
      const response = await api.getAllMT5Accounts();
      setMT5Accounts(response.data);
    } catch (error) {
      console.error('Error fetching MT5 accounts:', error);
    }
  };

  const deleteUser = async (userId) => {
    try {
      await api.deleteUser(userId);
      fetchUsers();
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  return (
    <div className="admin-panel">
      <h1>Admin Panel</h1>
      <section>
        <h2>Users</h2>
        <ul>
          {users.map(user => (
            <li key={user.id}>
              {user.username} - {user.email}
              <button onClick={() => deleteUser(user.id)}>Delete</button>
            </li>
          ))}
        </ul>
      </section>
      <section>
        <h2>MT5 Accounts</h2>
        <ul>
          {mt5Accounts.map(account => (
            <li key={account.id}>
              {account.login} - {account.server} (User ID: {account.user_id})
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default AdminPanel;