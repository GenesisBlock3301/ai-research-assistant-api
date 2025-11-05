import {create} from "zustand";
import {persist} from "zustand/middleware";
import api from "@/api/client";


interface User {
    id: string;
    email: string;
    password: string;
}

interface AuthState {
    user: User | null;
    token: string | null;
    loading: boolean;
    login: (email: string, password: string) => Promise<void>;
    register: (email: string, password: string) => Promise<void>;
    logout: () => void;
    setUser: (user: User | null) => void;
}

export const useAuthStore = create<AuthState>()(
    persist(
        (set) => ({
            user: null,
            token: null,
            loading: false,
            setUser: (user) => set({user}),
            login: async (email: string, password: string) => {
                set({loading: true});
                try {
                    const res = await api.post("/users/login", {email, password});
                    set({user: res.data.user, token: res.data.access_token});
                } catch (error) {
                    console.error(error);
                }finally {
                    set({loading: false});
                }
            },
            register: async (email: string, password: string) => {
                set({loading: true});
               try {
                   const res = await api.post("/users/register", {email, password});
                   set({user: res.data.user, token: res.data.access_token});
               } catch (error) {
                   console.error(error);
               } finally {
                   set({loading: false});
               }
            },
            logout: () => set({user: null, token: null}),

        }),
        {name: 'auth_storage'}
    )
);