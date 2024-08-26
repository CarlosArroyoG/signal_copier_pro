import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import SignalForm from '../components/SignalForm';
import api from '../services/api';

function Dashboard() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    fetchAccounts();
  }, []);

  const fetchAccounts = async () => {
    try {
      const response = await api.getMT5Accounts();
      setAccounts(response.data);
    } catch (error) {
      console.error('Error fetching accounts:', error);
    }
  };

  return (
    <div className="dashboard">
      <Sidebar />
      <main>
        <h1>Dashboard</h1>
        <SignalForm />
        <h2>Your MT5 Accounts</h2>
        <ul>
          {accounts.map(account => (
            <li key={account.id}>{account.login} - {account.server}</li>
          ))}
        </ul>
      </main>
    </div>
  );
}

export default Dashboard;