import axios, {AxiosRequestConfig} from "axios";
import {useAuthStore} from "@/store/authStore";


const api = axios.create({
    baseURL: 'http://localhost:8001/api/v1',
    headers: {
        'Content-Type': 'application/json'
    },
    withCredentials: true,
});


export default api;