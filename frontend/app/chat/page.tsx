import React from 'react'
import ProtectedRouter from "@/components/auth/ProtectedRouter";

const Page = () => {
    return (
        <ProtectedRouter>
            <div className="p-6">
                <h1 className="text-2xl font-bold mb-4">Chat interface</h1>
            </div>
        </ProtectedRouter>
    )
}
export default Page;
