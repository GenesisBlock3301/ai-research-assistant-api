'use client';

import Link from "next/link";

const Navbar = () => {
    let login = false
    return (
        <nav className="flex justify-between items-center px-6 py-4 bg-gray-800 text-white">
            <Link className="font-bold text-xl" href="/">AI Research assistant</Link>
            <div className="space-x-4">
                {login ? (<>
                    <button
                        className="px-3 py-1 bg-blue-600 rounded hover:bg-blue-700"
                    >
                        Logout
                    </button>
                </>) : (<>
                        <Link className="px-3 py-1 bg-blue-600 rounded hover:bg-blue-700" href="/login">Login</Link>
                        <Link className="px-3 py-1 bg-green-600 rounded hover:bg-green-700" href="/signup">Register</Link>
                    </>
                )}

            </div>
        </nav>
    )
}
export default Navbar;