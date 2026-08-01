import axios from 'axios';

const API_URL = `${import.meta.env.VITE_API_URL}/users/login`;

export const login = async (email, password) => {
  const response = await axios.post(API_URL, {
    email,
    password,
  });

  return response.data;
};
