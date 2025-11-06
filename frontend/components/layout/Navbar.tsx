'use client';

import Link from "next/link";
import {useAuthStore} from "@/store/authStore";

const Navbar = () => {
    const {user, logout, hydrated} = useAuthStore();

    if (!hydrated) return null;

    return (
        <nav className="flex justify-between items-center px-6 py-4 bg-gray-800 text-white">
            <Link className="font-bold text-xl" href="/">AI Research assistant</Link>
            <div className="space-x-4">
                {user ? (<>
                    <span>Welcome, {user.email}</span>
                    <button
                        className="px-3 py-1 bg-blue-600 rounded hover:bg-blue-700"
                        onClick={logout}
                    >
                        Logout
                    </button>
                </>) : (<>
                        <Link className="px-3 py-1 bg-blue-600 rounded hover:bg-blue-700" href="/login">Login</Link>
                        <Link className="px-3 py-1 bg-green-600 rounded hover:bg-green-700"
                              href="/signup">Register</Link>
                    </>
                )}

            </div>
        </nav>
    )
}
export default Navbar;