'use client';

import React from 'react'
import LoginForm from "@/components/auth/LoginForm";
import {useRouter} from "next/navigation";
import {useAuthStore} from "@/store/authStore";

const Login = () => {
    const router = useRouter();
    const {login, user, loading} = useAuthStore();
    const handleLogin = async (email: string, password: string) => {
        console.log("login before user", user);
        await login(email, password);
        console.log("login after user", user);
        if (user) router.push("/chat");
    }
    return (
        <div className="flex justify-center items-center min-h-screen bg-gray-50">
            <LoginForm onSubmit={handleLogin} loading={loading}/>
        </div>
    )
}
export default Login;
