import axios from 'axios';

const API_URL = 'http://localhost:5000/users/login';

export const login = async (email, password) => {
  const response = await axios.post(API_URL, {
    email,
    password,
  });

  return response.data;
};
