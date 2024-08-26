import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:5000/api',
});

api.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default {
  login: (credentials) => api.post('/login', credentials),
  register: (userData) => api.post('/register', userData),
  createSignal: (signalData) => api.post('/signals', signalData),
  getMT5Accounts: () => api.get('/mt5_accounts'),
  addMT5Account: (accountData) => api.post('/mt5_accounts', accountData),
  getAllUsers: () => api.get('/admin/users'),
  getAllMT5Accounts: () => api.get('/admin/mt5_accounts'),
  deleteUser: (userId) => api.delete(`/admin/users/${userId}`),
};