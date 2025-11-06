'use client';

import React, {useEffect} from 'react'
import LoginForm from "@/components/auth/LoginForm";
import {useRouter} from "next/navigation";
import {useAuthStore} from "@/store/authStore";

const Login = () => {
    const router = useRouter();
    const {login, user, loading} = useAuthStore();

    useEffect(() => {
        if (user) router.push('/chat');
    }, [user, router]);

    const handleLogin = async (email: string, password: string) => {
        await login(email, password);
    }
    return (
        <div className="flex justify-center items-center min-h-screen bg-gray-50">
            <LoginForm onSubmit={handleLogin} loading={loading}/>
        </div>
    )
}
export default Login;
