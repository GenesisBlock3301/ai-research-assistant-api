import React from 'react'
import ProtectedRouter from "@/components/auth/ProtectedRouter";

const Page = () => {
    return (
        <ProtectedRouter>
            <div>Chat</div>
        </ProtectedRouter>
    )
}
export default Page;
