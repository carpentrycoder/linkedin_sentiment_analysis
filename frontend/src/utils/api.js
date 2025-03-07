import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000"; // Django backend URL

const api = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true, // Ensure Django can handle credentials (if needed)
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
