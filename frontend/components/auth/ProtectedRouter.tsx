'use client';


import {useRouter} from "next/navigation";
import {useAuthStore} from "@/store/authStore";
import {useEffect, useState} from "react";
import api from "@/api/client";

const fetchCurrentUser = async (token: string) => {
    try {
        console.log("fetchCurrentUser", token);
        const response = await api.get("/users/me", {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });
        return response.data; // return the actual user data
    } catch (error) {
        console.error("Failed to fetch current user:", error);
        throw error; // re-throw so caller can handle it
    }
};


export default function ProtectedRouter({children}: {children: React.ReactNode}) {
    const router = useRouter();
    const {user, token, logout, setUser} = useAuthStore();
    const [loading, setLoading] = useState<boolean>(true);
    useEffect(() => {
        const verifyToken = async () => {
            try {
                // if token not exist
                if (!token) {
                    router.replace("/login");
                    return;
                }
                const res = await fetchCurrentUser(token);
                if (res.data) {
                    setUser(res.data);
                }else {
                    logout();
                    router.replace("/login");
                }
            }catch (error) {
                console.error("Failed to fetch current user:", error);
                logout();
            }finally {
                setLoading(false);
            }
        };
        verifyToken();
    }, [token, router, logout, setUser]);

    if (loading){
        return (
            <div className="flex justify-center items-center h-screen text-gray-500">
                checking authentication...
            </div>
        )
    };

    return <>{children}</>;
}