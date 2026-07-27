import axios from 'axios';

const API_URL = 'http://localhost:5000/users/login'; // Cambia por la URL de tu API

export const login = async (email, password) => {
  const response = await axios.post(API_URL, {
    email,
    password,
  });

  return response.data;
};
