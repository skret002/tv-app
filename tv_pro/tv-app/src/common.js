// frontend/src/api/common.js
import axios from 'axios'
export const HTTP = axios.create({
    baseURL: 'http://localhost:8000'
})